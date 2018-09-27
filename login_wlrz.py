from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
def login_wlrz(username, pwd):
    driver = webdriver.Edge()
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
