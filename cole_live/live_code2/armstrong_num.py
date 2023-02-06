
i,j = input().split(" ")
i = int(i)
j = int(j)

for test in range(i,j,1):

    num = int(test)
    # Convert number from int to str
    order = len(str(num))
    order = int(order)

    # Step 2: using // and %
    #371 // 10 = 37     371%10 = 1
    #37// 10 = 3        37 % 10 = 7
    #3 // 10 = 0        3% 10 = 3

    temp = number
    total = 0
    while tem!=0
        last_digit = temp % 10
        temp //= 10
        total += last_digit ** numb_of_digits

    if total == number:
        print(number)

    first_digit = num // 1000
    second_digit = num // 100 % 10
    thirth_digit = num // 10 % 10 % 10
    fourth_digit = num % 10

    #print(first_digit)
    #print(second_digit)
    #print(thirth_digit)
    #print(fourth_digit)


    tot = first_digit ** order + second_digit** order + thirth_digit **order + fourth_digit**order
    #print(order)
    #print(f"Tot = {tot}")
    if test == tot:
        print(test)
