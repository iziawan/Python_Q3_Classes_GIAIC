# Operators



# Arithmetic Operators



a = 10
b = 2

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b)  # Floor Division
print(a ** b) # a^b
print(a % b) # Remainder



# Relational or Comparision Operators => gives answer in True or False




a = 50
b = 20

print(a == b)  # a is equal to b ==> False
print(a != b)  # a is not equal to b  ==> True
print(a < b)   # a is less than b  ==> False
print(a > b)   # a is greater than b  ==> True
print(a <= b)  # a is less than or equal b  ==> False
print(a >= b)  # a is greater than or equal to b  ==> True



# Assignment Operators



a, b = 10, 20

a += 10
print(a)  # 20

a -= b
print(a)  # 0

b *= 2
print(b)  # 40

b //= b
print(b)  # 1

b /= b
print(b)  # 1.0

a %= 2
print(a) # 0

a **= b  
print(a) # 0.0




# Logical Operators




# And Operator
age = 18
isEligible = age >= 18 and age < 50

print(isEligible) #True

# OR Operator
age = 17
height = 5.5

isEligible = age >= 18 or height >= 5.5

print(isEligible) # True


# Not Operator
print(not False)  #True
print(not (True)) #False
f = 50
h = 3
print(not(h < f)) #False

isElie = ""
print(not isElie)

a = "abcd"
print("abc" not in a)
print("abc" in a)          # in function is used to find something in collection!