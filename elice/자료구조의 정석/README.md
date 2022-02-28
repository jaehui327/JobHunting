# 두 수의 합

숫자들의 배열이 주어지고 표적 숫자가 주어졌다고 합시다. 배열에 주어진 숫자들 중 두 개의 숫자를 더하면 표적 숫자가 되는데요, 이때 어떤 두 수를 더하면 표적숫자가 되는지 찾는 문제를 풀어 봅시다.예를 들어서, [2, 8, 19, 37, 4, 5] 가 배열로 주어지고 12 가 표적으로 주어지면 8,4 를 찾아내시면 됩니다.

- 입력 배열에는 중복되는 수가 없습니다.
- 입력 배열에는 합해서 표적이 되는 어떤 두 수가 반드시 있습니다.
- 출력의 순서는 상관 없습니다. 위 예시의 경우, 8,4 와 4,8은 둘 다 정답으로 인정합니다.

수수께끼 같은 느낌도 들죠? 코드의 효율성도 채점합니다. 100점에 도전 해 보세요!
100점을 못 받더라도 걱정하지 마세요. 해당 강의를 다 듣고 나면 100점을 받을 수 있습니다.

```python
def twoSum(nums, target):
    # O(n^2)
    # for i in range(0, len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return nums[i], nums[j]

    # O(n^2)
    # for num in nums:
    #     if target - num in nums:
    #         return num, target - num

    # O(nlogn)
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

    return 0,0

def main():
    print(twoSum([2, 8, 19, 37, 4, 5], 12)) # (4, 8) 혹은 (8, 4)가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
```

### 풀이법





# 가장 큰 두 수의 차

0보다 큰 정수들의 배열이 주어졌다고 합시다. 여기서 가능한 모든 서로 다른 두 숫자의 차이를 고려 해 보고, 이중 가장 큰 차이를 반환하는 함수를 적어봅시다. 예를 들어서, [2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23] 가 입력으로 주어졌을 경우 가장 큰 차이를 내는 숫자쌍은 50-1 = 49 입니다.

- 두 수의 차에 해당하는 값을 반환하면 됩니다. 위 예시의 경우, 49를 반환합니다.
- 양의 값을 반환해야 합니다. 위 예시의 경우 -49가 아니라 49를 반환해야 합니다.
- 배열의 길이는 2보다 크거나 같다고 가정합니다.

이 문제에는 여러 종류의 풀이법이 존재합니다. 각 풀이법의 시간 복잡도를 고려하면서 여러가지 방법으로 문제를 풀어 봅시다.

```python
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
```

### 풀이법





# 자동자 객체

Python은 세상의 모든 것을 객체(object)로 바라봅니다.

이 문제에는 자동차 객체가 주어져 있는데요, 아직 불완전한 상태입니다.

객체에 변수와 함수들을 추가해서 완성 해 봅시다.

## 풀어보세요

1. 변수 color를 추가 해 봅시다.
2. 함수 speedDown을 추가 해 봅시다.
3. 함수 changeColor를 추가 해 봅시다.
4. 함수 wheelChange의 내용을 변경 해 봅시다.

```python
class Car:
    def __init__(self):
        self.speed = 0
        self.year = 2017
        self.wheel = Wheel("aluminum")
        # 1. 여기에 새로운 오브젝트 변수, color를 추가 해 주세요.
        # 색은 기본적으로 "white"로 설정되도록 해 주세요
        self.color = "white"

    def speedUp(self, addSpeed):
        self.speed += addSpeed

    # 2. 여기에 새로운 오브젝트 함수, speedDown을 추가해 주세요
    # 변화시키고 싶은 속도량을 입력 받은 후, 그만큼 속도록 감소시키는 일을 하는 함수입니다.
    def speedDown(self, subSpeed):
        self.speed -= subSpeed

    # 3. 여기에 새로운 함수, changeColor를 추가 해 봅시다.
    # 변화시키고 싶은 색을 지정하면, 그 색깔로 차를 도색하는 함수입니다.    
    def changeColor(self, newColor):
        self.color = newColor

    def wheelChange(self, newWheelType):
        # 4. 객체의 데이터로 다른 객체를 사용 할 수도 있습니다. 
        # Car 객체는 Wheel 객체를 변수로 가지는데요, 
        # 여기에는 새 바퀴의 색상을 입력받고(newWheelType), 이를 바탕으로 새로운 Wheel 객체를 만들어서
        # 자동차의 wheel 데이터에 할당 하는 함수를 적어 봅시다.
        wheel = Wheel(newWheelType)

class Wheel:
    def __init__(self, newWheelType):
        self.wheelType = newWheelType

def main():
    audi = Car()
    print("고객님의 차량은 {} 년에 출고되었습니다.".format(audi.year))
    print("현재 속도는 {} km/h 입니다.".format(audi.speed))
    audi.speedUp(200)
    print("변경된 속도는 {} km/h 입니다.".format(audi.speed))

    randomWheel = Wheel("aluminum")
    print("바닥에 {} 재질의 바퀴가 떨어져 있습니다.".format(randomWheel.wheelType))

if __name__ == "__main__":
    main()
```

### 풀이법





# 중복된 하나의 숫자 찾아내기

숫자들의 배열이 주어집니다. 이 배열은 길이 n을 가지며, 1부터 n-1까지의 숫자로 이루어져 있습니다.  
모든 숫자가 배열에 단 한번씩만 나타납니다. 그런데, 딱 하나의 수가 배열에 두 번 등장합니다.  
이 중복되는 숫자를 찾아내어 보세요.

예를 들어서, `[1, 5, 2, 4, 5, 6, 3]` 를 살펴봅시다. 배열의 길이는 7이며, 따라서 1~6까지의 숫자들이 한번씩 등장합니다. 그런데 5만 한번 더 등장했네요. 따라서 이 경우에는`5`를 찾아내면 됩니다.

```python
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
```

### 풀이법





# 가장 큰 부분합 구하기

정수들의 리스트가 입력으로 들어옵니다. 이 정수들의 리스트를 일부분만 잘라내어 모두 더했을 때의 값을 부분합이라 부릅니다. 이때 가장 큰 부분합을 구해봅시다.

예를 들어, `[-10, -7, 5, -7, 10, 5, -2, 17, -25, 1]`이 입력으로 들어왔다면 `[10, 5, -2, 17]`을 모두 더한 30이 정답이 됩니다.

※입력에는 최소 하나 이상의 양수가 존재합니다.

※이 문제에는 여러 종류의 풀이법이 존재합니다. 각 풀이법의 시간 복잡도를 고려하면서 여러가지 방법으로 문제를 풀어 봅시다.

```python
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
```

### 풀이법



### 

# 1로 만들기

어떤 수가 입력으로 들어오면 몇번의 연산을 통해 숫자를 1로 가장 빨리 만들 수 있을지 계산하는 함수를 작성해 봅시다.

할 수 있는 연산은 다음과 같으며 어느 연산을 먼저 수행하는지에 대한 순서는 없습니다.

- 3의 배수라면 3으로 나눕니다.

- 2의 배수라면 2로 나눕니다.

- 1을 뺍니다.

예를 들어 10이 입력되었다면, `10 -> 5 -> 4 -> 2 -> 1`의 4번의 과정을 거쳐 1로 만들 수 있습니다.

하지만 `10 -> 9 -> 3 -> 1`의 방법으로 3번의 과정을 거쳐 더 빠르게 1로 만들 수 있습니다.

또한 이것이 가장 빠른 방법입니다.

이와 같이 숫자가 입력되면 가장 빠르게 1로 만드는 연산의 횟수를 출력하는 프로그램을 작성해 봅시다.

## Hint

작은 수부터 차근차근 계산해 보아요. 작은 수를 계산해두면 큰 수를 계산할 때 이용할 수 있을거에요.

```python
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
```

### 풀이법
