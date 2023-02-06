
i,j = input().split(" ")
i = int(i)
j = int(j)

for test in range(i,j,1):

    num = int(test)
    order = len(str(num))
    order = int(order)

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
