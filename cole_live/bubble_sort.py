def bubble_sort(a_list):
    # outer for loop, look at each pass, we have a total of n pass
    for i in range(0, len(a_list)):
        # inner for loop, we start at the beginning of the list
        # and compare two adjacent items, swap them
        for j in range(0, len(a_list)): # - 1 - i
            if j + 1 < len(a_list) and a_list[j] > a_list[j +1]:
                # if they are out of order, swap
                a_list[j], a_list[j +1] = a_list[j+1], a_list[j]

if __name__ == "__main__":
    size = int(input()) # length of the list
    a_list = []
    for _ in range(size):
        a_list.append(int(input()))
    bubble_sort(a_list)
    print(a_list)

