学习笔记
异常处理机制的原理
• 异常也是一个类
• 异常捕获过程：
1. 异常类把错误消息打包到一个对象
2. 然后该对象会自动查找到调用栈
3. 直到运行系统找到明确声明如何处理这些类异常的位置
• 所有异常继承自 BaseException
• Traceback 显示了出错的位置，显示的顺序和异常信息对象传播的方向是相反的

常见的异常类型主要有：
1. LookupError 下的 IndexError 和 KeyError
2. IOError
3. NameError
4. TypeError
5. AttributeError
6. ZeroDivisionError

模拟浏览器
# pip install fake-useragent

from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)



# 模拟不同的浏览器

print(f'Chrome浏览器: {ua.chrome}')

# print(ua.safari)

# print(ua.ie)



# 随机返回头部信息，推荐使用

print(f'随机浏览器: {ua.random}')


cookies验证
s = requests.Session()
s.post()


webdriver模拟浏览器行为
from selenium import webdriver

import time



try:

    browser = webdriver.Chrome()

    # 需要安装chrome driver, 和浏览器版本保持一致

    # http://chromedriver.storage.googleapis.com/index.html

    

    browser.get('https://www.douban.com')

    time.sleep(1)



    browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])

    btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')

    btm1.click()



    browser.find_element_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')

    browser.find_element_by_id('password').send_keys('test123test456')

    time.sleep(1)

    browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()



    cookies = browser.get_cookies() # 获取cookies

    print(cookies)

    time.sleep(3)



except Exception as e:

    print(e)

finally:    

    browser.close()


########## 小文件下载：

import requests

image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

r = requests.get(image_url)

with open("python_logo.png",'wb') as f:

    f.write(r.content)



############# 大文件下载：

# 如果文件比较大的话，那么下载下来的文件先放在内存中，内存还是比较有压力的。

# 所以为了防止内存不够用的现象出现，我们要想办法把下载的文件分块写到磁盘中。

import requests

file_url = "http://python.xxx.yyy.pdf"

r = requests.get(file_url, stream=True)

with open("python.pdf", "wb") as pdf:

    for chunk in r.iter_content(chunk_size=1024):

        if chunk:

            pdf.write(chunk)



验证码识别
先安装依赖库libpng, jpeg, libtiff, leptonica

# brew install leptonica

# 安装tesseract

# brew install  tesseract

# 与python对接需要安装的包

# pip3 install Pillow

# pip3 install pytesseract







import requests

import os

from PIL import Image

import pytesseract



# 下载图片

# session = requests.session()

# img_url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1320441599,4127074888&fm=26&gp=0.jpg'

# agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# headers = {'User-Agent': agent}

# r = session.get(img_url, headers=headers)



# with open('cap.jpg', 'wb') as f:

#     f.write(r.content)



# 打开并显示文件

im = Image.open('cap.jpg')

im.show()



# 灰度图片

gray = im.convert('L')

gray.save('c_gray2.jpg')

im.close()



# 二值化

threshold = 100

table = []



for i in range(256):

    if i < threshold:

        table.append(0)

    else:

        table.append(1)



out = gray.point(table, '1')

out.save('c_th.jpg')



th = Image.open('c_th.jpg')

print(pytesseract.image_to_string(th,lang='chi_sim+eng'))



# 各种语言识别库 https://github.com/tesseract-ocr/tessdata

# 放到 /usr/local/Cellar/tesseract/版本/share/tessdata