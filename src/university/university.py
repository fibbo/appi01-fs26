from room import Room


class Person:
    def __init__(self, id, name, age, role):
        self.id = id
        self.name = name
        self.age = age
        self.role = role


class Staff(Person):
    def __init__(self, id, name, age, department):
        super().__init__(id, name, age, "Staff")
        self.department = department


class Student(Person):
    def __init__(self, id, name, age, ecs):
        super().__init__(id, name, age, "Student")
        self.ecs = ecs


class Lecture:
    def __init__(self, subject, room, lecturer, students):
        self.subject = subject
        self.lecturer = lecturer
        self.students = students
        self.room = room
        room.book(self)


if __name__ == "__main__":
    lecturer = Staff(1, "Dr. Smith", 45, "Computer Science")
    students = [
        Student(2, "Alice", 20, 30),
        Student(3, "Bob", 22, 28),
        Student(4, "Charlie", 21, 32),
    ]
    room = Room(101, 5)
    lecture = Lecture("Introduction to Programming", room, lecturer, students)
