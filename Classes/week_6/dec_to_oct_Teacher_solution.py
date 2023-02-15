def dec_to_octal(decimal):
    res = "" # Starts with empty strings
    while decimal > 0:
        reminder = decimal % 8
        decimal //= 8
        res = str(reminder) + res

    return res



if __name__ == "__main__":
    # main logic 73 -> "111"
    decimal = int(input())
    print(dec_to_octal(decimal))