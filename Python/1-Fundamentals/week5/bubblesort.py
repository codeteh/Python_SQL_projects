unsorted_list = [101, 49, 3, 12, 56]

def bubblesort(the_list):
    high_idx = len(the_list) - 1
    # create two loops using nesting and the iteration variables i and j
    for i in range(high_idx):
        list_changed = False
        for j in range(high_idx):
            # inside the inner loop body retrieve the values for an adjacent pair
            item = the_list[j]
            next = the_list[j+1]
            # check if vlaue in item is bigger than the value in next. if so they are out of order so their values must be switched
            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                list_changed = True
                # print the value of the_list, i and j at the end of each inner loop iteration
            print(the_list, i, j)
        print(list_changed)
        if list_changed == False:
            break
# outside of bubblesort() call bubblesort function with the unsorted list
bubblesort(unsorted_list)
