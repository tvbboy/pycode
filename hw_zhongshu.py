nums = [3, 'x', 0, 0,0,0,0, 0, 6,0,0,0, 2, 0,0,0,0 ,6, 7, 6, 0, 0, 0, 9, 'x', 5, 3, 0, 0, 2, 9, 7, 1]
for item in nums:
    #print(item,nums.count(item),len(nums))
    if(nums.count(item)>len(nums)/2):
        print(item,nums.count(item))
        break