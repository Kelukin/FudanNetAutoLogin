from detectConnect import checkIfCanConnect
from login_wlrz import login_wlrz
import time
lastStatus = True
while True:
    lastStatus = checkIfCanConnect(lastStatus)
    if lastStatus:
        time.sleep(10)
    else:
        login_wlrz('18210240012','305471')
