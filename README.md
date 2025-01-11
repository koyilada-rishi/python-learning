# python-learning

Here is a list of important and commonly used built-in functions in Python, categorized for daily use:

1. Input and Output
print(): Prints output to the console.
input(): Reads input from the user.
2. Data Type Conversion
int(): Converts a value to an integer.
float(): Converts a value to a floating-point number.
str(): Converts a value to a string.
bool(): Converts a value to a boolean.
list(): Converts a value to a list.
tuple(): Converts a value to a tuple.
set(): Converts a value to a set.
dict(): Converts a value to a dictionary.
3. Iteration and Functional Programming
range(): Generates a sequence of numbers.
len(): Returns the length of an object.
enumerate(): Adds an index to an iterable.
zip(): Combines multiple iterables element-wise.
map(): Applies a function to every item in an iterable.
filter(): Filters elements of an iterable based on a condition.
sorted(): Returns a sorted list.
reversed(): Returns a reversed iterator.
4. Math and Numbers
abs(): Returns the absolute value of a number.
round(): Rounds a number to a given number of decimal places.
pow(): Returns the result of raising a number to a power.
sum(): Returns the sum of all elements in an iterable.
min(): Returns the smallest item in an iterable or among arguments.
max(): Returns the largest item in an iterable or among arguments.
divmod(): Returns the quotient and remainder as a tuple.
5. String Operations
len(): Returns the length of a string.
chr(): Converts a Unicode code to a character.
ord(): Converts a character to its Unicode code.
str(): Converts a value to a string.
6. File Handling
open(): Opens a file for reading, writing, or appending.
read() / write(): Reads from or writes to a file.
close(): Closes an open file.
7. Type Checking
type(): Returns the type of an object.
isinstance(): Checks if an object is an instance of a class.
8. Debugging
id(): Returns the memory address of an object.
dir(): Returns a list of attributes and methods of an object.
help(): Displays help information about an object or function.
9. Miscellaneous
all(): Returns True if all elements in an iterable are true.
any(): Returns True if any element in an iterable is true.
eval(): Evaluates a Python expression (use cautiously).
exec(): Executes Python code dynamically.
hash(): Returns the hash value of an object.
zip(): Combines multiple iterables element by element.
10. Object Operations
del: Deletes an object.
sorted(): Sorts items in an iterable.
reversed(): Reverses items in an iterable.
slice(): Creates a slice object.
Daily Use Cases
len(): To get the length of strings, lists, etc.
print(): Debugging and output.
input(): User interaction.
type() / isinstance(): Checking data types.
sum() / min() / max(): Quick mathematical operations.
map() / filter() / zip(): Functional programming.
open(): Reading and writing files.
sorted(): Sorting lists or other iterables.
Would you like examples for any specific functions?







You said:
Give me all with examples 
ChatGPT said:
ChatGPT
Here’s a comprehensive list of important Python built-in functions along with examples for each.

1. Input and Output
print()
Prints output to the console.

python
Copy code
print("Hello, World!")  # Output: Hello, World!
input()
Reads input from the user.

python
Copy code
name = input("Enter your name: ")
print(f"Hello, {name}!")  # Outputs the user's name
2. Data Type Conversion
int()
Converts a value to an integer.

python
Copy code
print(int("42"))  # Output: 42
print(int(3.14))  # Output: 3
float()
Converts a value to a floating-point number.

python
Copy code
print(float("3.14"))  # Output: 3.14
str()
Converts a value to a string.

python
Copy code
print(str(123))  # Output: "123"
bool()
Converts a value to a boolean.

python
Copy code
print(bool(1))  # Output: True
print(bool(0))  # Output: False
list()
Converts a value to a list.

python
Copy code
print(list("hello"))  # Output: ['h', 'e', 'l', 'l', 'o']
tuple()
Converts a value to a tuple.

python
Copy code
print(tuple("hello"))  # Output: ('h', 'e', 'l', 'l', 'o')
set()
Converts a value to a set (unique elements only).

python
Copy code
print(set("hello"))  # Output: {'e', 'h', 'l', 'o'}
dict()
Converts a list of tuples to a dictionary.

python
Copy code
print(dict([("key1", "value1"), ("key2", "value2")]))  # Output: {'key1': 'value1', 'key2': 'value2'}
3. Iteration and Functional Programming
range()
Generates a sequence of numbers.

python
Copy code
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
len()
Returns the length of an object.

python
Copy code
print(len("hello"))  # Output: 5
enumerate()
Adds an index to an iterable.

python
Copy code
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)  # Output: 0 a, 1 b, 2 c
zip()
Combines multiple iterables element-wise.

python
Copy code
names = ["Alice", "Bob"]
ages = [25, 30]
print(list(zip(names, ages)))  # Output: [('Alice', 25), ('Bob', 30)]
map()
Applies a function to every item in an iterable.

python
Copy code
nums = [1, 2, 3]
print(list(map(lambda x: x * 2, nums)))  # Output: [2, 4, 6]
filter()
Filters elements of an iterable based on a condition.

python
Copy code
nums = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, nums)))  # Output: [2, 4]
sorted()
Returns a sorted list.

python
Copy code
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]
reversed()
Returns a reversed iterator.

python
Copy code
print(list(reversed([1, 2, 3])))  # Output: [3, 2, 1]
4. Math and Numbers
abs()
Returns the absolute value of a number.

python
Copy code
print(abs(-5))  # Output: 5
round()
Rounds a number to the nearest integer or specified decimal places.

python
Copy code
print(round(3.14159, 2))  # Output: 3.14
pow()
Returns a number raised to a power.

python
Copy code
print(pow(2, 3))  # Output: 8
sum()
Returns the sum of all elements in an iterable.

python
Copy code
print(sum([1, 2, 3]))  # Output: 6
min()
Returns the smallest item in an iterable.

python
Copy code
print(min([3, 1, 2]))  # Output: 1
max()
Returns the largest item in an iterable.

python
Copy code
print(max([3, 1, 2]))  # Output: 3
divmod()
Returns the quotient and remainder as a tuple.

python
Copy code
print(divmod(10, 3))  # Output: (3, 1)
5. String Operations
len()
Returns the length of a string.

python
Copy code
print(len("hello"))  # Output: 5
chr()
Converts a Unicode code to a character.

python
Copy code
print(chr(65))  # Output: A
ord()
Converts a character to its Unicode code.

python
Copy code
print(ord("A"))  # Output: 65
6. File Handling
open()
Opens a file for reading, writing, or appending.

python
Copy code
with open("example.txt", "w") as f:
    f.write("Hello, World!")
7. Type Checking
type()
Returns the type of an object.

python
Copy code
print(type(123))  # Output: <class 'int'>
isinstance()
Checks if an object is an instance of a class.

python
Copy code
print(isinstance(123, int))  # Output: True
8. Debugging
id()
Returns the memory address of an object.

python
Copy code
x = 123
print(id(x))
dir()
Returns a list of attributes and methods of an object.

python
Copy code
print(dir([]))  # Lists all methods for a list
help()
Displays help information about an object or function.

python
Copy code
help(len)  # Outputs documentation for the len function
9. Miscellaneous
all()
Returns True if all elements in an iterable are true.

python
Copy code
print(all([1, 2, 3]))  # Output: True
any()
Returns True if any element in an iterable is true.

python
Copy code
print(any([0, 0, 1]))  # Output: True
eval()
Evaluates a Python expression.

python
Copy code
print(eval("2 + 3"))  # Output: 5
exec()
Executes Python code dynamically.

python
Copy code
exec("x = 5; print(x)")  # Output: 5
hash()
Returns the hash value of an object.

python
Copy code
print(hash("hello"))  # Output: Hash value (an integer)
This list covers almost all daily-use Python built-in functions with examples. Let me know if you'd like more details or examples for specific functions!
