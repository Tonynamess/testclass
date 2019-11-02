# -*- coding: utf-8 -*-
# author:   time:

def reverse(string):
    return string[::-1]

def test_reverse():
    string = "good"
    assert reverse(string) == "doog"

    another_string = "itest"
    assert reverse(another_string) == "tseti"
# 上面的代码做了2件事
# 定义了名为reverse(string)的全局函数，作用是把string反转并返回。比如输入"abc"会反转成"cba"
# 定义了名为test_reverse()的函数，包含了2个断言，用来测试reverse()方法的正确性
# 在该文件所在路径中输入cmd,在命令行中使用下面的命令去运行用例
# pytest
