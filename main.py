#Emily Gonzalez and Maite Hernandez
# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students

def print_students(data):
    for student in data:
        print("CPSID:", student["CPSID"])
        print("Name:", student["Combo,Name"])
        print("First Name:", student["FName"])
        print("Last Name:", student["LName"])
        if "MName" in student and student["MName"]:  # Check if MName key exists and is not None
            print("Middle Name:", student["MName"])
        print("Home Room:", student["HR"])
        print("Grade Level:", student["GL"])
        print("Emails:", ", ".join(student["Email"]))
        print("-" * 40)  # separator

print("More Students Data:")
print_students(students)

# print(students)
# # ### Problem 1: Count the Students
# Count the number of students in the `student_data` list and print the result.
print(len(students))

# ### Problem 2: Fetching Student Emails
# Given a `CPSID`, iterate over the `student_data` list to find and print the email(s) associated with that `CPSID`.
CPSID_example = input("SomeCPSID")
for student in students: 
  if student["CPSID"] == CPSID_example:
    print(f"Email for CPSID {CPSID_example}: {student['Email']}")
# ### Problem 3: Students with Multiple Emails
# Iterate through the `student_data` list and print the names (`Combo,Name`) of students who have more than one email.
# for student in students:
#   if len(student)
# ### Problem 4: Update Email for a Student
# Choose a `CPSID` and update the email list for that student. After updating, print the updated `student_data` list.

# ### Problem 5: Add a New Student
# Create a new dictionary with all the necessary details of a student and append this dictionary to the `student_data` list. Print the updated list.

# ### Problem 6: Students in a Specific Room
# Given a room number, iterate through the `student_data` list and print the names (`Combo,Name`) of all students in that room.

# ### Problem 7: Search by Name
# Given a partial name string, iterate over the `student_data` list and print all students whose `Combo,Name` contains that substring.

# ### Problem 8: Remove a Student from the List
# Choose a `CPSID` and remove the associated student from the `student_data` list. Print the updated list.

# ### Problem 9: Class Details
# Using the `student_data` list, count and print the number of students enrolled in the "HS2 Chemistry" class.

# ### Problem 10: Unique Teachers
# Create a list of all teachers (`TName`) present in the `student_data` list and print out the unique names from this list.

# ### Problem 11: Email Domain Count
# Iterate over the `student_data` list and create a dictionary where the keys are email domains and the values are counts of students using each domain. Print this dictionary.

# ---


###########################I rephrased all the problems above  in another way to make it easier to read and understand. Here is the rephrased version of the problem sets############################################
# Alright, folks, let's have some fun with our student data! Here's what I want you to do with our student_data list:

# 📌 Problem 1: Can you count how many students are in our list and show me the number?

# 📌 Problem 2: If I give you a student ID (let's call it CPSID), can you find their email for me? Give it a shot!

# 📌 Problem 3: Some students have more than one email, I know, wild! Can you show me who they are by their names?

# 📌 Problem 4: Imagine you're a student, and you just updated your email. If I give you a CPSID, can you swap out their old emails with the new ones? And then, show me what our list looks like after!

# 📌 Problem 5: Let's make a new friend! Add a new student to our list with all their details. Show me our bigger group after!

# 📌 Problem 6: I lost my class. 🙈 If I give you a room number, can you find out which students are in that room?

# 📌 Problem 7: I remember a part of someone's name, but not the whole thing. If you search our list, can you show me everyone that has that name part?

# 📌 Problem 8: Oops, someone left our school. If I give you their CPSID, can you remove them from our list and then show me the updated list?

# 📌 Problem 9: Curious minds want to know: how many of us are in the "HS2 Chemistry" class? Can you count and show me?

# 📌 Problem 10: We have some cool teachers! Can you make a list of all their names without repeating any of them?

# 📌 Problem 11: Emails are fun, right? Can you check which email domains (like example.com) we're using and count how many of us use each? Then, show me what you got!





# print("More Students Data:")
# print_students(students)



