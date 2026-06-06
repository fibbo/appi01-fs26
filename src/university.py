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


class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity

    def book(self, lecture):
        if len(lecture.students) <= self.capacity:
            print(f"Room {self.number} booked for {lecture.subject}")
        else:
            print(
                f"Room {self.number} cannot accommodate {len(lecture.students)} students for {lecture.subject}"
            )


class Lecture:
    def __init__(self, subject, room, lecturer, students):
        self.subject = subject
        self.lecturer = lecturer
        self.students = students
        self.room = room
        room.book(self)
