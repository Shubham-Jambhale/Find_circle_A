def find_circle_A ( B ) :
    
    subtracted_i = []
    sum_B = sum(B)
    
    #subtracting the i+1 element
    for i in range(0, len(B)):
        if(i == len(B)-1):
            subtracted_i.append(B[i] - B[0])
            break
        else:
            subtracted_i.append(B[i] - B[i+1])
    
    if(len(B) % 3 == 1):
        return mod_three_1(B,subtracted_i,sum_B)
    else:
        return not_mod_three(B,subtracted_i,sum_B)
        
        
#if not mod 3 == 1         
def not_mod_three(B,subtracted_i,sum_B):
    end_element = 0
    increment_3 = 0
    
    while(increment_3 < len(B)):
        end_element = end_element + B[increment_3]
        increment_3 += 3
    end_element = int(end_element - (sum_B/3))
    result_list_shuffled = [0]*len(B)
    
    j = 0
    for i in range(0,len(B)):
        if(j == 0):
            result_list_shuffled[j] = end_element - subtracted_i[j]
            end_element = result_list_shuffled[j]
            j = j + 3
        elif(j >= len(B)):
            j = j % len(B)
            end_element = end_element - subtracted_i[j]
            result_list_shuffled[j] = end_element
            j = j + 3
        else:
            end_element = end_element - subtracted_i[j]
            result_list_shuffled[j] = end_element
            j = j + 3
    final_list = []
    j = 3  * (len(B)//3)
#     print(j)
    for i in range(0, len(B)):
        final_list.append(result_list_shuffled[j])
        j = j + 1
        if(j >= len(B)):
            j = 0
    
    return final_list

   
#if 3 mod 1 is 1.
def mod_three_1(B,B_subtracted,sum_B):
    result_list_shuffled = [0]*len(B)
    rest_sum = 0
    k = 1
    while(k < len(B)):
        rest_sum = rest_sum + B[k]
        k = k + 3
    last_element = int((sum_B/3) - rest_sum)
    j = 0
    for i in range(0,len(B)):
        if(j == 0):
            result_list_shuffled[j] = last_element - B_subtracted[j]
            last_element = result_list_shuffled[j]
            j = j + 3
        elif(j >= len(B)):
            j = j % len(B)
            last_element = last_element - B_subtracted[j]
            result_list_shuffled[j] = last_element
            j = j + 3
        else:
            last_element = last_element - B_subtracted[j]
            result_list_shuffled[j] = last_element
            j = j + 3
    final_list = []
    j = 3  * (len(B)//3) - 1
    for i in range(0, len(B)):
        final_list.append(result_list_shuffled[j])
        j = j + 1
        if(j >= len(B)):
            j = 0

    return final_list
    return 0

print("---Output---")
print()
print("Array for [179,129,62,144,182] is:")
output = find_circle_A([179,129,62,144,182])
print(output)
print()

print("Array for [10,6,9,12,15,18,14] is:")
output = find_circle_A([10,6,9,12,15,18,14])
print(output)
print()

print("Array for [11,6,9,12,15,18,21,16] is:")
output = find_circle_A([11,6,9,12,15,18,21,16])
print(output)
print()

print("Array for [3,3,3,3,3,3,3,3] is:")
output = find_circle_A([3,3,3,3,3,3,3,3])
print(output)
print()