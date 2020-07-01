"""
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

fname = input("Enter file name:-")
fh = open(fname)
fileList = list()
fileDict = dict()
for line in fh:
    if line.startswith("From "):
        line = line.split()
        fileList.append(line[1])
for email in fileList:
	# if email not in fileDict:
	# 	fileDict[email] = 1
	# else:
	# 	fileDict[email] = fileDict[email] + 1
    fileDict[email] = fileDict.get(email, 0) + 1

maxcount = None
maxword = None
for key, value in fileDict.items():
    if maxcount is None or value > maxcount:
        maxword = key
        maxcount = value

print(maxword, maxcount)
