# _*_ coding:utf-8 _*_
# author: huhua

# 题目一
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

# 示例：
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 分析：目的：找到数组中和为目标值的两个数，并返回他们的索引；这里可以用两个for循环来遍历数组nums，让他们的和
# 等于target。代码如下：

'''
def twoSum(nums, target):
	# 定义空列表存放满足要求的两个数
	result = []
	n = len(nums)
	# 遍历第一个数
	for i in range(n):
		# 从i的后面开始，遍历第二个数
		for j in range(i+1, n):
			# 判断两数之和,如果满足条件就加入到列表中
			if nums[i] + nums[j] == target:
				result.append(i)
				result.append(j)
				return result

nums = [2, 7, 11, 15]
res = twoSum(nums,9)
print(res)
# 提交结果：超出时间限制。哈哈，用时太长了。这里用了2层for循环，时间复杂度为O(n^2)
'''
# 有没有更好的方法呢？既然要返回元素的索引值，不妨试试把元素和其索引存放到字典里试一试。
# first：通过创建字典，将nums里的值和序号对应起来
# second：创建另一个字典用来存储目标值（target-nums）的值，
# third：判断该值是否在nums内，并返回其对应索引值
def twoSum(nums, target):

	n = len(nums)
	# 创建字典一，键:列表元素；值:索引
	dict1 = {nums[i]: i for i in range(n)}
	#print(dict1)
	# 创建另一个字典，键:索引；值：target-nums的差值
	dict2 = {i: target - nums[i] for i in range(n)}
	#print(dict2)
	# 判断差值是否是目标列表中的元素，如果是返回索引值，不是则继续执行
	result = []
	for i in range(n):
		# 将字典二中的差值作为字典一中的值
		j = dict1.get(dict2.get(i))
		if (j is not None) and (j != i):
			result = [i, j]
			break
	return result

# 测试
aList = [2,3,5,7,9,10]
tar = 19
res = twoSum(aList, tar)
print(res)
print(aList[res[0]])
print(aList[res[1]])
# 这个只遍历了一次列表，时间复杂度降低为O(n)