def summation():
    list1 = []
    list2 = []
    updated_list = []
    
    n = int(input())
    
    print()
    for i in range(n):
        l = int(input())
        list1.append(l)
    
    print()
    for y in range(n):
        m = int(input())
        list2.append(m)
    
    for z in range(n):
        updated_list.append(list1[z] + list2[z])
    
    return updated_list

def find_min_max(updated_list):
    min_value = updated_list[0]
    max_value = updated_list[0] 
    
    for num in updated_list:
        if num < min_value:
            min_value = num 
        if num > max_value:
            max_value = num  
    return min_value, max_value

updated_list = summation()
print(updated_list)

min_value, max_value = find_min_max(updated_list)
print((min_value, max_value))# YOUR CODE HERE
