# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanSpiderPipeline:
    # def process_item(self, item, spider):
    #     return item

    # def process_item(self, item, spider):
    #     title = item['title']
    #     link = item['link']
    #     content = item['content']
    #     output = f'|{title}|\t|{link}|\t|{content}|\n\n'
    #     with open('./doubanmovie.txt', 'a+', encoding='utf-8') as article:
    #         article.write(output)
    #     return item

    def process_item(self, item, spider):
        name = item['name']
        t = item['type']
        on_time = item['on_time']
        output = f'{name},{t},{on_time}\n'
        with open('./maoyan_movie.csv', 'a+', encoding='utf-8') as f:
            f.write(output)
        return item
