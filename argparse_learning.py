#utf-8f

#argparse 命令行参数解析的作用，就是解析自行配置的参数
#在zmd中使用过程是: d:转入目标路径,再cd 打开文件文件位置,然后使用>python argparse_learning.py --help 查看
#使用语句 python argparse_learning.py  kelly 传参并且运行得到运行结果 : Namespace(echo='kelly')      kelly

import argparse


#第一部分,基础语法
def fondmental():
    #创建ArgumentParser() 对象
    parser = argparse.ArgumentParser()
    # 调用 add_argument 添加参数
    parser.add_argument('echo')
    #使用  parse_args 解析函数
    args = parser.parse_args()

    #打印出最终的参数空间属性
    print(args)
    # 报错，py: error: the following arguments are required: echo， 需要在cmd终端，用python调用并传入参数即可解决（就是说需要的参数，不是在IDE里输入的，而是在cmd里输入的）
    #解决方式，在另一处文件调用的时候传入参数。
    # 打印参数空间中的变量
    print(args.echo)
    #打印针对这个添加参数模块的使用帮助说明（此处会打印出使用方法）
    # parser.print_help()


# fondmental()

#第二部分 不同参数的输入

#用函数封装一种传参种类
def one():
    parse = argparse.ArgumentParser()
    parse.add_argument('A',type=int,help = " I am A")
    parse.add_argument('B', type=int,help = " I am B")
    parse.add_argument('name')
    #可选参数
    parse.add_argument('--C',help = 'random')
    #简化可选参数输入过程
    parse.add_argument('-d','--D', help='random')



    args = parse.parse_args()
    parse.description = 'kelly ,this is test'

    print(args)

    print(args.A*args.B, args.name)

    parse.print_help()

    if args.C:
        print('this is an optinal argument')
    if args.D:
        print('this is an optinal argument,and print samplely')

#2019-12-29 第二次学习
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-square', required = False,
                        default = 2,
                        help = 'echo the string you are here',
                        type = int)
    args = parser.parse_args()

    print(args.square)
if __name__ == '__main__':
    main()