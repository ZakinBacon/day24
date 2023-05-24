# opening a file and reading the contents.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# mode w for write, a for append, r read
with open("my_file.txt", mode="a") as file:
    file.write("New Text. \n")

# creating a new file and writing too it
with open("new_file.txt", mode="w") as file:
    file.write("New Text. \n")