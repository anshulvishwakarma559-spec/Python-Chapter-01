#Variables & memory concept

'''Variable = variable is a container to name that stores a value in memory 
 - In python ,variables are used to store data that can be referenced and manipulated during program execution.
 - Example:
     x = 10
     y = "hello"
 - Python automatically decide the data type
 - Variables are references(lables) pointing to memory object. 
 - Use id(x) to check memory location for example: '''

x = 10
y = 20
print("actual value of x is: ",x)
print("actual value of y is: ",y)
print("memory id of your variable x is: ",id(x))
print("memory id of your variable y is: ",id(y))
print("sum of actual value of x and y is: ",x+y)
x = 22
print("changed value of x is: ",x)
sum = x+y
print("sum of chenged value of x and actual value of y is: ",sum)

#variable ki value ko hm kabhi bhi change kr sakte h pr variable ki actual value ko hm change nhi kr sakte

#variable: 

'''We can create a new python variable by assingning a value to a label, using the = assignment operator.
 -- A variable name can be composed by characters, numbers, the _ underscore character. It can't start with a number. these are all valid variable name:
  - name1
  - AGE
  - aGE
  - a111
  - my_name
  - _name
 -- These are invalid variable names: 
  - 123
  - test!
  - name%
  - age$
-- Other than that, anythingid s valid unless it's a Python keyword. There are some keywords like: for, if, while, import, else, def and more. it is a part of python programming language
 '''