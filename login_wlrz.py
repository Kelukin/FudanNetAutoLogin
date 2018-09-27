from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
def login_wlrz(username, pwd):
    //当前脚本使用selenium，模拟人手动登录的过程
    driver = webdriver.Edge()//当前默认使用的是Edge浏览器
    //driver = webdriver.Chrome()//浏览器不同也对应着替换，注意的是放到Path下的driver也必须不同
    //driver = webdriver.FireFox()
    driver.get("http://wlrz.fudan.edu.cn")
    elem = driver.find_element_by_name("username")
    elem.clear()
    elem.send_keys(username)#输入账号
    elem = driver.find_element_by_name("pass")
    elem.clear()
    time.sleep(0.1)
    elem.send_keys(pwd)#输入密码


    button = driver.find_element_by_class_name("btn login-btn")
    login_elem = driver.find_element_by_id("button")
    actions = ActionChains(driver)
    actions.move_to_element(login_elem)
    actions.click(login_elem)
    actions.perform()
    driver.close()
    print("Try to reconnect.")
