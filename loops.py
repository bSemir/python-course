# Python control flows - Loops

'''
Python’s for statement iterates over the items of any sequence 
(a list or a string), in the order that they appear in the 
sequence.

The built-in Range function 'range()' comes in handy if you do need 
to iterate over a sequence of numbers. It generates arithmetic progressions:

range(start, stop, step)
start
The value of the start parameter (or 0 if the parameter was not supplied)
stop
The value of the stop parameter
step
The value of the step parameter (or 1 if the parameter was not supplied)
'''

# The basics
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Create a sample collection
users = {
    'Quinn': 'active',
    'Éléonore': 'inactive',
    'John': 'active'
}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        # add the key into the empty dict with the value status
        active_users[user] = status

# using the range function
for i in range(5):
    print(i)

# another way
for k, v in users.items():
    print(str(k) + ': ' + str(v))


# ...remember range(start, stop, step)
list(range(5, 10))  # [5,6,7,8,9]
list(range(0, 10, 3))  # [0,3,6,9]
list(range(-10, -100, -30))  # [-10, -40, -70]

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
# ispis:
# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb

# using the built-in sum function
sum(range(4))
# sum itself is looping through
