import math


def paint_calc(height, width, cover):
    area = height * width
    # using math.ceil not round but ceil always rounds up whilst round rounds normally, up or down depending on the preceeding digit
    num_cans = math.ceil(area/cover)
    print(f"You'll need to buy {num_cans} cans of paint")

test_h = int(input('Height of wall: '))
test_w = int(input('Width of wall: '))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)