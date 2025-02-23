class Student:
    def talk(self):
        print("Says something")

class Bachelor(Student):
    def talk(self):
        print("Says something smart")

class Masters(Student):
    def talk(self):
        print("Says something very smart")

class PhD(Student):
    def talk(self):
        print("Says something very-very smart")

Bachelor().talk()   # Expected: Says something smart
Masters().talk()    # Expected: Says something very smart
PhD().talk()        # Expected: Says something very-very smart