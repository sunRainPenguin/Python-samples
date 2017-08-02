from __future__ import print_function
# input = raw_input("Enter the Strings:\n")

# for letter in input:
    # if(letter.isalpha()):
        # print(letter,end="")
input = open("input.txt")
lineNum = 0
for line in input:
    lineNum = lineNum+1
    for letter in line:
        if(letter.isalpha()):
            print(letter,end="")
            print(lineNum)