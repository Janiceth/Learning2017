# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘PyTest’

# import math
# sum = 0
# x = 1
# n = 1
# while True:
#     sum = sum + x
#     # ide自带了pow（），可以不用引用 math，直接使用 x = pow(2, n)
#     x = math.pow(2, n)
#     n += 1
#     if n > 20:
#         break
# print sum

# sum = 0
# x = 0
# while True:
#     x = x + 1
#     if x > 100:
#         break
#     if x % 2 == 0:
#         continue
#     sum += x
# print sum

# # 多重循环
# for x in [ 1,2,3,4,5,6,7,8,9 ]:
#     for y in [ 0,1,2,3,4,5,6,7,8,9 ]:
#         if x < y:
#             print 10 * x + y
#
# d1 = {
#     'Adam':95,
#     'Lisa':85,
#     'Bart':59
# }
# if 'Paul' in d1:
#     print 'Paul'
# else:
#     d1['Paul'] = '75'
#
# print "Adam:", d1['Adam']
# print "Lisa:", d1.get('Lisa')
# if 'Bart' in d1:
#     print "Bart:", d1['Bart']
#
# d2 = {
#     '95':'adam',
#     '85':'lisa',
#     "59":'bart'
# }
#
# months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
# x1 = 'Feb'
# x2 = 'Sun'
#
# if x1 in months:
#     print 'x1: ok'
# else:
#     print 'x1: error'
#
# if x2 in months:
#     print 'x2: ok'
# else:
#     print 'x2: error'

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
#    print x[0], ":", x[1]
    print ("%s:%d")%x
