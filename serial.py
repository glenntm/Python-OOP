"""Python serial number generator."""
import random

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)
    
    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self):
        self.number = 100

    def generate(self):
        self.number +=1
        print(self.number)
    
    def reset(self):
        self.number =100
        return self.number

class RandomWord:
    counter = 0
    myWords = []
    def __init__(self, filepath):
        self.filepath = filepath
        file = open(filepath, 'r')
        for line in file:
            self.myWords.append(line)
            self.counter += 1
        file.close()
        print(f"{self.counter} words read")

    def random(self):
        print(random.choice(self.myWords))

class SpecialWordFinder(RandomWord):
    def __init__(self, filepath):
        self.actualWords = []
        super().__init__(filepath)
        for word in self.myWords:
            print(word)
            if not (word.isspace() or word.startswith('#')):
                self.actualWords.append(word)
        

    def random(self):
        print(random.choice(self.actualWords))