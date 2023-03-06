def consecutive_fours (arr): #similar to count_runs
    # [3,3,3,2,4,4]
    #runs = 1
    count = 1 # how may times the current appears
    current =arr[0]
    for num in arr[1:]: # num =3
        if current == num:
            count += 1
        else:
            current = num # current = 2
            count = 1 # restart the count
            #runs increment runs by 1
        if count >= 4:
            # if  count >15 so break into a new run
            return True
    return False


def sum_by_parity ():
    for idx, num in enumerate(arr):
        if idx % 2 == 0:
            sum_even += num
        else:
            num_odd += num
    return[sum_even, sum_odd] # get decode length junt even sum

def expand_by_index(arr):
    res=[]
    for idx, num in enumerate(arr):
        value = idx
        repeated_times = num
        for i in range(repeated_times):
            res.append(value)
        #res.extend([value] * repeated_times) # [0] *2 = [0, 0]
def decode_rle(arr):
    res=[]
    for idx in enumerate(0, len(arr), 2):
        value = arr[idx + 1]
        repetead_time =
    pass

def numerical_count(string):
    res = 0
    for char in string:
        if char.isdigit():
            res += 1
    return res

if __name__ =="__main__":
    arr = [1,2,3,4]
    for idx, num in enumerate(arr):
        print(idx, num)

