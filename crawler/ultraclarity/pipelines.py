# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from ultraclarity.items import UltraclarityItem
import os

class UltraclarityPipeline(object):
    def process_item(self, item, spider):
        # Create files to store all pdf according to their year of publication
        if not os.path.exists('laws/'+item['title'].split('_')[2]+'/'):
            os.makedirs('laws/'+item['title'].split('_')[2]+'/')

        with open('laws/'+item['title'].split('_')[2]+'/'+item['title'], 'w') as f:
            f.write(item['desc'])
        return item
