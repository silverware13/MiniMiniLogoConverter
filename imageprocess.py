# By Zachary Thomas
# Transform image in binary
# into MiniMiniLogo commands
# 2/13/2019

# Import modules.
from __future__ import print_function
import string

# Open our output file.
outf= open("OwlCmd.txt","w+")

# The horizontal and vertical depth across the image
h = 0
hs = 0
v = 131

# If the pen is down or not.
p = 0

with open("owl.txt") as inFile:
    while True:
        c = inFile.read(1)
        if not c:
            break
        h = h + 1
        if c == '1':
		if p == 0:
			p = 1
			hs = h
        
	if c == '0':
		if p == 1:
			p = 0
			outf.write("      ln " + str(hs) + " " + str(v) + " " + str(h) + " " + str(v) + " ++ \n")
        
	if c == '\n':
		if p == 1:
			p = 0
			outf.write("      ln " + str(hs) + " " + str(v) + " " + str(h) + " " + str(v) + " ++ \n")
		h = 0
		v = v - 1
