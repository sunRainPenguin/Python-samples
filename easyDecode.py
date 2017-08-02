# from __future__ import print_function
# statements = raw_input("Enter a word:")


# for letter in statements:
    # if letter.isalpha():
        # if ord(letter)+2>ord('z'):
            # print(chr(ord(letter)-24),end="")
        # else:
            # print(chr((ord(letter)+2)),end="")
    # else:
        # print(letter,end="")
		
# -*- coding: UTF-8 -*-
from string import maketrans

input = "abcdefghijklmnopqrstuvwxyz"
ouput = "cdefghijklmnopqrstuvwxyzab"
tranRegular = maketrans(input,ouput)

statements = raw_input("Enter statements:")
print statements.translate(tranRegular)