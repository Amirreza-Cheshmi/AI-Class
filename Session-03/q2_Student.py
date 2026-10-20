class Student:

  def __init__(self, name, student_id):
    self.name = name
    self.student_id = student_id
    self.grades = {}

  def add_grade(self, course, grade):
    if 0 <= grade <= 20:
      self.grades[course] = grade
    else:
      print("Invalid grade")

  def average(self):
    if len(self.grades) == 0:
      return 0
    total = sum(self.grades.values())
    return total / len(self.grades)

  def best_course(self):
    return max(self.grades, key=self.grades.get)

  def failed_courses(self):
    failed = []
    for course, grade in self.grades.items():
      if grade < 10:
        failed.append(course)
    return failed

  def status(self):
    avg = self.average()
    if avg >= 17:
      return "Excellent"
    elif avg >= 14:
      return "Good"
    elif avg >= 12:
      return "Normal"
    else:
      return "Probation"

  def report(self):
    print("-" * 60)
    print(f"Student : {self.name} *** Student_ID: {self.student_id})")
    for course, grade in self.grades.items():
      print(f"{course}: {grade}")
    print(f"Average : {self.average()}")
    print(f"Best course : {self.best_course()}")
    print(f"Failed courses : {self.failed_courses()}")
    print(f"Status : {self.status()}")
    print("-" * 60)


student1 = Student("mmd", "12345678")
student1.add_grade("Math", 12)
student1.add_grade("Physics", 5)
student1.add_grade("Programming", 20)
student1.add_grade("English", 12)

student2 = Student("amir", "87654321")
student2.add_grade("Math", 14)
student2.add_grade("Physics", 14)
student2.add_grade("Programming", 14)
student2.add_grade("English", 13)

student1.report()
student2.report()

print("Test : ")
student1.add_grade("AI", 25)
