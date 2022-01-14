#x marks the spot

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')

position = input('Where do you want to put the treasure? ')

# position[1] determines the row on the map
# position[0] determines the object inside the row
(map[(int(position[1])-1)][(int(position[0])-1)]) = 'X'
print(f'{row1}\n{row2}\n{row3}')