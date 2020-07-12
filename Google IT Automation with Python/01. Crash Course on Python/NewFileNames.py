"""
Given a list of filenames, we want to rename all the files with extension hpp to the extension h. 
To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. 
"""
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for x in range(len(filenames)):
    old_name = filenames[x]
    if old_name.endswith(".hpp"):
      new_name = old_name.replace('.hpp','.h')
    else:
      new_name = old_name;
    newfilenames.append( new_name)
print (newfilenames)
