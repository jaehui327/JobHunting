from collections import Counter

def findDuplicate(nums):
    count = Counter(nums)
    for (key, value) in count.items():
        if value == 2:
            return key

def main():
    print(findDuplicate([1, 5, 2, 4, 5, 6, 3]))

if __name__ == "__main__":
    main()
