def convertTo1(num):
    count = [0] * (num + 1)
    for i in range(2, num + 1):
        count[i] = count[i - 1] + 1
        if i % 3 == 0:
            count[i] = min(count[i], count[i // 3] + 1)
        elif i % 2 == 0:
            count[i] = min(count[i], count[i // 2] + 1)
    return count[num]

def main():
    print(convertTo1(10))

if __name__ == "__main__":
    main()

