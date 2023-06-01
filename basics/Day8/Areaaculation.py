import math
test_h=int(input("Height of the Wall: "))
test_w=int(input("Width of the wall: "))
coverage=5

def paint_calc(height,width,cover):
    area=height*width
    can_req=math.ceil(area/cover)
    print(f"total {can_req} number of can's required for paint.")


paint_calc(height=test_h,width=test_w,cover=coverage)