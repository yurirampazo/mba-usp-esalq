# RECURSION


# INPUT -> FUNCITON -> OUTPUT(FUNCTION ITSELF)

#  FACTORIAL OF 4: 4 * 3 * 2 * 1 = 24  

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num -1)

print('Factorial ', factorial(4))


# FIBONACCI OF 8

# SEQUENCE: 0,1,1,2,3,5,8,13

def fibonacci(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:  
    return fibonacci(num -2) + fibonacci(num -1)

print('Fibonacci', fibonacci(6))