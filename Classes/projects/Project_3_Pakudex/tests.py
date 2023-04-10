no_option =0
while no_option == 0:
    choice = int(input())
    print("menu")
    if choice not in range(1, 6):
        no_option = 0
    else:
        print("end")
        no_option = 1