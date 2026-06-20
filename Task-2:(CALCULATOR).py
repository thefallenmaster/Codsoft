while True:
    print("\tCALCULATOR\t")
    a=int(input("Enter Number 1:"))
    b=int(input("Enter Number 2:"))
    print("\tMenu\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
    menu=int(input("Enter Choice:"))
    if menu == 1:
        print('Answer:',a+b)
    elif menu == 2:
        print('Answer:', a-b)
    elif menu == 3:
        print('Answer:', a*b)
    elif menu == 4:
        print('Answer:', a/b)
    elif menu == 5:
        exit()
    else:
        print("Invalid Choice!")