def maxTwoDiff(nums):
    # O(nlogn)
    # nums.sort()
    # # last = len(nums) - 1
    # return nums[-1] - nums[0]
    
    # O(n)
    return max(nums) - min(nums)

def main():
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # 49가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
