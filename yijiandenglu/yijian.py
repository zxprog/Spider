# 本地Chrome浏览器设置方法
from selenium import webdriver # 从selenium库中调用webdriver模块
import time # 调用time模块
import cv2
import requests
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
driver = webdriver.Chrome()
url_login = 'http://yjsy1.ustb.edu.cn:8080/pyxx/login.aspx'
student_number = 'g20188777'
password = '972229787zx'
student_name = 'zhouxu' 
driver.get(url_login) # 访问页面
time.sleep(2) # 暂停两秒，等待浏览器缓冲
img_element = driver.find_element_by_id('myCode')
    #print(type(img_element))
validation_img_src = img_element.get_attribute('src')
img_res = requests.get(validation_img_src)  #z这里可能每访问一次，都会随机选择，所以会和看到的不一样，这里相当于访问了第二遍验证码
with open(r'sch_valid_code.jpg','wb+') as f:
    f.write(img_res.content)
plt.imshow(mpimg.imread('sch_valid_code.jpg'))
plt.show()

def login(student_number,student_name,password,validation_code):
    student_login = driver.find_element_by_id('_ctl0_txtusername')
    student_login.send_keys(student_number)
    English_name = driver.find_element_by_id('_ctl0_txtxmpy')
    English_name.send_keys(student_name)
    user_password = driver.find_element_by_id('_ctl0_txtpassword')
    user_password.send_keys(password)
    validation = driver.find_element_by_id('_ctl0_txtyzm')
    validation.send_keys(validation_code)
    login = driver.find_element_by_id('_ctl0_ImageButton1')
    login.click()
###官网上的是aspx文件，卡住了
def choose_link(click_choice):
    '''if click_choice == '查看成绩单':
        report = driver.find_element_by_link_text('http://yjsy1.ustb.edu.cn:8080/pyxx/grgl/xskccjcx')  
        report.click()
    elif click_choice == '查看课表':
        sechdule = driver.find_element_by_link_text('http://yjsy1.ustb.edu.cn:8080/pyxx/pygl/kbcx_xs')  
        sechdule.click()'''
    pass
def choice():
    list = ['查看成绩单','查看课表']
    number = int(input('0：查看成绩单；1：查看课表'))
    return list[number]
	
	
	
validation_code = input('输入你看到的验证码')
choose = choice()
login(student_number,student_name,password,validation_code)
choose_link(choose)