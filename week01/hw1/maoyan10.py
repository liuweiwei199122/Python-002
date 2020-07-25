import requests, pandas, random, re
from bs4 import BeautifulSoup as bs
#任务：获取前 10 个电影名称、电影类型和上映时间

#传入url，发送请求并获取html
def get_html(url):
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
		"Cookie": "__mta=212046763.1595598495496.1595599529630.1595601029153.4; uuid_n_v=v1; uuid=51EC27E0CDB411EA9F0EBD9BEC3DAA2B57D95868D1A34384A3192ADFE5ED5A55; _csrf=432daac7bd5a4092ef33b85e225e63f12bbd15aa2b56adc8bce81970bb33d879; mojo-uuid=2989fc9b6e30a6e830165df2dabe6b70; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595598495; _lxsdk_cuid=1738114debcc8-0a7561f3b0465d-b7a1334-100200-1738114debcc8; _lxsdk=51EC27E0CDB411EA9F0EBD9BEC3DAA2B57D95868D1A34384A3192ADFE5ED5A55; __mta=212046763.1595598495496.1595599529630.1595600573456.4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595601029; _lxsdk_s=173815f8d70-bba-d2e-5bf%7C%7C1"
	}
	res = requests.get(url, headers=headers)
	info = bs(res.text, "html.parser")
	return info

url = 'https://maoyan.com/films?showType=3'
info = get_html(url)
#获取前10个链接存入列表
href_list = []

for i in info.find_all('div', attrs={'class': 'movie-item'}):
	href = i.find('a',).get('href')
	complete_href = 'https://maoyan.com' + href
	href_list.append(complete_href)
	if len(href_list) == 10:
		break
print(href_list)
#循环列表，获取电影名称、电影类型和上映时间
movie_list = []
for href in href_list:
	info = get_html(href)
	name = info.find('h1',).text
	#print(name)
	t_list = info.find_all('a', attrs={'class': 'text-link'})
	type_list = []
	movie_dict = {}
	for t in t_list:
		type = t.text
		type_list.append(type)
	pattern = re.compile('\d{4}-\d{2}-\d{2}')

	j = 0
	for li in info.find_all('li', attrs={'class': 'ellipsis'}):
		j += 1
		if j == 3:
			on_time = re.match(pattern, li.text).group()
	movie_dict['name'] = name
	movie_dict['type'] = '/'.join(type_list)
	movie_dict['on_time'] = on_time

	movie_list.append(movie_dict)

movie = pandas.DataFrame(data=movie_list)
movie.to_csv('./movie.csv', encoding='utf-8', index=False, header=False)





