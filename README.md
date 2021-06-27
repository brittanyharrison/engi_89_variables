# Variables 
**Variables** are containers for storing data values.
## Creating Variables
A variables is created when you first assign a value to it.

EXAMPLE:
```python
x = 5
y = "Brittany"
print(x) # Output: 5
print(y) # Output: Brittany
```

## Casting 

Variables do not need to be declared with a particular _type_, and canc change after they have been set.

If you want to specify the data type, this can be done with **casting**.

EXAMPLE:
```python
x = str(3) # Output: '3'
y = int(3) # Output: 3
z = float(3) # Output: 3.0
```

## Get the type
You can get the type of a variable with the `type()` function. 

EXAMPLE:
```python
x = 5
y = "Brittany"
print(type(x)) # Output: <class 'int'>
print(type(y)) # Output: <class 'str'>
```

## Case Sensitive 
Variables are case-sensitive

EXAMPLE:
```python
a = 5
A = "Brittany"
# A will not overwrite a 
```

## Variable Names
Rules for Python variables:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)

EXAMPLE:
```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

## Assign Multiple Variables
Python allows you to assign values to multiple variables in one line.

```python
x, y, z = "Orange", "Banana", "Cherry "
print(x) # Output: Orange 
print(y) # Output: Banana
print(z) # output: Cherry 
```
<span style="background-color:HoneyDew">**Note**: Make sure the number of variables matches the number of values, or else you will get an error.</span>

## One value to Multiple Variables
You can assign the same value to multiple variables in one line.

```python
x = y = z = "Orange"
print(x) # Output: Orange
print(y) # Output: Orange
print(z) # Output: Orange 
```

## Global Variables
Variables that are created outside of a function are known as **global variables**. Global variables can be used by everyone, both inside the functions ad outside. 

When we create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the `global` keyword.

EXAMPLE:
```python
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) # Output: Python is fantastic

```
