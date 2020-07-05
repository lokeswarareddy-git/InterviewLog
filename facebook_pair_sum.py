##Finding list of pair sum in the array 

def pair_sum(list1, k):

    #Edge Case 
    if len(list1) < 2:
        print("Please enter the list whose lengh more than 1")
    seen = set()
    output = set()
    for num in list1:   #O(n)
        target = k - num 
        if target not in seen:
            seen.add(target)
        else:
            output.add((min(target, num), max(target, num)))
    print(output)


pair_sum([1,3,2,2],4)
