"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file
"""
with open("output.txt","rt") as fh:
    content = fh.read()

print(content)

user_input= input("Enter the text you want to insert in the file: ")

with open("output.txt","at") as fh:
      print("\n")
      fh.write("\n"+ user_input)

print("Text appended successfully")

with open("output.txt","rt") as fh:
    content = fh.read()

print(content)

