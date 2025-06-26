result={}
print(result)

def add_students():
    sname=input('Enter the name of the student: ')
    smarks=int(input('Enter the marks: '))
    result[sname]=smarks

def update_marks():
    sname=input("Enter name of an existing student: ")
    smarks=int(input("Enter updated marks: "))
    result[sname]=smarks
    print(result)

def high_low_marks():
    highest_marks=max(result.values())
    print("The highest marks scored are: ", highest_marks)
    lowest_marks=min(result.values())
    print("The lowest marks scored are: ",lowest_marks)

def avg_marks():
    average_marks=sum(result.values())/len(result)
    print("The average marks scored by students are: ",average_marks)

def show():
    print(result)

print("1. Add Students\n2. Update Marks\n3. Highest and Lowest Marks\n4. Average Marks\n5. Show Records")
while(True):
    opt=int(input("Enter your choice: "))
    if opt==1:
        add_students()
    elif opt==2:
        update_marks()
    elif opt==3:
        high_low_marks()
    elif opt==4:
        avg_marks()
    elif opt==5:
        print("The final records are:")
        show()
        break
    else:
        print("Invalid!")