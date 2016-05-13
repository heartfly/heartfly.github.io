Title: Python实现异或(xor)加密算法
Date: 2014-9-12 12:06
Category: 编程
tags: Python, xor, 加密, 算法
Slug: xor
Author: qxh
Summary: Python实现异或(xor)加密算法

    #encoding=UTF-8
    from random import seed,randint
    from binascii import *
    import base64

    str_in=input('请输入一个字符串：')
    you_seed=input('请输入密码：')
    print str_in, you_seed

    #lock
    def my_lock(lock_str,lock_seed):
        seed(lock_seed)
        li_out=[]
        for i in lock_str:
            a = randint(0,65535)
            li_out.append(unichr(ord(i)^a))
        return ''.join(li_out)
    my_lock_str=my_lock(str_in,you_seed)
    print '原字符串：',str_in
    print '加密字符串：',my_lock_str
    print '还原后字符串：',my_lock(my_lock_str,you_seed)

