import argparse
import time
#编写一个类似编译的源码的解析脚本 提供 make clean make  make install 等调用

parser = None


def make():
    print("start make")
    time.sleep(2)
    print("end make")

def make_install():
    print('start make install')
    time.sleep(2)
    print('end make install')

def make_clean():
    print('start make clean')
    time.sleep(2)
    print('end make clean')

parser = argparse.ArgumentParser(description= '模拟编译操作')
parser.add_argument('do',type =str,nargs = '?',help ='设置需要做的操作',
                    choices = ['install', 'clean'])

result = parser.parse_args()

#开始根据参数判定
if result.do == None:
    make()
elif result.do == 'install':
    make_install()
elif result.do == 'clean':
    make_clean()
else:
    pass



