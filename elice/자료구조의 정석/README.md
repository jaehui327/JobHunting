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
        pass
        # 4. 객체의 데이터로 다른 객체를 사용 할 수도 있습니다. 
        # Car 객체는 Wheel 객체를 변수로 가지는데요, 
        # 여기에는 새 바퀴의 색상을 입력받고(newWheelType), 이를 바탕으로 새로운 Wheel 객체를 만들어서
        # 자동차의 wheel 데이터에 할당 하는 함수를 적어 봅시다.
        wheel = Wheel(newWheelType)
        self.wheel = wheel

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
