val = input("Input f|a|b (fibonacci, abundant or both): ")

if val == "f" or val == "b":
    length = int(input("Input the length of the sequence: "))
    print("Fibonacci Sequence:")
    print("-------------------")



    firstnum = 0
    secondnum = 1
    nextnum = firstnum + secondnum

    print(0)
    for i in range(1,length):
        print(nextnum)
        #the fibonacci formula 
        nextnum = (firstnum) + (secondnum)
        #updateing the numbers
        firstnum = secondnum
        secondnum = nextnum
        
if val == "a" or val == "b":
    max_num = int(input("Input the max number to check: ")) 
    print("Abundant numbers:")
    print("-----------------")

    for i in range(max_num + 1): 
        total = 0 
        for x in range(1,i): 
            if i % x == 0: # if the numbers that are dvided by the input number then
                total += x 
        if total > i: # if the total is over the i then it is aboundet
            print(i)
