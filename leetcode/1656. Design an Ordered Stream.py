from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.pre = 1
        self.ptr = 1
        self.last = n + 2
        self.result = [[] for i in range(n + 1)]

    def insert(self, idKey: int, value: str) -> List[str]:
        self.result[idKey] = value
        if idKey > self.ptr:
            self.pre = idKey
            return []
        elif idKey == self.ptr:
            try:
                self.ptr = self.result[idKey:].index([]) + idKey
            except:
                self.ptr = self.last
            return self.result[idKey:self.ptr]
        else:
            self.ptr = idKey
            return self.result[self.pre:idKey]

a = ["OrderedStream","insert","insert","insert","insert","insert"]
b = [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
obj = None
res = []
for i, x in enumerate(a):
    param_1 = []
    if x == "OrderedStream":
        obj = OrderedStream(b[i][0])
        res.append(None)
    elif x == "insert":
        param_1 = obj.insert(b[i][0],b[i][1])
        res.append(param_1)
print(res)
