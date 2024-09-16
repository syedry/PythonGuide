#The lambda keyword is used to define anonymous functions in Python. Usually, such a function is meant for one-time use.

square = lambda x : x * x
n = square(5) 
print(n)

sum = lambda *x: x[0]+x[1]+x[2]+x[3]  
a = sum(5, 10, 15, 20)
print(a)

#For more inf -- https://www.tutorialsteacher.com/python/python-lambda-function