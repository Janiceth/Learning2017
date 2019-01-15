# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘Hello World’


#  变量（variable）和命名
# 车辆数
cars = 100
space_in_a_car = 4.0
# 司机人数
drivers = 30
# 拼车人数
passengers = 90
# 空闲车辆数量
cars_not_driven = cars - drivers
# 工作车辆数量
cars_drivern = drivers
# 运输人数
carpool_capacity = cars_drivern*space_in_a_car
# 平均每个车拼车人数
average_passengers_per_car = passengers/cars_drivern


print "There are", cars, "cars availabe."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
