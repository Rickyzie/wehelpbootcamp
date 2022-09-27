print("Assignment 1")
def calculate(min, max, step):
    ans=0
    for i in range(min, max+step, step):
        if i <= max:
            ans+=i
    print(ans)
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0
print(" ")

print("Assignment 2")
def avg(data):
    total = 0
    counter = 0
    for i in data["employees"]:
        if i["manager"] == False:
            counter+=1
            total+=i["salary"]
    print(total / counter)  

avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
}) # 呼叫 avg 函式
print(" ")

print("Assignment 3")
def func(a):
    return lambda b, c: print(a + b*c) 

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果
print(" ")

print("Assignment 4")
def maxProduct(nums):
    result = []
    for i_index, i in enumerate(nums):
        for j_index, j in enumerate(nums):
            if i_index == j_index:
                break
            result.append(i * j)
    print(max(result)) 

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10
print(" ")

print("Assignment 5")
def twoSum(nums, target):
    newNums = list(map(lambda x: x-target, nums))
    result = []
    for i_index, i in enumerate(newNums):
        for j_index, j in enumerate(nums):
            if i + j ==0 and i_index != j_index:
                result.append(i_index)
                result.append(j_index)
                return result

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
print(" ")

print("Assignment 6")
def maxZeros(nums):
    array = []
    counter = 0
    for i in nums:
        array.append(0)
        if i == 0:
            array[counter]+=1
        else : 
            counter+=1
    print(max(array))
    return max(array)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
print(" ")