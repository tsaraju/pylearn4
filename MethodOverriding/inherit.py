class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_profile(self):
        print("User Details: ")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

class Student(User):
    def __init__(self, name, email, course):
        super().__init__(name, email)
        self.course = course

    def display_profile(self):
        super().display_profile()
        print(f"Student assigned to course {self.course}")

    def submit_assignment(self, concept):
        print(f"Submitted assignment for the {concept}")

class Mentor(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def display_profile(self):
        super().display_profile()
        print(f"Mentor is dealing with subject {self.subject}")

    def create_course(self, course_name):
        print(f"Mentor created the course {course_name}")

class Admin(User):
    def __init__(self, name, email, access):
        super().__init__(name, email)
        self.access = access

    def display_profile(self):
        super().display_profile()
        print(f"Admin has the access rights {self.access}")

    def apply_permissions(self, permission):
        print(f"Admin provided the permissions {permission}")

# Create objects
student = Student("Raju", "raju@gmail.com", "Python Programming")
mentor = Mentor("Ramu", "ramu@yahoo.com", "Python")
admin = Admin("Admin", "admin@gmail.com", "Write")

# Demonstrate overridden methods
student.display_profile()
student.submit_assignment("Inheritance Assignment")

print()

mentor.display_profile()
mentor.create_course("Advanced Python")

print()

admin.display_profile()
admin.apply_permissions("Read")