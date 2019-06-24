## 1. Introduction ##

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}
i = 21
f = 3.5
print(type(l))
print(type(s))
print(type(d))
print(type(i))
print(type(f))

## 3. Defining a Class ##

class MyClass():
    pass

mc_1 = MyClass()
mc_2 = MyClass()

print(type(mc_1))

## 5. Creating Methods ##

class MyClass():
    def add_two_numbers(self,a,b):
        return a+b
    
mc = MyClass()
answer = mc.add_two_numbers(3,4)

## 8. Attributes and the Init Method ##

class SuperList():
    def __init__(self, argument = []):
        self.data = argument

my_list = SuperList([1, 2, 3, 4, 5])
print(type(my_list))
print(my_list.data)

## 9. Creating an Append Method ##

class SuperList():
    def __init__(self, initial_state=[]):
        self._data = initial_state

    def __repr__(self):
        string_representation = str(self._data)
        return string_representation

    def __eq__(self, other):
        is_equal = self.__dict__ == other.__dict__
        return is_equal

    def append(self, string):
        self._data += [string]
        
    def reverse(self):
        self._data = self._data[::-1]

my_list = SuperList([1, 2, 3, 4, 5])
print(my_list)

my_list.append(6)
print(my_list)

my_list.reverse()
print(my_list)

## 10. Creating and Updating an Attribute ##

class SuperList():
    def __init__(self, initial_state=[]):
        self._data = initial_state
        self._calc_length()

    def __repr__(self):
        string_representation = str(self._data)
        return string_representation

    def __eq__(self, other):
        is_equal = self.__dict__ == other.__dict__
        return is_equal

    def append(self, new_item):
        self._data = self._data + [new_item]
        self._calc_length()

    def reverse(self):
        self._data = self._data[::-1]
        self._calc_length()

    def _calc_length(self):
        length = 0
        for item in self._data:
            length += 1
        self.length = length

fibonacci = SuperList([1, 1, 2, 3, 5])
print(fibonacci.length)

fibonacci.append(8)
print(fibonacci.length)