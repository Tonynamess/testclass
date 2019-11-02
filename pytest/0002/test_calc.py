# -*- coding: utf-8 -*-
# author:   time:2019-10-13
def add(x,y):
    return x + y
def test_add():
    assert add(1,0) == 1
    assert add(12,88) == 100
    assert add(10,990) == 1000

# 所有以test_开头的py文件都被当成了测试文件
# 所有测试文件中以test开头的方法被当成了测试用例执行