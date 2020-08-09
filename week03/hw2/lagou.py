# 要求：改造基于 requests 爬虫，增加多线程功能，实现通过拉勾网，获取 北、上、广、深四地 Python 工程师的平均薪水待遇，并将获取结果存入数据库。
# 通过多线程实现 requests 库的多线程方式。
# 获取北京、上海、广州、深圳四个地区，各地区 100 个 Python 工程师职位的职位名称和薪资水平。
# 相同地区、相同职位及相同待遇的职位需去重。
# 将获取的内容存入数据库中。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time,requests,pymongo
from hw2 import mongo
from lxml import etree
from concurrent.futures import ThreadPoolExecutor,TimeoutError
import hw2.constants as cs


def handle_job(city):
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	wb = webdriver.Chrome(chrome_options=chrome_options)
	url = 'https://www.lagou.com'
	wb.get(url)
	wb.find_element_by_xpath(f'//a[@data-city="{city}"]').click()
	wb.find_element_by_xpath('//*[@id="search_input"]').send_keys('python工程师')
	wb.find_element_by_xpath('//*[@id="search_button"]').click()
	wb.find_element_by_xpath('/html/body/div[9]/div/div[2]').click()
	while True:
		time.sleep(2)
		handle_parse(city, wb.page_source)
		try:
			if wb.find_element_by_xpath('//span[@class="pager_next "]').text == '下一页':
				wb.find_element_by_xpath('//span[@class="pager_next "]').click()
		except Exception as e:
			break



def handle_parse(city, page_source):
	p_list = etree.HTML(page_source).xpath('//*[@id="s_position_list"]/ul/li')
	info_list = []
	for p in p_list:
		info = {}
		info['city'] = city
		info['name'] = p.xpath('./div[1]/div[1]/div[1]/a/h3/text()')[0]
		info['salary'] = p.xpath('div[1]/div[1]/div[2]/div/span/text()')[0]
		info_list.append(info)
	mongo.mycollection.insert_many(info_list)


city_list = ['上海','北京','广州','深圳']
with ThreadPoolExecutor(4) as excutor:
	try:
		excutor.map(handle_job, city_list, timeout=3)
	except Exception as e:
		print(e)

