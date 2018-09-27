# FudanNetAutoLogin
该脚本是用于保持复旦校园网的连接状态。由于复旦校内网络每天晚上便会断开所有连接一次，就很烦。如果想要保持你的远程主机24小时在线的话，就必须设置一个自动登录的脚本。而Login界面会将账号与密码进行加密后发送出去，因此直接构造个request Header并不大OK。查阅之后发现使用Selenium可以较好地模拟人手工登录过程。
## 先期准备
+ 该脚本基于python 3.x
+ 预先通过 `pip install selenium`安装所需的selenium包
+ 根据浏览器及版本的不同选择对应的driver，并将其放置于PATH目录  
    + 如果不大明白PATH的概念，windows用户放置于C:\Windows\System32, Linux用户放置于/usr/bin 或者/usr/local/bin 

|浏览器|下载链接|
|-|-|
|Chrome:|https://sites.google.com/a/chromium.org/chromedriver/downloads|  
|Edge:|https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/|  
|Firefox:|https://github.com/mozilla/geckodriver/releases|  
|Safari:|	https://webkit.org/blog/6900/webdriver-support-in-safari-10/|

## 具体操作
+ 将`login_main.py`中 Line 10 替换入自己的学号以及密码
+ 当前脚本的默认采用的浏览器是Edge，如果不同进入`login_wlrz.py`按照注释进行修改
+ 修改完毕后 `python login_main.py`就OK   

**记得浏览器不要保存学号以及密码**  
**如果浏览器已经保存学号以及密码，直接删除`login_wlrz.py`中的Line 10-16行即可**
