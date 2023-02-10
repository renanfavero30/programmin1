def dec_to_hex(dechimal_nums):
    hexa = 0
    stop = 0
    temp = int(dechimal_nums)
    while stop == 0:
        reminder = temp % 16 # Modulo - reminder transfor in hexa
        temp = (int(temp) // 16)  # Quociente - temp for continue
        if temp >0:
            if reminder > 9:
                reminder = (chr(reminder + 55)) # transform in hexa
            hexa = ("".join([str(reminder), str(hexa)]))
        else:
            if reminder > 9:
                reminder = (chr(reminder + 55)) # transform in hexa
            hexa = ("".join([str(reminder), str(hexa)]))
            hexa = hexa[:-1]
            print(hexa)
            stop = 1
    return hexa

dec_to_hex(10) #A15
dec_to_hex(1456) #5B0