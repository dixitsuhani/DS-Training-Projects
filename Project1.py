#Grade Calculator
name=input('Enter the name of the student: ')
roll_no=int(input('Enter the exam roll number of the student: '))
sub1=int(input('Enter the marks for subject 1: '))
sub2=int(input('Enter the marks for subject 2: '))
sub3=int(input('Enter the marks for subject 3: '))
sub4=int(input('Enter the marks for subject 4: '))
sub5=int(input('Enter the marks for subject 5: '))
print('\t\tReport')
print('Name: ',name)
print('Exam Roll Number: ',roll_no)
total_marks=sub1+sub2+sub3+sub4+sub5
print('Total marks (Out of 500): ',total_marks)
percentage=(total_marks/500)*100
print(f"{percentage}%")
if 75<=percentage<=100:
    print('A')
elif 50<=percentage<75:
    print('B')
else:
    print('C')