import random
x=random.randint(1,1000)
#x=1
print(x)
mag1=[[0 for i in range(3)] for j in range(3)]
#mag1=[[0]*3]*3
print(mag1)


#position 
pos=random.randint(1,5)
#pos=3
print("pos=",pos)

#list
list=[]
for i in range(9):
    list.append(x+i)
print(list)
print("\n\n")
#++++++++++++++++++++++++++++++++++++++++++
mag5=[[0 for i in range(3)] for j in range(3)]
def question(x,mag5):
    for i in range(x,):
        for j in range(x):
            if (a==mag5[i][j] or b==mag5[i][j] or c==mag5[i][j]):
                mag3[i][j]=mag5[i][j]
            else:
                mag3[i][j]=0
#+++++++++++++++++++++++++++++++++++++++++++
#geting input form user function
def inpmag(x):
    for i in range(x):
        for j in range(x):
         z=int(input())
         mag4[i][j]=z
    return mag4
#++++++++++++++++++++++++++++++++++++++++++
#check q and a
def check(x):
    for i in range(x):
        for j in range(x):
            if mag2[i][j]==mag4[i][j]:
                if(i==2 and j== 2):
                    print("WOW....congratsu got it right")
                else:
                    continue
            else:
                print(i+1,"th row is incorrect")
                print("ur pattern is incorrect pls try again")
                inpmag(3)
                break
#++++++++++++++++++++++++++++++++++++++++++++++++
                
mag1[0][0]=list[1]
mag1[0][1]=list[6]
mag1[0][2]=list[5]
mag1[1][0]=list[8]
mag1[1][1]=list[4]
mag1[1][2]=list[0]
mag1[2][0]=list[3]
mag1[2][1]=list[2]
mag1[2][2]=list[7]


#transpose of m.g.s
    
mag2=[[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        mag2[j][i]=mag1[i][j]

mag3=[[0 for i in range(3)] for j in range(3)]
mag4=[[0 for i in range(3)] for j in range(3)]
#mag4=[0,0,0]
if(pos==1):
    print(mag1[0])
    print(mag1[1])
    print(mag1[2])
    print("\n\n")
    a=random.choice(mag1[0])
    b=random.choice(mag1[1])
    c=random.choice(mag1[2])
    print(a)
    print(b)
    print(c)
    print("\n\n")
    question(3,mag1)
    print(mag3[0])
    print(mag3[1])
    print(mag3[2])
    print("\n\n")
    inpmag(3)
    print("\n\n")
    print(mag4[0])
    print(mag4[1])
    print(mag4[2])
    check(3)
elif(pos==2):
    mag1.reverse()
    print(mag1[0])  
    print(mag1[1])
    print(mag1[2])
    print("\n\n")
    a=random.choice(mag1[0])
    b=random.choice(mag1[1])
    c=random.choice(mag1[2])
    print(a)
    print(b)
    print(c)
    print("\n\n")
    question(3,mag1)
    print(mag3[0])
    print(mag3[1])
    print(mag3[2])
    print("\n\n")
    inpmag(3)
    print("\n\n")
    print(mag4[0])
    print(mag4[1])
    print(mag4[2])
    check(3)
elif(pos==3):
    print(mag2[0])
    print(mag2[1])
    print(mag2[2])
    print("\n\n")
    a=random.choice(mag2[0])
    b=random.choice(mag2[1])
    c=random.choice(mag2[2])
    print(a)
    print(b)
    print(c)
    print("\n\n")
    question(3,mag2)
    print(mag3[0])
    print(mag3[1])
    print(mag3[2])
    print("\n\n")
    inpmag(3)
    print("\n\n")
    print(mag4[0])
    print(mag4[1])
    print(mag4[2])
    check(3)
    
elif(pos==4):
    mag2.reverse()
    print(mag2[0])
    print(mag2[1])
    print(mag2[2])
    print("\n\n")
    a=random.choice(mag2[0])
    b=random.choice(mag2[1])
    c=random.choice(mag2[2])
    print(a)
    print(b)
    print(c)
    print("\n\n")
    question(3,mag2)
    print(mag3[0])
    print(mag3[1])
    print(mag3[2])
    print("\n\n")
    inpmag(3)
    print("\n\n")
    print(mag4[0])
    print(mag4[1])
    print(mag4[2])
    check(3)

#print(mag1)

