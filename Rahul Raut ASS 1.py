#Name = Rahul Raut
#Date = 


# ----------- ASSIGNMENT 1 DSL PYTHON ------------

'''

In second year computer engineering class, group A student's play cricket,
group B students play badminton and group C students play football.
Write a Python program using functions to compute following: -
    a) List of students who play both cricket and badminton
    b) List of students who play either cricket or badminton but not both
    c) Number of students who play neither cricket nor badminton
    d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions

'''




#Group A = group of students who play ONLY cricket
#Group B = group of students who play ONLY badminton
#Group C = group of students who play ONLY football
#Uni = group of all the students in the Uni

#predefining the lists
groupA = []
groupB = []
groupC = []
uni = []

#defining the main function
def start():
    C = int(input("Enter Number of Students who Play Cricket: "))
    
    #Global function for group A (input)
    global groupA
    print("Enter the Roll Number who play Cricket: ")
    for i in range(C):
        cri = int(input("Enter Roll Number: "))
        groupA.append(cri)
    print(groupA)
    
    #Global Function for Group B (input)
    global groupB
    B = int(input("Enter the Roll Number who play Badminton: "))
    for i in range(B):
        bad = int(input("Enter Roll Number: "))
        groupB.append(bad)
    print(groupB)
    
    #Global Function for Group C (input)
    global groupC
    F = int(input("Enter the Roll Number who play Football: "))
    for i in range(F):
        foot = int(input("Enter Roll Number: "))
        groupC.append(foot)
    print(groupC)
    
    #Global Function for input of all students
    U = int(input("Enter Number of Students in Class: "))
    global uni
    for x in range(1,U+1):
        uni.append(x)
    print(uni)

# List of students who play both cricket and badminton
def cri_bad():
    uni_cri_bad=[]
    for i in groupA:
        for j in groupB:
            if i == j:
                uni_cri_bad.append(j)
    print(uni_cri_bad)

# list of students who play either cricket or badminton but not both
def cri_bad_not_both():
    not_cri_bad = []
    for i in groupA:
        if i not in groupB:
            not_cri_bad.append(i)
    for j in groupB:
        if j not in groupA:
            not_cri_bad.append(j)
    print(not_cri_bad)

# list of students who play neither cricket nor badminton
def nei_cri_nor_bad():
    uni_cri_bad = []
    uni_cri_bad.extend(groupA)
    for j in groupB:
        if j not in groupA:
            uni_cri_bad.append(j)
    print(uni_cri_bad)
    
    #comp with uni
    not_cri_bad = []
    for i in uni:
        if i not in uni_cri_bad:
            not_cri_bad.append(i)
    print(not_cri_bad)

    
# list of students who play cricket football and not badminton
def cri_foot_not_bad():
    cri_foot = []
    cri_foot.extend(groupA)
    for i in groupC:
        if i not in groupA:
            cri_foot.append(i)
    final=[]
    for j in cri_foot:
        if j not in groupB:
            final.append(j)
    print(final)
    
    
#Creating a MENU for the user
if __name__ == '__main__':
    print("------------------ Input Window ------------------")
    start()
    while(True):
        print("1. List of Students who play both Cricket And Badminton ")
        print("2. List of Students who play either Cricket Or Badminton but Not Both ")
        print("3. List of Students who play neither Cricket nor Badminton but Not Both ")
        print("4. List of students who play Cricket And Badminton but not Badminton ")
        print("5. Exit ")
        print("Enter Choice ")
        ch=int(input())
        if(ch == 1):
            cri_bad()
        if(ch == 2):
            cri_bad_not_both()
        if(ch == 3):
            nei_cri_nor_bad()
        if(ch == 4):
            cri_foot_not_bad()
        if(ch == 5):
            print("Thank You !!")
            exit()
