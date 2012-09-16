#!/usr/bin/env python
# -- coding: utf-8 --

#动物是物体
class Animal(object):
	pass

#狗属于动物
class Dog(Animal):
	def __init__(self, name):
		self.name = name

#猫也属于动物
class Cat(Animal):
	def __init__(self, name):
		self.name = name

#人是物体的一种
class Person(object):
	def __init__(self, name):
		self.name = name
		#人有一个宠物
		self.pet =  None
#有一种人叫做雇员
class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary

#鱼也属于物体
class Fish(object):
	pass

class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

#rover是一只狗
rover = Dog("Rover")

#satan是一只猫
satan = Cat("Satan")

#Mary是一个人
mary = Person("Mary")

#satan是mary的
mary.pet = satan

#frank有120000的年薪
frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
