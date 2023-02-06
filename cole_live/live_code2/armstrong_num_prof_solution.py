
i,j = input().split(" ")
i = int(i)
j = int(j)

for number in range(i,j,1):

    number = int(number)
    # Convert number from int to str
    numb_of_digits = len(str(number))
    numb_of_digits = int(numb_of_digits)

    # Step 2: using // and %
    #371 // 10 = 37     371%10 = 1
    #37// 10 = 3        37 % 10 = 7
    #3 // 10 = 0        3% 10 = 3

    temp = number
    total = 0
    while temp!=0:
        last_digit = temp % 10
        temp //= 10
        total += last_digit ** numb_of_digits

    if total == number:
        print(number)

