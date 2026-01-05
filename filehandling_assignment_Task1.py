"""

Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

"""
""" 
with open( "sample1.txt",'wt') as fh:
    line1 =fh.write("Line1 : This is a sample text file\n ")
    line2 =fh.write("Line 2 : It contains multiple lines\n")
"""
"""
with open("sample1.txt","rt") as fh:
   line1= fh.readline()
   line2 = fh.readline()

print("Reading files  contains : \n")
print(line1)
print(line2)
"""

"""
If the file does not exist:
"""
try:
    with open("sample1.txt","rt") as fh:
        data =fh.read()
        print(data)
except FileNotFoundError as  fileError:
    print("THE FILE YOU ARE TRYING TO OPEN IS DOSE NOT EXISTS ...!")
    print(fileError)
else:
    print(data)