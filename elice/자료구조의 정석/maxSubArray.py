
def maxSubArray(nums):
    sum = 0
    result = 0
    for num in nums:
        sum = max(sum + num, num)
        result = max(sum, result)
    return result

def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1])) # 30이 리턴되어야 합니다

if __name__ == "__main__":
    main()
