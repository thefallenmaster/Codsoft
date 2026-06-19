tasks=[]
def add():
    tasks.append(input("Enter Task:"))

def update():
    co=int(input("Enter Number Of Task To Update:"))
    if len(tasks) >= co > 0:
        tasks[co-1]=input("Enter Task To Update:")
        print("Task Updated")
    else:
        print("Invalid Task Count")

def remove():
    co=int(input("Enter Number Of Task To Remove:"))
    if len(tasks) >= co > 0:
        tasks.pop(co-1)
        print("Tasks Removed!")
    else:
        print("Invalid Task Count")

def display():
    print("\tTasks")
    for i in range (0,len(tasks)):
        print(i+1,"."+tasks[i],sep="")

while True:
    print("\tMenu\t\n1.Add\n2.Update\n3.Remove\n4.Display\n5.Exit")
    choice=int(input("Enter Choice:"))
    if choice==1:
        add()
    elif choice==2:
        update()
    elif choice==3:
        remove()
    elif choice==4:
        display()
    elif choice==5:
        exit()
    else:
        print("Invalid Choice")
