scrapy startproject spiders
scrapy genspider movies douban.com
scrapy crawl movies

dont_filter=true  不受allow_domain的影响

把list保存到csv文件中
movie = pandas.DataFrame(data=movie_list)
movie.to_csv('./movie.csv', encoding='utf-8', index=False, header=False)

from scrapy import Selector
name = Selector(response=response).xpath('//h1/text()').extract()[0]
extract()：提取Selector对象，返回list
extract_first():提取Selector对象的第一个元素，返回str


__repr__ 和 __str__ 的区别：
前者能把一个对象用字符串的形式表达出来以便辨认，后者是在 str() 函数被使用，或是在用 print 函数打印一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好。
