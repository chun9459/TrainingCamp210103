# 要求一：函式與流程控制
# 在函式中 使用迴圈 計算最小值到最大值之間，所有整數的總和。
def calculate(min, max):
    sum = 0
    for i in range(min,max+1):
        sum = sum + i
    print(sum)
calculate(1, 3) 
calculate(4, 8)



# 要求二：Python 字典與列表
# 正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
def avg(data):
    data_employees = data["employees"] 
    # data_employees=[{"name":"John","salary":30000},{"name":"Bob","salary":60000},{"name":"Jenny","salary":50000}]
    dict = {}
    n = 0
    sum = 0
    for i in range(len(data_employees)):
        dict[i] = data_employees[i]
        # dict={0:{'name':'John','salary':30000}, 1:{'name':'Bob','salary':60000}, 2:{'name':'Jenny','salary':50000}}
    for j in range(len(dict)):
        n = dict[j]["salary"]
        sum = sum + n
    print(sum / len(dict))     
avg({"count":3,
     "employees":[{"name":"John",  "salary":30000},
                  {"name":"Bob",   "salary":60000},
                  {"name":"Jenny", "salary":50000}]
    })



# 要求三：演算法
# 找出至少包含兩筆整數的列表 (Python) 中，兩兩數字相乘後的最大值。
def maxProduct(nums):
    if nums[0] >= nums[1]:
        n1 = nums[0]
        n2 = nums[1]
    else:
        n1 = nums[1]
        n2 = nums[0]
    for i in range(2,len(nums)):
        if n2 >= nums[i]:
            continue
        elif n1 < nums[i] and n2 < nums[i] and i < len(nums):
            n2 = n1
            n1 = nums[i]
        elif n1 > nums[i] and n2 < nums[i] and i < len(nums):
            n2 = nums[i]
            continue
    else:
        a = n1 * n2
    
    if nums[0] <= nums[1]:
        n3 = nums[0]
        n4 = nums[1]
    else:
        n3 = nums[1]
        n4 = nums[0]
    for j in range(2,len(nums)):
        if n4 <= nums[j]:
            continue
        elif n3 > nums[j] and n4 > nums[j] and j < len(nums):
            n4 = n3
            n3 = nums[j]
        elif n3 < nums[j] and n4 > nums[j] and j < len(nums):
            n4 = nums[j]
            continue
    else:
        b = n3 * n4
    
    if a > b:
        print(a)
    else:
        print(b)
    # List = sorted(nums)
    # a = List[0] * List[1]
    # b = List[-1] * List[-2]
    # if a > b:
    #   print(a)
    # else:
    #   print(b)   *另一種寫法。
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-10, -20, 1, 2])



# 要求四 ( 請閱讀英文 )：演算法
# Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if ( nums[i] + nums[j] ) == target:
                return [i, j]
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9



# 要求五 ( Optional )：演算法
# 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。
def maxZeros(nums):
    n = 0
    L = []
    for i in range(len(nums)):
        if nums[i] == 0 :
            n = n + 1
            continue
        else:
            L.append(n)
            n = 0
            continue
    else:
        L.append(n)
        print(max(L))
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
