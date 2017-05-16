from lxml import html
import requests
import time

# Get cats urls
catsUrl = []
for pageNum in range(1, 5):
  page = requests.get('http://www.catbreedslist.com/all-cat-breeds/list_1_' + str(pageNum) + '.html')
  tree = html.fromstring(page.content)
  breeds = tree.xpath('//div[@class="list"]/div[1]/div[2]/div[1]/p/a/@href')
  catsUrl.extend(breeds);
  print "Crawling catbreedslist.com: page " + str(pageNum) + "/4"
  time.sleep(1)
  
print "Total: " + str(len(allCats)) + "\n"

# Get breeds detailed info and write to file
catsFile = open("../data/cats_breeds_list_info.csv", 'w')
catsFile.truncate()

count = 1;
for url in catsUrl:
  page = requests.get(url)
  tree = html.fromstring(page.content)
  cat = tree.xpath('//table[@class="table-01"]/tbody/tr[4]/td[2]/text()')[0]
  size = tree.xpath('//table[@class="table-01"]/tbody/tr[8]/td[2]/a/text()')[0]
  lifeSpan = tree.xpath('//table[@class="table-01"]/tbody/tr[10]/td[2]/text()')[0]
  
  height = tree.xpath('//table[@class="table-01"]/tbody/tr[12]/td[2]/text()')[0]
  heightSec = tree.xpath('//table[@class="table-01"]/tbody/tr[12]/td[2]/span/text()')
  
  if(heightSec):
    heightSec = heightSec[0]
  
  price = tree.xpath('//table[@class="table-01"]/tbody/tr[16]/td[2]/text()')[0]
  
  print cat + ": DONE (" + str(count) + "/" + str(len(catsUrl)) + ")"
  count += 1
  time.sleep(1)
  
catsFile.close()
print "File closed!"

