from time import sleep,ctime
import threading
#让同学同时说和写
#定义说和写的方法
def Talk(content,loop):
    for i in range(loop):
        print('Start talk:%s %s'%(ctime(),content))
        sleep(2)
def Write(content,loop):
    for i in range(loop):
        print('Start write:%s %s'%(ctime(),content))
        sleep(3)
#定义和加载说和写的线程
theads=[]
t1=threading.Thread(target=Talk,args=("hello,11",2))
theads.append(t1)
t2=threading.Thread(target=Write,args=("hello,33",2))
theads.append(t2)
#执行多线程
if __name__=="__main__":
    for t in theads:
        t.start()
    for t in theads:
        t.join()#阻塞线程
    print("all thead end")