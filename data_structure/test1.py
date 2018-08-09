# _*_ coding:utf-8 _*_
# author: huhua

# 链表中的节点(Node)对象
class Node(object):
	"""节点的类"""
	def __init__(self, elem):
		# 初始化属性，一个节点有2个属性，元素区(与外部交互)和链接区，elem和next
		self.elem = elem  # 实际数据
		self.next = None  # 下一节点的标识

class SingleLinkList(object):
	"""
	定义一个单链表的类，用来连接各个节点，实现对链表的各种操作
	"""
	def __init__(self, node=None):
		# 链表的头节点, 开始默认为空链表
		self.__head = node

	def is_empty(self):
		"""判断链表是否为空"""
		# 如果头节点_head指向空，则为空,返回True
		return self.__head== None

	def length(self):
		"""返回链表长度"""
		# 这样需要遍历链表;这样需要增加一个属性:指针来辅助完成遍历工作
		# 定义指针cur来移动访问各个节点,可以用循环开完成,初始值指向头节点
		cur = self.__head
		count = 0     # count用来记录节点数量，
		# 循环条件，当cur不指向None时,就后移。如果为空链表,count=0,也符合要求
		while cur != None:
			count += 1
			cur = cur.next # 后移
		return count

	def travel(self):
		"""遍历整个链表"""
		# 使用while循环，每次cur指向一个节点，打印节点数据elem
		cur = self.__head
		while cur != None:
			print(cur.elem, end=',')
			cur = cur.next
		print('') #换行

	def add(self, item):
		"""链表头部添加元素"""
		# 新节点的next要指向__head指向的那个节点，head再指向新节点的elem区
		# 当链表为空时，也满足要求
		node = Node(item)
		node.next = self.__head
		self.__head = node


	def append(self, item):
		"""链表尾部添加元素"""
		# 将新节点放到链表尾部，由于用户输入的只有数据，这里先要将数据构造为节点对象
		node = Node(item)  # 新节点对象
		# 先找到尾部节点，然后把尾部节点的next区指向新节点的elem区，这样就完成增加了
		# 特殊情况，如果为空链表，cur为空，没有next
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next # 找到尾部节点
			cur.next = node


	def insert(self, pos, item):
		"""指定位置添加元素"""
		# 执行插入操作时，要先找到指定位置的前一个节点，
		# 定义一个指针pre来完成指向操作
		# 新节点next指向pre后面节点的elem，pre的next指向新节点的elem

		# 情况1，pos<=0,我们当作头部插入
		if pos <= 0:
			self.add(item)

		# 情况2，pos比链表长度值还大，则认为尾部插入
		elif pos > (self.length()-1):
			self.append(item)

		else:
			pre = self.__head
			count = 0
			# 先找到插入位置前一个位置：pos-1
			while count < (pos - 1):
				count += 1
				pre = pre.next
				# 循环退出后，pre指向pos前一个位置
			node = Node(item)
			node.next = pre.next
			pre.next = node

	def remove(self, item):
		"""删除节点"""
		# 先用指针pre定位到要删除的元素的当前位置的前一个位置，
		# 再定义一个指针cur指向元素的当前位置
		# 判断当前元素是否与删除元素是否一样，若是，则pre的next指向cur的next
		cur = self.__head
		pre = None
		while cur != None:
			if cur.elem == item: #找到元素
				# 若删除的节点为第一个节点元素
				if cur == self.__head:
					self.__head = cur.next
				else:
					#将删除位置前一个节点的next指向删除位置的后一个节点
					pre.next = cur.next
				break # 删除后退出
			else:
				# 没有找到节点，继续
				pre = cur
				cur = cur.next


	def search(self, item):
		"""查找节点是否存在"""
		# 需要遍历链表，然后判断查找的数据与当前指针cur所指数据相等
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next #后移继续比较
		return False # 遍历完仍然没有则返回False


if __name__ == '__main__':

	# 创建链表对象
	link_list1 = SingleLinkList()

	# print(link_list1.is_empty())
	# print(link_list1.length())
	#测试
	link_list1.append(1)
	link_list1.append(2)
	link_list1.append(3)
	# link_list1.add(100)
	link_list1.travel()     #out: 1,2,3,
	# 测试
	link_list1.insert(0, 9)
	link_list1.insert(2,99)
	link_list1.insert(10, 999)
	link_list1.travel()    #out: 9,1,99,2,3,999,

	link_list1.remove(99)
	link_list1.travel()    #out: 9,1,2,3,999,
	link_list1.remove(9)
	link_list1.travel()    #out: 1,2,3,999,
	link_list1.remove(999)
	link_list1.travel()    #out: 1,2,3,







