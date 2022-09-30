#编写对应题目的批改程序，作为函数整合到此文件中
#部分题目代码写对给分，结果判定正确也给分，所以可能存在超过100分的情况
#请注意查看程序结果提示


import os
from glob import glob
from subprocess import Popen as popen,PIPE as pipe,STDOUT as stdout


    
            
####===============================================================######
        
def p1():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 's=0' in i:
            s+=33.33
        if '1,30,2)' in i:
            s+=33.33
        if 's=s+i' in i:
            s+=33.33

    print('得分',s,end='')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
        
    if ret[0].decode('gb2312').replace("\n","")[:-1]=='1～29所有奇数的和为 225':
        print('结果验证通过')
    else:
        print('输出结果有误')
        
        
    
def p2():
    s=0 
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 's=0' in i:
            s+=33.33
        if '2,31,2)' in i:
            s+=33.33
        if 's=s+i' in i:
            s+=33.33
    if s<90:
        error_inf.append(filename)
    print('步骤得分',s,end=' ')


    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)


    if ret[0].decode('gb2312').replace("\n","")[-4:]=='240\r':
        print('结果验证通过')
    else:
        print('输出结果有误')


def p3():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 's=0' in i:
            s+=33.33
        if '(3,31,3)' in i:
            s+=33.33
        if 's=s+i' in i:
            s+=33.33
    print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)



    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-4:]=='165\r':
        print('结果验证通过')
    else:
        print('输出结果有误')

    

    



def p4():
    s=0 
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 's=0' in i:
            s+=33.33
        if '(5,31,5)' in i:
            s+=33.33
        if 's=s+i' in i:
            s+=33.33
    print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
        
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-4:]=='105\r':
        print('结果验证通过')
    else:
        print('输出结果有误')





def p5():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 's=0' in i:
            s+=33.33
        if '(7,29,7)' in i:
            s+=33.33
        if 's=s+i' in i:
            s+=33.33
    print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-3:]=='70\r':
        print('结果验证通过')
    else:
        print('输出结果有误')



def p6():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 's=1' in i:
            s+=33.33
        if '(10,17,2)' in i:
            s+=33.33
        if 's=s*i' in i:
            s+=33.33
    print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)

    if ret[0].decode('gb2312').replace("\n","")[-6:]=='26880\r':
        print('结果验证通过')
    else:
        print('输出结果有误')
    

def p7():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 's=1' in i:
            s+=33.33
        if '(11,18,2)' in i:
            s+=33.33
        if 's=s*i' in i:
            s+=33.33
    print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-6:]=='36465\r':
        print('结果验证通过')
    else:
        print('输出结果有误')
        



def p8():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 's=1' in i:
            s+=33.33
        if '(3,16,3)' in i:
            s+=33.33
        if 's=s*i' in i:
            s+=33.33
    print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-6:]=='29160\r':
        print('结果验证通过')
    else:
        print('输出结果有误')



def p9():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 's=1' in i:
            s+=33.33
        if '(5,21,5)' in i:
            s+=33.33
        if 's=s*i' in i:
            s+=33.33
    print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-6:]=='15000\r':
        print('结果验证通过')
    else:
        print('输出结果有误')




def p10():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 's=1' in i:
            s+=33.33
        if '(7,29,7)' in i:
            s+=33.33
        if 's=s*i' in i:
            s+=33.33
    print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-6:]=='57624\r':
        print('结果验证通过')
    else:
        print('输出结果有误')

    
    

def k1():
    data=[b'5\n4',b'5\n5',b'5\n6']
    ans=['盈利', '亏本', '亏本']
    response=[]
    
    s=0
    for i in  range(0,3):
        ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(data[i])
        response.append(ret[0].decode('gb2312').replace("\n","")[-3:-1])

    for i in range(0,3):
        if ans[i]==response[i]:
            s=s+33.33
            print('测验数据',i+1,'通过',end=' ')
        else:
            print('测验数据',i+1,'失败',end=' ')

    print('得分',s)
    if s<90:
        error_inf.append(filename)

    
def k2():
    data=[b'50\n 50',b'40\n 45',b'25 \n 26']
    ans=['绩：录取\r', '继续努力\r', '继续努力\r']
    response=[]

    s=0
    for i in  range(0,3):
        
        ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(data[i])
        response.append(ret[0].decode('gb2312').replace("\n","")[-5:])

    for i in range(0,3):
        if ans[i]==response[i]:
            s=s+33.33
            print('测验数据',i+1,'通过',end=' ')
        else:
            print('测验数据',i+1,'失败',end=' ')

    print('得分',s)
    if s<90:
        error_inf.append(filename)

def k3():
    data=[b'30\n 50',b'40\n 40',b'50 \n 20']
    ans=['80\r', '80\r', '30\r']
    response=[]

    s=0
    for i in  range(0,3):
        ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(data[i])
        response.append(ret[0].decode('gb2312').replace("\n","")[-3:])

    for i in range(0,3):
        if ans[i]==response[i]:
            s=s+33.33
            print('测验数据',i+1,'通过',end=' ')
        else:
            print('测验数据',i+1,'失败',end=' ')
    
    print('得分',s)
    if s<90:
        error_inf.append(filename)



def k4():
    data=[b'3\n 50',b'10\n 10',b'2 \n 20']
    ans=['：可抽奖\r', '谢谢惠顾\r', '谢谢惠顾\r']
    response=[]

    s=0
    for i in  range(0,3):
        ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(data[i])
        response.append(ret[0].decode('gb2312').replace("\n","")[-5:])

    for i in range(0,3):
        if ans[i]==response[i]:
            s=s+33.33
            print('测验数据',i+1,'通过',end=' ')
        else:
            print('测验数据',i+1,'失败',end=' ')

    print('得分',s)
    if s<90:
        error_inf.append(filename)

def k5():
    data=[b'50\n 3',b'40\n 5',b' 60 \n 8']
    ans=['原价\r', '原价\r', '打折\r']
    response=[]

    s=0
    for i in  range(0,3):
        ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(data[i])
        response.append(ret[0].decode('gb2312').replace("\n","")[-3:])

    for i in range(0,3):
        if ans[i]==response[i]:
            s=s+33.33
            print('测验数据',i+1,'通过',end=' ')
        else:
            print('测验数据',i+1,'失败',end=' ')

    print('得分',s)

    if s<90:
        error_inf.append(filename)




def k6():
    data=[b'50\n 10',b'40\n 5',b' 60 \n 0']
    ans=['5.0\r', '8.0\r', '：错误\r']
    response=[]

    s=0
    for i in  range(0,3):
        ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(data[i])
        response.append(ret[0].decode('gb2312').replace("\n","")[-4:])

    for i in range(0,3):
        if ans[i]==response[i]:
            s=s+33.33
            print('测验数据',i+1,'通过',end=' ')
        else:
            print('测验数据',i+1,'失败',end=' ')

    print('得分',s)
    if s<90:
        error_inf.append(filename)

def k7():
    data=[b'5\n 2',b'5\n 5',b' 5 \n 10']
    ans=['3\r', '0\r', '5\r']
    response=[]

    s=0
    for i in  range(0,3):
        ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(data[i])
        response.append(ret[0].decode('gb2312').replace("\n","")[-2:])

    for i in range(0,3):
        if ans[i]==response[i]:
            s=s+33.33
            print('测验数据',i+1,'通过',end=' ')
        else:
            print('测验数据',i+1,'失败',end=' ')

    print('得分',s)
    if s<90:
        error_inf.append(filename)

def k8():
    data=[b'60\n 60',b'100 \n 80',b' 55 \n 10']
    ans=['合格\r', '合格\r', '加油\r']
    response=[]

    s=0
    for i in  range(0,3):
        ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(data[i])
        response.append(ret[0].decode('gb2312').replace("\n","")[-3:])

    for i in range(0,3):
        if ans[i]==response[i]:
            s=s+33.33
            print('测验数据',i+1,'通过',end=' ')
        else:
           print('测验数据',i+1,'失败',end=' ')

    print('得分',s)

    if s<90:
        error_inf.append(filename)


def k9():
    data=[b'60\n 60',b'30 \n 30',b' 45 \n 10']
    ans=['：合格', '：合格', '不合格']
    response=[]

    s=0
    for i in  range(0,3):
        ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(data[i])
        response.append(ret[0].decode('gb2312').replace("\n","")[-4:-1])

    for i in range(0,3):
        if ans[i]==response[i]:
            s=s+33.33
            print('测验数据',i+1,'通过',end=' ')
        else:
            print('测验数据',i+1,'失败',end=' ')

    print('得分',s)
    if s<90:
        error_inf.append(filename)

        
def k10():
    
    data=[b'60\n 60',b'60 \n 70',b' 60 \n 40']
    ans=['继续行驶\r', '继续行驶\r', '速：超速\r']
    response=[]

    s=0
    for i in  range(0,3):
        ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(data[i])
        response.append(ret[0].decode('gb2312').replace("\n","")[-5:])

    for i in range(0,3):
        if ans[i]==response[i]:
            s=s+33.33
            print('测验数据',i+1,'通过',end=' ')
        else:
            print('测验数据',i+1,'失败',end=' ')
    print('得分',s)
    if s<90:
        error_inf.append(filename)

        

def d1():
    s=0 
    for i in file:
        
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 'a=12' in i:
            s+=20
        if 'b=10' in i:
            s+=20
        if ('c=a*a-6' or 'c=a**2-6' ) in i:
            s+=20
        if 'd=c-b' in i:
            s+=20
        if 'print(d)' in i:
            s+=20

        print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-4:-1]=='128':
        print('结果验证通过')
    else:
        print('输出结果有误')



def d2():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 'a=20' in i:
            s+=20
        if 'b=5' in i:
            s+=20
        if ('c=a/b') in i:
            s+=20
        if ('d=c**2' or 'd=c*c') in i:
            s+=20
        if 'print(d)' in i:
            s+=20
        print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-5:-1]=='16.0':
        print('结果验证通过')
    else:
        print('输出结果有误')




def d3():
    s=0 
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 'a=26' in i:
            s+=20
        if 'b=8' in i:
            s+=20
        if ('c=a%b') in i:
            s+=20
        if ('d=8**c') in i:
            s+=20
        if 'print(d)' in i:
            s+=20
        print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-3:-1]=='64':
        print('结果验证通过')
    else:
        print('输出结果有误')


    


def d4():
    s=0 
    for i in file:
        
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 'a=8.71' in i:
            s+=20
        if 'b=3.14' in i:
            s+=20
        if 'c=a-b' in i:
            s+=20
        if 'd=int(c)' in i:
            s+=20
        if 'print(d)' in i:
            s+=20

        print('步骤得分',s,end=' ')
    if s<90:        
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-2:-1]=='5':
        print('结果验证通过')
    else:
        print('输出结果有误')
    


def d5():
    
    s=0
    for i in file:
        
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 'a=12' in i:
            s+=20
        if 'b=37' in i:
            s+=20
        if 'c=b-a' in i:
            s+=20
        if 'd=str(c)' in i:
            s+=20
        if 'print(d)' in i:
            s+=20
      
        print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-3:-1]=='25':
        print('结果验证通过')
    else:
        print('输出结果有误')



def d6():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 'a=6' in i:
            s+=20
        if 'b=4' in i:
            s+=20
        if ('c=b*b-a' or 'c=b**2-a'  ) in i:
            s+=20
        if 'd=float(c)' in i:
            s+=20
        if 'print(d)' in i:
            s+=20
      
        print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-5:-1]=='10.0':
        print('结果验证通过')
    else:
        print('输出结果有误')


def d7():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 'a=93' in i:
            s+=20
        if 'b=10' in i:
            s+=20
        if ('c=a//b' ) in i:
            s+=20
        if 'd=bin(c)' in i:
            s+=20
        if 'print(c)' in i:
            s+=20
      
        print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-2:-1]=='9':
        print('结果验证通过')
    else:
        print('输出结果有误')


def d8():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 'a=23.4' in i:
            s+=20
        if 'b=12.6' in i:
            s+=20
        if ('c=a-b' ) in i:
            s+=20
        if 'd=round(c)' in i:
            s+=20
        if 'print(d)' in i:
            s+=20
      
        print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-3:-1]=='11':
        print('结果验证通过')
    else:
        print('输出结果有误')


def d9():
    s=0
    for i in file:
        
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 'a="福建"' in i:
            
            s+=20
        if 'b="欢迎您"' in i:
            s+=20
        if ('c=a+b' ) in i:
            s+=20
        if 'd=len(c)' in i:
            s+=20
        if 'print(d)' in i:
            s+=20
      
        print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-2:-1]=='5':
        print('结果验证通过')
    else:
        print('输出结果有误')

def d10():
    s=0
    for i in file:
        i=i.replace('\n','')
        i=i.replace(' ','')
        if 'a="2022"' in i:
            s+=20
        if 'b="冬奥"' in i:
            s+=20
        if ('c=a+b' ) in i:
            s+=20
        if 'd=len(c)' in i:
            s+=20
        if 'print(c)' in i:
            s+=20
      

        print('步骤得分',s,end=' ')
    if s<90:
        error_inf.append(filename)
    ret=popen("py "+filename,stdin=pipe, stdout=pipe,stderr=stdout).communicate(input=None)
    if ret[0].decode('gb2312').replace("\n","")[-7:-1]=='2022冬奥':
        print('结果验证通过')
    else:
        print('输出结果有误')






    


        
correct={'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,

       'k1':k1,'k2':k2,'k3':k3,'k4':k4,'k5':k5,'k6':k6,'k7':k7,'k8':k8,'k9':k9,'k10':k10,

       'd1':d1,'d2':d2,'d3':d3,'d4':d4,'d5':d5,'d6':d6,'d7':d7,'d8':d8,'d9':d9,'d10':d10
 
       
       }


















#批改文件目录地址
#path=r'E:\工作区\'
path=input("请输入学生作业批改目录：")

global file

#root=os.listdir(path)

files=[]

files=[f for f in glob(str(path)+'\\**\\*.py',recursive=True)]


global filename
global error_inf
error_inf=[]
批改错误=[]
for i in files:
    with open(i,'r',encoding='utf-8') as file:
        xx=i
        xx=xx.split("\\")
        a=xx[-1][:-3]
        b=xx[-2]
        
        print(b,a)
        filename=i
        try:
            correct[a]()
        except:
            批改错误.append(a)
            


with open('record2.txt','w') as file:
    for i in error_inf:
        file.write(i+'\n')
if len(批改错误)>0:
    print("以下文件不符合命名规范",批改错误)
