try:
    a = 3* 2 // 4
    b = 8/0
    print(a+2)
except ZeroDivisionError as e:
    print("zero div error")
except Exception as e:
    print("something wrong")