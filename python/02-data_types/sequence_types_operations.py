from collections import namedtuple

list1 = [1, 2]
print("list1 ==", list1)

list2 = [3, 4]
print("list2 ==", list2)

print("1 in list1:", 1 in list1)  # True

print("2 not in list2:", 2 not in list2)  # True

print("list1 + list2 ==", list1 + list2)  # [1, 2, 3, 4]

print("""
Concatenating immutable objects always results in a new object.
This means that building up a sequence by repeated concatenation
will have a quadratic runtime cost in the total sequence lenght.
Immutable objects: str, bytes, tuple, etc
""")

print("list1 * 3 ==", list1 * 3)

empty_list_times_3 = [[]] * 3

print("empty_list == [[]]")

print("empty_list_times_3 ==", empty_list_times_3)  # [[], [], []]

empty_list_times_3[0].append(3)

print("empty_list_times_3[0].append(3) ==",
      empty_list_times_3)  # [[3], [3], [3]]

print('Note that items are not copied, they are referenced multiple times.')

list3 = list1 + list2  # [1, 2, 3, 4]
print("list3 ==", list3)

print("list3[0] ==", list3[0])  # 1

print("Slicing a list is exclusive list3[1:3] ==", list3[1:3])  # [2, 3]

print("list3[0:4:2] ==", list3[0:4:2])  # 1, 3]

print("list3[-1] ==", list3[-1])  # 4

print("list3[50] throws a IndexError")

print("But list3[0: 50]: ", list3[0:50])  # [1, 2, 3, 4]

print("Steppint backwards: list3[-1:-4:-2]", list3[-1:-4:-2])  # [4, 2]

print("len(list3) ==", len(list3))  # 4

print("min(list3) ==", min(list3))  # 1

print("max(list3) ==", max(list3))  # 4

print("list3.index(3) ==", list3.index(3))  # 2

print("list3.count(1) ==", list3.count(1))  # 1

list1_twin = [1, 2]
print("list1_twin ==", list1_twin)

print("list1 == list1_twin:", list1 == list1_twin)  # True

list1_cousing = (1, 2)
print("list1_cousing ==", list1_cousing)

print("list1 == list1_cousing:", list1 == list1_cousing)  # False

# Mutable sequence operations:
list4 = [1, 2, 3, 4, 5]

print("list4", list4)

list4.insert(1, 0)

print("list4.insert(1, 0), list4:", list4)

list4.pop(1)

print("list4.pop(1), list4:", list4)

list4.reverse()

print("list4.reverse(), list4:", list4)

print("""Lists:
Are mutable sequencies, typically used to store collections of similar items
""")

print("""Tuples:
Are immutable sequences, typically used to store collections of different data.
Tuples are also used for cases where an immutable sequence of similar data is
needed (such as allowing storage in a set or dict instance).
""")
print("""Note that it's actually the comma which makes a tuple, not the
parentheses. The parentheses are optional except in the empty tuple case, or
when they are needed to avoid syntactic ambiguity.
""")
print("""We can also use collections.namedtuple, which is a tuple subclass used
to create tuple-like objects that have fields accessible by attribute lookup as
well as being indexable and interable.
""")

Point = namedtuple("Point", ["x", "y"])

p = Point(11, y=22)

print("p:", p)

print("p.x + p.y:", p.x + p.y)

print("p[0] + p[1]:", p[0] + p[1])

print("""Ranges:
The range type represents an immutable sequence of numbers and is commonly used
for looping a specific number of times in for loops.
""")
print("""The advantage of the range type over a regular list or tuple is that a
range object will always take the same amount of memory, no matter the size of
the range it represents as it only stores the start, stop and step values,
calculating individual items and subranges as needed
""")
