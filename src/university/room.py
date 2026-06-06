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
            raise Exception("Room capacity exceeded")
