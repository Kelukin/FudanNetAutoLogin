from detectConnect import checkIfCanConnect
from login_wlrz import login_wlrz
import time
lastStatus = True
while True:
    lastStatus = checkIfCanConnect(lastStatus)#定时检查当前网络是否连接
    if lastStatus:
        time.sleep(10)//10秒后开启下一轮询问
    else:
        login_wlrz('yourUserName','yourPassword') #将函数里面对应的参数替换为你的学号以及密码
