def max_distance(arr): 
   # same_tulple=()
    n = len(arr) 
    max_d = -1
    for i in range(n - 1): 
        for j in range(i + 1, n): 
            if arr[i] == arr[j]: 
                temp = abs(j - i) 
                max_d = max(max_d, temp) 
               # same_tulple=(arr[i],arr[j])
    return max_d
  
# Driver code 
arr = [1, 2, 4, 1, 3, 4, 2, 5, 6, 5] 
print("Maximum distance between two occurrences of same element in array:", max_distance(arr)) 



# Python program to find maximum distance between two 
# same occurrences of a number. 
  
# Function to find maximum distance between equal elements 
def maxDistance(arr, n): 
      
    # Used to store element to first index mapping 
    mp = {} 
  
    # Traverse elements and find maximum distance between 
    # same occurrences with the help of map. 
    maxDict = 0
    for i in range(n): 
  
        # If this is first occurrence of element, insert its 
        # index in map 
        if arr[i] not in mp.keys(): 
            mp[arr[i]] = i 
  
        # Else update max distance 
        else: 
            maxDict = max(maxDict, i-mp[arr[i]]) 
  
    return maxDict 
  
# Driver Program 
if __name__=='__main__': 
    arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2] 
    n = len(arr) 
    print (maxDistance(arr, n)) 
          
# Contributed By: Harshit Sidhwa 