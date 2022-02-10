# FileNotFoundError

# try this
try:
    file = open("a_nonexistent_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["a non-existent key"])
# if trial was unsuccessful, catch the error
except FileNotFoundError:
    file = open("a_nonexistent_file.txt", "w")
    file.write("This file has been created")
except KeyError as message:
    print(f"The key, {message} does not exist")
# if the trial was successful, do this
else:
    contents = file.read()
    print(contents)
# regardless of the outcome, do this
finally:
    file.close()
