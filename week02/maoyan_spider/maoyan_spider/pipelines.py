# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
class MaoyanSpiderPipeline:
    # def process_item(self, item, spider):
    #     return item


    def process_item(self, item, spider):
        print('danger!!!')
        name = item['name']
        t = item['type']
        on_time = item['on_time']

        # output = f'{name},{t},{on_time}\n'
        # with open('./maoyan_movie.csv', 'a+', encoding='utf-8') as f:
        #     f.write(output)
        # return item
        dbInfo = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'movie',
            'charset': 'utf8'
        }
        try:
            conn = pymysql.connect(**dbInfo)
        except Exception as e:
            print(e)
        cur = conn.cursor()
        value = (name, t, on_time)
        sql = 'insert into maoyan(`name`, `type`, `on_time`) values(%s, %s, %s)'

        try:
            cur.execute(sql, value)
            cur.close()
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            conn.close()
        return item


