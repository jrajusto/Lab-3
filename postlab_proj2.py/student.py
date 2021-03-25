"""
File: student.py
Resources to manage a student's name and test scores.
"""

import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __eq__(self,other):
        return self.name == other.name

    def __lt__(self,other):
        return self.name < other.name

    def __ge__(self,other):
        return self.name >= other.name
    def __str__(self):
        return "Name: " + self.name  + "\nScores: " + \
        " ".join(map(str, self.scores))


def main():
    """A simple test."""
    s_list = []
    ctr = int(input("Enter how many students will be in the list:"))

    for i in range(ctr):
        s_name = str(input("Enter name of student to be added in the list:"))
        s_list.append(Student(s_name, i))

    print('\n')

    random.shuffle(s_list)
    print("This is the shuffled list of students:", end= " ")

    for j in range(len(s_list)):
        print(s_list[j].name, end= ", ")

    print('\n')
    s_list.sort()
    print("This is the sorted list of students by their Name:", end= " ")

    for k in range(len(s_list)):
        print(s_list[k].name, end=", ")

    print('\n')

if __name__ == "__main__":
    main()


