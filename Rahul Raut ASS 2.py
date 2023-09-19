#Name = Rahul Raut
#Date = 


# ----------- ASSIGNMENT 2 DSL PYTHON ------------

'''

Write a Python program to store marks scored in subject "Fundamental of Data Structure" by N students in the class.
Write functions to compute following:

a) The average score of the class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d)Display mark with highest frequency

'''



#Predefining the marks array
marks=[]

#Defning the STUDENT GET function;
def stud_get():
    print("--------------------------------------------")
    N = int(input("Enter No. of Students in Class= "))
    
    #globally defining the function marks;
    global marks
    for i in range(N):
        print("Enter the Marks of Students (Write -1 for Absent Students)")
        M = int(input())
        marks.append(M)
    print(marks)

#Defining the function Average Marks to calculate the Average Score of the class
def avg_marks():
    print("--------------------------------------------")
    sum = 0
    cnt = 0
    for i in range(len(marks)):
        if marks[i] != -1:
            sum = sum + marks[i]
            cnt += 1
    print("Total Marks = ",sum)
    print("Average Marks = ", sum//cnt,"(", sum/cnt ,")" )

    
#Defning the function High Low (h_l) to calculate the Highest and Lowest marks
#x is temp var
def h_l():
    print("--------------------------------------------")
    #for calc Highest Marks
    x = marks[0] # x = temp var
    for i in range(len(marks)):
        if x < marks[i]:
            x = marks[i]
    print("Highest Marks = ", x)

    #for calc Lowest Marks
    x = marks[0]
    for i in range(len(marks)):
        if marks[i] != -1:
            if x > marks[i]:
                x = marks[i]
    print("Lowest Marks = ", x)

    
#Defining the count_abs for COunting the number of students absent in FDS test
def count_abs():
    print("--------------------------------------------")
    cnt = 0
    for i in range(len(marks)):
        if marks[i] == -1:
            cnt += 1
    print("Number of Students Absent in the Test = ",cnt)

    
#Defining Highest Freq function to calculate the highest frequency of the marks
def high_freq():
    print("--------------------------------------------")
    freq = []
    for i in range(len(marks)):
        if marks[i] != -1:
            freq.append(marks.count(marks[i]))
    y = max(freq)
    print("Highest Frequency= ", y)
    print("Highest Marks= ", marks[y])

    
#Giving a Menu to the whole code and creating a loop for execution
if __name__ == '__main__':
    print("------------------- Input WIndow -------------------")
    stud_get()
    while(True):
        print("1. The Average Score of Class ")
        print("2. Highest Score and Lowest Score of Class ")
        print("3. Count of Students who were Absent for the Test ")
        print("4. Display Marks with Highest frequency ")
        print("5. EXIT ")
        print("Enter Choice")
        ch = int(input())
        if(ch == 1):
            avg_marks()
            print("--------------------------------------------")
        if(ch == 2):
            h_l()
            print("--------------------------------------------")
        if(ch == 3):
            count_abs()
            print("--------------------------------------------")
        if(ch == 4):
            high_freq()
            print("--------------------------------------------")
        if(ch == 5):
            print("Thank You !!!")
            exit()
