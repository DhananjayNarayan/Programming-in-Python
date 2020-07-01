"""
 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
 You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

fname = input("Enter file name:")
fh = open(fname)
hourdict = dict()
list2 = list()
for line in fh:
    if line.startswith("From "):
        line = line.split()
        line = line[5].split(":")
        list2.append(line[0])

for hour in list2:
    hourdict[hour] = hourdict.get(hour, 0) + 1



temp = list()
for k, v in hourdict.items():
    newt = (k, v)
    temp.append(newt)



temp = sorted(temp)

for k, v in temp:
    print(k, v)
