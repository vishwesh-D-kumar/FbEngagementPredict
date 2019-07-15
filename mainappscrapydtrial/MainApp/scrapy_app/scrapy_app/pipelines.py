from FBEngagementPredict.models import *
import json

class ScrapyAppPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'), # this will be passed from django view
        )

    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.
        # print(item)

        main=Mainsite.objects.get(id=self.unique_id)
        print(main.siteurl+"#######################")
        # print("Honto"+str(self.items)+"baka")
        print(len(self.items))
        print(len(list(set(self.items))))
        print(type(self.items))
        for i in list(set(self.items)):
        		# print(i+"This is subsite")
        		# x=Mainsite(siteurl=i)
        		# x.save()
        		main.subsites_set.create(subsiteurl=i)
        		print("done")
        main.crawled=True
        main.save()
    def process_item(self, item, spider):
        # print(str(item)+"what tf")
        x=[i for i in list(set(item['url']))]
        item['url']=x
        for i in item['url']:
        	self.items.append(i)
        if len(list(set(self.items)))>100:
        	return item
        	raise CloseSpider('100 site limit reached')
        return item
