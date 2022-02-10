fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


try:
    make_pie(4)
except IndexError:
    print("Fruit pie")


# Angela's
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")


# make_pie(4)


