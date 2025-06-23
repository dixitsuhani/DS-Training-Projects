#Simple Calculator
print('Welcome to Basic Calculator!!!')
a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Power')
choice=int(input('Enter the choice: '))
if choice==1:
    print(f'The addition of {a} and {b} is: ',a+b)
elif choice==2:
    print(f'The difference between {a} and {b} is: ',a-b)
elif choice==3:
    print(f'The multiplication of {a} and {b} is: ',a*b)
elif choice==4:
    print(f'{a} divided by {b} is: ',a/b)
elif choice==5:
    print(f'{a} to the power {b}: ',a**b)
else:
    print('Invalid choice!')