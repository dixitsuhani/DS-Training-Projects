# Create a class that demonstartes the use of private and protected members.

class Demo:
    def __init__(self):
        self._protected = "Protected"
        self.__private = "Private"

    def show(self):
        print(self._protected)
        print(self.__private)

d = Demo()
d.show()