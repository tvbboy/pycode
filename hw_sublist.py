# Define a list 'l1' containing numeric elements and another list 'l2' containing string elements
l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
# Print the original list 'l1'
print("Original list:")
print(l1)
print("\nOriginal list:")
print(l2)
print("Sublists of the said list:")
for i in range(0, len(l2) ):
        # Use the 'combinations' function to generate all combinations of 'my_list' of length 'i'
        # temp=[]
        # temp.append(l2[0:i])
    for j in range(i+1, len(l2)+1):
        #print(i,j)
        print(l2[i:j])



