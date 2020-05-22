"""
Python Gradebook Project to test concepts of Lists.
You are a student and you are trying to organize your subjects and grades using Python. 
Explore what we’ve learned about lists to organize your subjects and scores.
"""


last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects= ['physics', 'calculus', 'poetry', 'history']
subjects.append('computer science')
grades=[98, 97, 85, 88]
grades.append(100)
gradebook=zip(subjects,grades)
gradebook=list(gradebook)
gradebook.append(('visual arts', 93))
#print(gradebook)
full_gradebook= last_semester_gradebook+ gradebook
print(full_gradebook)



