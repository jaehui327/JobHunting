def twoSum(nums, target):
    nums.sort()
    i = 0
    j = len(nums) - 1
    
    while i < j:
        sum = nums[i] + nums[j]
        
        if sum == target:
            return nums[i], nums[j]
        elif sum < target:
            i += 1
        else:
            j -= 1

def main():
    print(twoSum([2, 8, 19, 37, 4, 5], 12)) # (4, 8) 혹은 (8, 4)가 리턴되어야 합니다.

if __name__ == "__main__":
    main()

