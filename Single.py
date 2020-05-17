from time import sleep,ctime
# 让同学先说再写
def Talk():
    print('Start talk:%r'%ctime())
    sleep(2)
def Write():
    print("Start write:%r"%ctime())
    sleep(3)
if __name__=='__main__':
    Talk()
    Write()
    print('All end !%r'%ctime())

