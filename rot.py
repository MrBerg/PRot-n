#!/usr/bin/env python3
import sys
import os.path
import argparse

def rotate(text, nrOfRotations):
	while int(nrOfRotations) <0:
		nrOfRotations = int(nrOfRotations) + 26
	splitText = str(text).split()
	newText = []
	for word in splitText:
		newWord = ""
		for i in range(len(word)):
			if word[i].isupper():
				newChar = ord(word[i]) + (int(nrOfRotations)%26)
				if newChar>90:
					newChar = newChar-26
			elif word[i].islower():
				newChar = ord(word[i]) + (int(nrOfRotations)%26)
				if newChar>122:
					newChar = newChar-26
			else:
				newChar = ord(word[i])
			newWord = newWord + chr(newChar)
		newText.append(newWord)
	return " ".join(newText)

def reverseInput(text):
	return text[::-1]

def main():
#	usage = "Usage: %prog [options] arg1 arg2"
	desc = "Use a rot-n cipher on a text"
	parser = argparse.ArgumentParser(description=desc)
	#parser.add_argument("-i","--input", dest="input", type=argparse.FileType('r'),help="Use input file instead of stdin") #TODO Check if file exists
	parser.add_argument("-n", type=int, dest="number", help="number of rotations to perform (13 by default)", default=13)
	parser.add_argument("-f", "--file", metavar="FILE", type=argparse.FileType('w'), dest="filename", default=sys.stdout,help="write output to FILE instead of stdout")
	parser.add_argument("-r", "--reverse",action="store_true", help="reverse the string before rotating it", dest="reverse")
	parser.add_argument("-a", "--auto", action="store_true", dest="auto", help="go through all possible rotations (1-25)")
	args = parser.parse_args()
#	print(args)
#	if not os.path.exists(args.input):
	inputText = input("What text do you want to rotate?\n")
#	else:
#	inputText = open(args.input)
#	reverse = input("Do you want to reverse the input? (y/n)\n")
	if args.reverse:
		text = reverseInput(inputText)
	else:
		text = inputText
#	auto = input("Do you want to go through all possibly solutions? (y/n)\n")
	if args.auto:
		for i in range(25):
			result = rotate(text, i+1)
			print("ROT-{:g}:\n{:s}".format(i+1, result), file=args.filename)
	else:
		#number = input("For how many rotations?\n")
		result = rotate(text, args.number)
		print(result, file=args.filename)
	return
if __name__ == '__main__':
    sys.exit(main())
