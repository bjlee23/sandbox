import json
import os
import glob

file_directory = os.path.join(os.environ["HOMEPATH"], "Desktop\\SF_Reports\\*.json")
files = glob.glob(file_directory)

#Length - Specific Walls
length_full_storefront = 0
length_partial_storefront = 0
length_other_storefront = 0
length_gyp_walls = 0

#AREA - General
area_usf = 0
area_rooms = 0

#AREA - Specific Rooms
area_offices = 0

#AREA - Program Types
area_work = 0

#COUNT - General
count_door_storefront_slider = 0
count_door_storefront_swing = 0
count_door_storefront_other = 0
count_door_other = 0

for file_name in files: 
    file_path = os.path.join(file_directory, file_name)
    with open(file_name) as f:
        json_dict = json.loads(f.read())
        elements = json_dict[list(json_dict)[0]]
        type(elements)
        for key, value in elements.items():
            element = elements[key]

            parameters = element["Parameters"]

            #------------------------WALLS--------------------------#
            if element["Category"] == "Walls":
                wall_name = element["Name"].lower()
                try:
                    wall_length = parameters["Length"]
                except:
                    print(element["Name"])

                if "storefront" in wall_name.lower():
                    if "full" in wall_name.lower():
                        length_full_storefront += wall_length
                    elif "partial" in wall_name.lower():
                        length_partial_storefront += wall_length
                    else:
                        length_other_storefront += wall_length

                elif "gyp" in wall_name.lower():
                    length_gyp_walls += wall_length

            #------------------------ROOMS--------------------------# 
            elif element["Category"] == "Rooms":
                room_name = parameters["Name"]
                room_program = parameters["ProgramType"]
                try:
                    room_area = element["Area"]
                except:
                    try:
                        room_area = parameters["Area"]
                    except:
                        print(element["UniqueId"])
                        print(element["Project Name"])
                        continue

                area_rooms += room_area

                if "work" in room_program.lower():
                    area_work += room_area

                if "office" in room_name.lower():
                    area_offices += room_area

            #------------------------AREAS--------------------------#
            elif element["Category"] == "Areas":
                try:
                    area_area = element["Area"]
                except:
                    try:
                        area_area = parameters["Area"]
                    except:
                        print(element["UniqueId"])
                        print(element["Project Name"])
                        continue
                area_usf += area_area

            #------------------------DOORS--------------------------#
            elif element["Category"] == "Doors":
                try:
                    door_name = element["Name"]
                except:
                    try:
                        door_name = element["Id"]["Name"]
                    except:
                        print(element["UniqueId"])
                        print(element["Project Name"])
                        continue
                host_name = element["Host"]["Name"]
                if "storefront" in host_name.lower():
                    count_door_storefront_slider += 1
                else:
                    count_door_other += 1




print(length_full_storefront)
print(length_partial_storefront)
print(length_other_storefront)
print(length_gyp_walls)
print(area_offices)
print(area_rooms)
print(area_usf)
print(((length_full_storefront + length_partial_storefront)/area_usf))
print(area_offices/area_rooms)
print(area_offices/area_usf)
print(count_door_storefront_slider)
print(count_door_other)

print((count_door_storefront_slider/area_usf))