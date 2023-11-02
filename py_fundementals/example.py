# class User:

#     def __init__(self,user_id,username):
#         self.id = user_id
#         self.username = username
#         self.followers= 0
#         self.following = 0

#     def follow(self,user):
#         user.followers += 1
#         user.following += 1


# user_1 = User("001","karam")
# user_2 = User("002","7amty")
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)


# class Employee:
#     num_of_employees= 0
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + "@company.com"
#         Employee.num_of_employees +=1

#     def full_name(self):
#         return "{} {} ".format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay *1.04)

# print(Employee.num_of_employees)
# emp1 = Employee('karam','oweineh',5000)
# print(Employee.num_of_employees)

# print(emp1.pay)
# emp1.apply_raise()


# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade

# class Course:
#         def __init__(self, name, max_students):
#             self.name = name
#             self.max_students = max_students
#             self.students = []

#         def add_student(self, student):
#             if len(self.students) < self.max_students:
#                 self.students.append(student)
#                 return True
#             return False

#         def get_average_grade(self):
#            value=0
#            for student in self.students:
#                value += student.get_grade()
#            return value/len(self.students)

# s1 = Student("karam", 37, 95)
# s2 = Student("noni", 19, 75)
# s3 = Student("safsoof", 34, 35)

# course = Course("science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.get_average_grade())
# print(course.add_student(s3))


# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"I am {self.name} and i am {self.age} years old")


# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color

#     def speak(self):
#         print("meow")

#     def show(self):
#         print(f"I am {self.name} and i am {self.age} years old and i am {self.color}")


# class Dog(Pet):
#     def speak(self):
#         print("Barking")


# p = Pet("ceaser", 19)
# p.show()
# c = Cat("Bill", 34, "grey")
# c.show()
