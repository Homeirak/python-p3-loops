#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
    print('Happy New Year!')

int_list = [1, 2, 3, 4, 5]

def square_integers(int_list):
    squared_int_list = []
    for num in int_list:
        squared_int = num * num
        squared_int_list.append(squared_int)
    return squared_int_list

square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    i = 1
    while i <101:
        if (i % 3) == 0 and (i % 5) == 0:
            print('FizzBuzz')
        elif (i % 3) == 0:
            print('Fizz')
        elif (i% 5) == 0:
            print('Buzz')
        else:
            print(i)
        i += 1


# other practice-
#while loop:
# i = 0
# while i < 5:
#     print(f"Loop {i+1}!")
#     i += 1

# #for loop:
# for i in range(10):
#     print(f"Loop {i+1}!")
#     print(f"i is: {i}")

#List Comprehensions:
#we can write a for loop to handle this
# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# def convert_heights_to_inches(player_heights):
#     inch_heights = []
#     for height in player_heights:
#         inch_height = height * 7920
#         inch_heights.append(inch_height)
#     print(inch_heights) #print final list outside the loop
#     #remember its a local variable and if you want to print it, you have to do it inside the function
# #call function to execute 
# convert_heights_to_inches(player_heights)

#or we can write a list comprehension, which allows us to transform sequences of data in a single line.
# inch_heights = [height * 7920 for height in player_heights]
# print(inch_heights)

#another benefit of list comprehensions: you can easily reuse the name of your original sequence without worrying about conflicting names

# player_heights = [height * 7920 for height in player_heights]
# print(player_heights)



