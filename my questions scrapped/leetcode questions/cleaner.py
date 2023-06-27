import re  # Required for pattern matching
arr = [ ]   # Array to store the lines of the file

# open the file
with open("X:\Web development hackatthon Algozenith\leetcode questions\lc.txt","r") as file:
    #reaad each line one by one
    for line in file:
        #process the line
        arr.append(line)  # You can perform any operation on the line here
        
        
def remove_elements_with_pattern(array, pattern):
    new_array =[]
    for element in array:
        if pattern not in element:
            new_array.append(element)
        else:
            print("Removed:" + element)
    
    return new_array

arr= remove_elements_with_pattern(arr, "/solution")
print(len(arr))
arr = list(set(arr))

with open('X:\Web development hackatthon Algozenith\leetcode questions\lc_problems.txt','a')as f:
    # iterate over each link in your final list
    for j in arr:
        # write each link to the file, followed by a newline
        f.write(j)
        
        
        

    