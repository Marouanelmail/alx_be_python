#!/usr/bin/python3
number = int(input("Enter the size of the pattern: "))
# for _ in range(1, number+1):
#     print(f"{number * '*'}")
# for star in range(number):
    # print(f"{'*' * number}")
    # for content in range(number):
    #     if content == number - 1:
    #         print("*")
    #     else:
    #         print("*", end="" )
counter = 0
while counter < number:
    for content in range(number):
        if content == number - 1:
            print("*")
        else:
            print("*", end="")
    counter += 1


