import random

class Set:
    def __init__(self, elements):
        self.element_dict = {}
        self.elements = []
        for element in elements:
            self.add(element)

    def add(self, element):
        if element not in self.element_dict:    
            self.elements.append(element)
            self.element_dict[element] = len(self.elements)

    def remove(self, element):
        if element in self.element_dict:
            elemIndex = self.element_dict[element]
            last_elem = self.elements.pop()
            self.elements[elemIndex] = last_elem
            self.element_dict[last_elem] = elemIndex
            del self.element_dict[element]

    def random(self):
        ran = random.randint(0, len(self.elements)-1)
        return elements[ran]


