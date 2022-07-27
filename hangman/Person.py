class Person:
    
    def __init__(self, name, count):
        self.name = name
        self.count = count
        
    def __repr__(self):
        return "{}, {}".format(self.name, self.count)
            