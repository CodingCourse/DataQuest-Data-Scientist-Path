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

## 4. Creating Methods ##

class MyClass():
    def add_two_numbers(self,a,b):
        return a+b
    
mc = MyClass()
answer = mc.add_two_numbers(3,4)

## 5. Attributes and the 'Init' Method ##

class SuperList():
    def __init__(self, argument = []):
        self.data = argument

my_list = SuperList([1, 2, 3, 4, 5])
print(type(my_list))
print(my_list.data)

## 6. Dunder Methods ##

class SuperList():
    def __init__(self, argument = []):
        self._data = argument
    
    def __repr__(self):
        return str(self._data)
    
    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    
sl_1 = SuperList([1, 2, 3, 4, 5])
sl_2 = SuperList([1, 2, 3, 4, 5])
sl_3 = SuperList([1, 2, 3])

compare_1_2 = sl_1 == sl_2
compare_2_3 = sl_2 == sl_3

## 7. Creating Our First Methods ##

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

## 8. Creating and Updating Our First Attribute ##

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

## 9. Creating Attributes for Minimum and Maximum Values ##

class SuperList():
    def __init__(self, initial_state=[]):
        self._data = initial_state
        self._update()

    def __repr__(self):
        string_representation = str(self._data)
        return string_representation

    def __eq__(self, other):
        is_equal = self.__dict__ == other.__dict__
        return is_equal
    
    def _update(self):
        self._calc_length()
        self._calc_max()
        self._calc_min()

    def _calc_length(self):
        length = 0
        for item in self._data:
            length += 1
        self.length = length

    def append(self, new_item):
        self._data = self._data + [new_item]
        self._update()

    def reverse(self):
        self._data = self._data[::-1]
        self._update()

    def _calc_min(self):
        try:
            self.min = min(self._data)
        except:
            pass

    def _calc_max(self):
        try:
            self.max = max(self._data)
        except:
            pass


temperatures = SuperList([18, 28, 35])
print(temperatures.min,temperatures.max)

temperatures.append(-12)
print(temperatures.min,temperatures.max)

temperatures.append(42)
print(temperatures.min,temperatures.max)

## 10. Creating An Attribute That Checks for Types ##

class SuperList():
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state=[]):
        self._data = initial_state
        self._update()
      
    def __repr__(self):
        string_representation = str(self._data)
        return string_representation
  
    def __eq__(self, other):
        is_equal = self.__dict__ == other.__dict__
        return is_equal
  
    def _calc_length(self):
        """
        A helper function to calculate the .length
        attribute.
        """
        length = 0
        for item in self._data:
            length += 1
        self.length = length
  
    def _calc_max(self):
        """
        A helper function to calculate the .max
        attribute.
        """
        try:
            self.max = max(self._data)
        except:
            self.max = None
  
    def _calc_min(self):
        """
        A helper function to calculate the .min
        attribute.
        """
        try:
            self.min = min(self._data)
        except:
            self.min = None

    def _update(self):
        """
        A helper method to call other helper methods
        and update attributes when underlying
        data changes.
        """
        self._calc_length()
        self._calc_min()
        self._calc_max()
        self._calc_types()

    def append(self, new_item):
        """
        Append `new_item` to the SuperList
        """
        self._data = self._data + [new_item]
        self._update()
  
    def reverse(self):
        """
        Reverse the order of items in the SuperList
        """
        self._data = self._data[::-1]
        self._update()
        
    def _calc_types(self):
        types = []
        for item in self._data:
            item_type = type(item)
            if item_type not in types:
                types.append(item_type)
        self.types = types

multiple_types = SuperList(["one", 2, "three"])
print(multiple_types.types)

multiple_types.append(4.0)
print(multiple_types.types)


## 11. Creating an Info Method ##

class SuperList():
    def __init__(self, initial_state=[]):
        self._data = initial_state
        self._update()
      
    def __repr__(self):
        string_representation = str(self._data)
        return string_representation
  
    def __eq__(self, other):
        is_equal = self.__dict__ == other.__dict__
        return is_equal
  
    def _calc_length(self):
        length = 0
        for item in self._data:
            length += 1
        self.length = length
  
    def _calc_max(self):
        try:
            self.max = max(self._data)
        except:
            self.max = None
  
    def _calc_min(self):
        try:
            self.min = min(self._data)
        except:
            self.min = None
          
    def _calc_types(self):
        types = []
        for item in self._data:
            item_type = type(item)
            if item_type not in types:
                types.append(item_type)
        self.types = types

    def _update(self): 
        self._calc_length()
        self._calc_min()
        self._calc_max()
        self._calc_types()
  
    def append(self, new_item):
        self._data = self._data + [new_item]
        self._update()
  
    def reverse(self):
        self._data = self._data[::-1]
        self._update()

    def info(self):
        template = '''\
List Length:     {}
Max Value:       {}
Min Value:       {}
Types Contained: {}
'''.format(self.length,self.max,self.min,self.types)
        print(template)
        
a = SuperList([1, 2, 3, 4, 5])
a.info()

b = SuperList([1.3, -14, "hello"])
b.info()
