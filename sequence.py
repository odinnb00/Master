
# Design an algorithm that generates the first n numbers in 
# the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_num = 0
second_num = 1
third_num = 2
next_num  = first_num + second_num + third_num 

if n >= 1:
    print(second_num)
    if n >= 2:
        print(third_num)    


for i in range(n-2):
    next_num  = first_num + second_num + third_num
    first_num = second_num
    second_num = third_num
    third_num = next_num
    print(next_num)