import random
scores = [0, 0]  # User,Computer
#{0:'Rock',1:'Paper',2:'Scissors'}
def result(user):
    global scores
    if user <0 or user>2:
        print("Invalid Choice")
        return
    cresult=random.randint(0, 2)
    if cresult==user:
        print("Draw!")
    elif (user==2 and cresult==0) or (cresult==1 and user==0) or(user==1 and cresult==2):
        print("Computer Win!")
        scores[1]+=1
    else:
        print("You Win!")
        scores[0]+=1
while True:
    r=0
    for i in range(3):
        print("Round:",r)
        print("User Score:",scores[0],"\tComputer Score:",scores[1])
        result(user=int(input("\tMenu\t\n1.Rock\n2.Paper\n3.Scissors\nEnter Your Choice:"))-1)

    round=input("Enter Your Choice [Yes/No]:")
    if round.lower()=="yes":
        r+=1
    else:
        break