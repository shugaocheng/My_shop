# from operator import add,sub
# from random import randint,choice
#
# ops = {'+':add,'-':sub}
# MAXTRIES = 2
#
# def doprob():
#     op = choice('+-')
#     nums = [randint(1,10) for i in range(2)]
#     # nums = []
#     # for i in range(2):
#     #     nums=randint(1,10)
#     nums.sort(reverse=True)
#     ans = ops[op](*nums)
#     pr = '%d %s %d = '%(nums[0],op,nums[1])
#     oops = 0
#     while True:
#         try:
#             if int(input(pr)) == ans:
#                 print('correct')
#                 break
#             if oops==MAXTRIES:
#                 print('answer\n%s%d'%(pr,ans))
#             else:
#                 print('incorrect...try again')
#                 oops += 1
#         except (KeyboardInterrupt,EOFError,ValueError):
#             print('invalid input ...try again')
#
# def main():
#     while True:
#         doprob()
#         try:
#             opt = input('Again [y]').lower()
#             if opt and opt[0] == 'n':
#                 break
#         except (KeyboardInterrupt,EOFError):
#             break
#
# if __name__ == '__main__':
#     main()

# from time import ctime,sleep
#
# def tsfunc(func):
#     def warppedDunc():
#         print(warppedDunc)
#         print(func)
#         print(warppedDunc.__name__)
#         print('[%s] %s() called' % (ctime(),func.__name__))
#         return func()
#     return warppedDunc
#
# @tsfunc
# def foo():
#     print(foo)
#     pass
#
# foo()
#
# bar = foo
# bar()
# print(foo)
# print(foo())
# print(bar)
# print(bar())
# sleep(4)
#
# for i in range(2):
#     sleep(1)
#     foo()


# def tupleVarArgs(args1,args2='defaultb',*theRest):
#     print(args1)
#     print(args2)
#     for each in theRest:
#         print(each)
#
# tupleVarArgs('abc')