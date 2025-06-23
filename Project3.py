#Age Checker
name=input('Enter your name: ')
age=int(input('Enter your age: '))
if age>=18:
    print(f'{name} is legal for driving.')
    print(f'{name} is legal for voting.')
else:
    res=18-age
    print(f'Wait for {res} year(s)')