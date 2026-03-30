# File Handling in Python
# Opening a file in write mode (this will create the file if it doesn't exist)

# Writing to a file
file = open("data.txt", "w")
file.write("Hello Ahmad\n")
file.write("Learning Python File Handling")
file.close()

# Reading from a file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Appending to a file
file = open("data.txt", "a")
file.write("\nThis is an appended line.")
file.close()

# Reading the updated file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Using 'with' statement for better file handling (automatically closes the file)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
    
    