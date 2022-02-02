# to open a file
file = open("my_file.txt")

# to read the contents of the file
contents = file.read()

print(contents)

# to close the file
file.close()

# to automatically close a file after using it
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# to write to a file
# with open("my_file.txt", "w") as file:
#     file.write("New text")

# to append to a file
with open("my_file.txt", "a") as file:
    file.write("\nNew text.")

# writing to a file that does not exist,
# creates a new file with the passed name and writes to it
with open("new_file.txt", "w") as file:
    file.write("New text.")
