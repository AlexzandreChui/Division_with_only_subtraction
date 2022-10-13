# Created By: Alex Chui 
# Created On: 2022/10/12
# This code asks the user for two numbers to calculate the quotient of them.
y = 0
z = 0
m = 0

x = int(input("Enter a number: "))
divisor = int(input("Enter the divisor: "))

if (divisor == 0):
    print("Invalid")
    divisor = int(input("Renter the divisor: "))
  
if (x == 0):
    print("Quotient: 0 with a remainder of 0")
  
if (x < divisor) and (x > 0) and (divisor >0):
    print(f'Quotient: {y} with a remainder of {x}')
  
if ((x >= divisor) and (divisor > 0)):
  while x >= divisor:
      x -= divisor
      y += 1
      # print (f'Quotient: {y} with a remainder of {x}')
  print (f'Answer: ')
  print (f'Quotient: {y} with a remainder of {x}')
else:
    if abs(x) >= abs(divisor):
      # abs is short for absolute which means it uses the number itself without the sign
       z = abs(x)
       m = abs(divisor)
       while z >= m:
        z -= m
        y += 1
        # print (f'Quotient: {y} with a remainder of {z}')
      # print (f'Answer 2: ')
    if ((x < 0) and (divisor < 0)):
       print (f'Answer: ')
       print (f'Quotient: {y} with a remainder of {z}')
    else:
       if (((x < 0) and (divisor > 0)) or ((x > 0) and (divisor <0))):    
         print (f'Answer: ')
         print (f'Quotient: {-y} with a remainder of {z}')


