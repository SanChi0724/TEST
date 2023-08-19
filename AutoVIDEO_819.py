import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import selenium
import configparser
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
js="window.open('{}','_blank');"
# 获取指定目录下的所有文件名

def get_file_names(directory):
    file_names = []  # 创建一个空列表用于存储文件名

    try:
        # 遍历指定目录下的所有文件
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)  # 获取文件的完整路径
                file_names.append(file_path)  # 将文件路径添加到列表中
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
        return []

    return file_names

# 去除最后一个小数点后所有字符
def remove_after_last_dot(input_string):
    last_dot_index = input_string.rfind('.')
    if last_dot_index != -1:
        return input_string[:last_dot_index]
    else:
        return input_string


# 创建配置解析器对象
config = configparser.ConfigParser()
# 【读取配置文件】
config.read('config.ini', encoding='utf-8')
path = config.get('Path','path')
delay = config.get('Delay','delay')

fns = get_file_names(str(path))
for f in fns:
    print(f)

# 打开浏览器
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://sweb.alipay.com/page/content-creation/posts?appId=2030093521521524")
browser.maximize_window()
actions = ActionChains(browser)
time.sleep(30)
for i in range(0,10):
    print(i)
    print(fns[i])
    file_name = str(fns[i])
    actions.click(browser.find_element('xpath', '//*[@id="bportal"]/div/div[2]/div/div[1]/div[2]/a[1]/div')).perform()
    actions.click(browser.find_element('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div[2]/div[1]/button')).perform()
    print(file_name)
    browser.find_element('xpath', '//*[@id="root"]/div/div/div[2]/div/div/div/div/div/div/div/div/div/form/div/div/div/div/div/div/div/span/div/div/div/div[1]/div/div/div/div/div/div/div/input').send_keys(file_name)
    time.sleep(int(delay))

    #下一个网站
    browser.execute_script(js.format('https://sweb.alipay.com/page/content-creation/posts?appId=2030093521521524'))
    browser.switch_to.window(browser.window_handles[-1])    #切换到最新页面
    i = i+1
# time.sleep(6000)
print('待机中')
while 1:
    pass