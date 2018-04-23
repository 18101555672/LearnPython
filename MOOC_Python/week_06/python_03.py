# 实例：基本统计值计算
# 求和
nums = [4,5,6,3,1,2,8,9]
def getSum(nums):
    s = 0
    for i in nums:
        s += i
    return s
print(getSum(nums))

# 平均值
def getAverage(nums):
    return getSum(nums)/len(nums)
print(getAverage(nums))

# 中位数
def getMid(nums):
    s_nums = sorted(nums)
    size = len(nums)
    if size % 2 ==0:
        print((s_nums[size//2-1]+s_nums[size//2])/2)
    else:
        print(s_nums[(size//2)])
getMid(nums)