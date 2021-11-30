class Student:
    def __init__(self, name: str, marks: int):
        self._name = name
        self._marks = marks

    def is_passed(self) -> bool:
        if (self._marks > 50):
            return True
        else:
            return False


stud = Student("Jacek", 70)
print(stud.is_passed())
