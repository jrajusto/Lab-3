"""
File: student.py
Resources to manage a student's name and test scores.
"""

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
    student_1 = Student("Ken", 5)
    student_2 = Student("Ericka", 5)
    
    print("Does student 1's name come after student 2's name in alphabetical order or they are the same?")
    print(student_1 >= student_2)
    print("Does student 1's name the same as student 2's name?")
    print(student_1 == student_2)
    print("Does student 1's name come before student 2's name in alphabetical order ?")
    print(student_1 < student_2)
  

    

if __name__ == "__main__":
    main()


