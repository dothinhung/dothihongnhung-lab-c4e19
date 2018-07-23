def is_inside(first_list, second_list):
    # x1, y1 là tọa độ x,y
    x1 = first_list[0] 
    y1 = first_list[1]
    # x2, y2 là tọa độ bắt đầu hình chữ nhật
    x2 = second_list[0]
    y2 = second_list[1]
    width = second_list[2]
    height = second_list[3]

    check = True
    if (x2 <= x1 <= x2 + width) and (y2 <= y1 <= y2 + height):
        check = True
    else: 
        check = False
    
    return check

# check = is_inside([100, 120], [140, 60, 100, 200])
check = is_inside([200, 120], [140, 60, 100, 200])

if check == True:
    print("Your function is correct")
else:
    print("Oops, bugs detected")

