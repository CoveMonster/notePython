# 操作系统的作用

# 1、并发 多个程序同时运行
#
import time, os
from multiprocessing import Process


def fun(args, args1):
    # for i in range(0,5):
    #     print('thread 0 :', i,'\n')
    time.sleep(1)
    print(args, args1)


def fun_1():
    for i in range(0,5):
        print('thread 1 :', i, '\n')

def func(arg1, arg2):
    print(arg1)
    time.sleep(5)
    print(arg2)

if __name__ == '__main__':
    # p_0 = Process(target=fun, args=('args1', 'args2'))
    # #p_1 = Process(target=fun_1)
    # p_0.start()
    # #p_1.start()
    # print('main', os.getpid())
    # print('main father', os.getppid())


    # join 方法
    # p = Process(target=func, args=(10, 20))
    # p.start()
    # p.join()
    # print('main')

    # 开启多个子进程
    for i in range(10):
        p = Process(target=func, args=(10, 20))
        p.start()
