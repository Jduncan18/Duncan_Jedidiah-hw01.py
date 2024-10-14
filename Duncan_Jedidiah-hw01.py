# Jedidiah Duncan
# UWYO COSC 1010
# 10/14/24
# HW 01
# Lab Section: 15
# Sources, people worked with, help given to:
# your
# comments
# here
# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student
 #and their scores
# in different subjects.
#
# Student Data:
students = [{"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},{"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},{"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},{"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}]

alice_avg_score = sum(students[0]["scores"].values())/3
print(alice_avg_score)
bob_avg_score = sum(students[1]["scores"].values())/3
print(bob_avg_score)
charlie_avg_score = sum(students[2]["scores"].values())/3
print(charlie_avg_score)
david_avg_score = sum(students[3]["scores"].values())/3
print(david_avg_score)

students_average = {"alice":alice_avg_score, "bob": bob_avg_score, "charlie":charlie_avg_score, "david":david_avg_score}

print(students_average)

for name in students_average:
    scores_above_80 = []
    if students_average[name] > 80:
        scores_above_80.append(name)
    print(scores_above_80)
    



# Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student's name is the key
 #and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.
# Your task is to calculate the average scores for each student and print the names
# of students
# whose average score is greater than 80.
#Solution
