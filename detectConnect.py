import urllib.request
import http.client
import time
import urllib.error
def checkIfCanConnect(lastStatus = True):
    urlList = ['https://www.baidu.com','https://cn.bing.com/']
    cnt = 0
    for url in urlList:
        try:
            text = urllib.request.urlopen(url,timeout=5)
            cnt +=1
        except urllib.error.URLError:
            cnt  = cnt
    if cnt == 2:
        if(lastStatus == False):
            print("Reconnect OK!")
        return True
    else:
        print("Lost connect on " + time.strftime("%y-%m-%d-%H:%M",time.localtime(time.time())))
        return False
if __name__ == '__main__':
    if checkIfCanConnect()== True :
        print("Connect OK!")
    else:
        print("No Connect")
