# _*_ coding:utf-8 _*_
# author: huhua

class Person(object):
	"""人的类"""
	def __init__(self, name):
		self.name = name
		self.gun = None # 用来保存枪对象的引用，可以用来获取枪对象方法返回的值
		self.HP = 100

	def anzhuang_zidan(self, dan_jia_temp, zi_dan_temp):
		# 子弹装到弹夹： 可以理解为：弹夹.保存子弹（子弹）
		dan_jia_temp.baocun_zidan(zi_dan_temp)  # 方法名称要保持一致

	def anzhuang_danjia(self, gun_temp, dan_jia_temp):
		# 弹夹装到枪上，可以理解为：枪.保存（弹夹）
		gun_temp.baocun_danjia(dan_jia_temp)  # 到枪的类中去添加方法和属性

	def naqiang(self, gun_temp):
		# 拿起一把枪
		self.gun = gun_temp   # 定义一个属性来保存gun_temp

	def __str__(self):
		if self.gun:
			return '%s的血量：%d，他有枪, %s'%(self.name, self.HP, self.gun)
		else:
			if self.HP > 0:
				return '%s的血量：%d，他没枪'%(self.name, self.HP)
			else:
				return '%s already dead'%self.name

	def shot(self, enemy):
		# 人开枪去打敌人，枪.开火(敌人)
		self.gun.fire(enemy)

	def lose_blood(self, power):
		self.HP -= power

class Gun(object):
	"""枪的类"""
	def __init__(self, name):
		self.name = name
		self.danjia = None

	def baocun_danjia(self, dan_jia_temp):
		"""用一个属性来保存弹夹对象的引用"""
		self.danjia = dan_jia_temp

	def __str__(self):
		if self.danjia:  # 获取枪类中属性对应的对象的方法
			return '枪的信息为:%s，%s'%(self.name, self.danjia)
		else:
			return '枪的信息为:%s，没有弹夹'%(self.name)

	def fire(self, enemy):
		# 枪发出子弹，射击敌人, 子弹.击中(敌人)，
		# 但要先从弹夹取出子弹，弹夹.tanchu()
		zi_dan = self.danjia.tanchu() # 用个变量保存这颗子弹
		# 子弹有可能是空，增加一个判断
		if zi_dan:
			zi_dan.jizhong(enemy)
		else:
			print('没有子弹了....')

class Danjia(object):
	"""弹夹类"""
	def __init__(self, contain):
		self.contain = contain   # 弹夹容量
		self.zidan_list = []     # 保存多个子弹

	def baocun_zidan(self, zi_dan_temp):
		# 将这颗子弹保存，用一个变量来指向子弹的引用
		# self.xxxx= zi_dan_temp, 这样会导致每次来一颗子弹都要调用，而且self.xx属性会指向新的引用
		# 所以要用一个空列表保存多个子弹的引用
		self.zidan_list.append(zi_dan_temp)

	def __str__(self):
		# 描述信息
		return '弹夹的信息为:%d/%d'%(len(self.zidan_list), self.contain)

	def tanchu(self):
		# 弹出一发子弹，先判断弹夹是否有子弹
		if self.zidan_list:
			return self.zidan_list.pop()
		else:
			return None


class Zidan(object):
	"""子弹类"""
	def __init__(self, power):
		self.power = power    # 每发子弹伤害

	def jizhong(self, enemy):
		# 击中效果，敌人扣血, diren.扣血(威力)
		enemy.lose_blood(self.power)

def main():
	"""主控制"""
	# 1.创建人物对象
	player = Person('华仔')
	boss = Person('怪物BOSS')
	# 2.创建枪对象
	gun = Gun('m416')
	# 3.创建弹夹对象
	dan_jia = Danjia(30)

	# 4.创建子弹
	for i in range(20):  # 持续填充子弹
		zi_dan = Zidan(5)
		# 6.装子弹，player装子弹到弹夹(子弹，弹夹),需要传两个参数，在类里面定义方法时也要传入同样数量的参数
		player.anzhuang_zidan(dan_jia, zi_dan)

	# 7.装弹夹， player.安装弹夹到枪中(枪，弹夹)
	player.anzhuang_danjia(gun, dan_jia)

	# 8.拿枪, player.拿枪（枪）
	player.naqiang(gun)
	# print(player)

	# 9.射击，player对敌人进行射击，player.射击(敌人)
	player.shot(boss)  # 开一枪
	print(boss)
	print(player)

	for i in range(1, 20):  # 子弹打完
		player.shot(boss)
	print(boss)
	print(player)



	# 测试,打印信息，使用__str__方法来描述对象信息
	# print(dan_jia)
	# print(gun)
if __name__ == '__main__':
	main()


