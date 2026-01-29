# Please write a program which asks for the number of students on a course and the desired group size.
# The program will then print out the number of groups formed from the students on the course. 
# If the division is not even, one of the groups may have fewer members than specified.

# How many students on the course? 8
# Desired group size? 4
# Number of groups formed: 2
#
# HOw many students on the course? 8
# Desired group size? 3
# Number of groups formed: 4

stud = int(input("How many students on the course? "))
group = int(input("Desired group size? "))

formed = stud // group


print(f"Number of groups formed: {formed}")
