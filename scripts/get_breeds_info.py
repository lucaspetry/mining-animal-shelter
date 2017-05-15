from lxml import html
import requests

dogsUrl = []
for pageNum in range(1, 20):
  page = requests.get('http://www.dogbreedslist.info/all-dog-breeds/list_1_' + str(pageNum) + '.html')
  tree = html.fromstring(page.content)
  urls = tree.xpath('//div[@class="list"]/div[1]/div[2]/div[1]/p/a/@href')
  dogsUrl.extend(urls);
  print "Dog: Page " + str(pageNum) + " read"

print "Total: " + str(len(dogsUrl)) + "\n"

count = 1;
for url in dogsUrl:
  page = requests.get(url)
  tree = html.fromstring(page.content)
  dog = tree.xpath('//table[@class="table-01"]/tbody/tr[4]/td[2]/text()')[0]
  size = tree.xpath('//table[@class="table-01"]/tbody/tr[8]/td[2]/a/text()')[0]
  lifeSpan = tree.xpath('//table[@class="table-01"]/tbody/tr[10]/td[2]/text()')[0]
  
  height = tree.xpath('//table[@class="table-01"]/tbody/tr[12]/td[2]/text()')[0]
  heightSec = tree.xpath('//table[@class="table-01"]/tbody/tr[12]/td[2]/span/text()')
  
  if(heightSec):
    heightSec = heightSec[0]
  
  price = tree.xpath('//table[@class="table-01"]/tbody/tr[16]/td[2]/text()')[0]
  
  print dog + ": DONE (" + str(count) + "/" + str(len(dogsUrl)) + ")"
  count += 1

allCats = []
for pageNum in range(1, 5):
  page = requests.get('http://www.catbreedslist.com/all-cat-breeds/list_1_' + str(pageNum) + '.html')
  tree = html.fromstring(page.content)
  breeds = tree.xpath('//div[@class="list"]/div[1]/div[2]/div[1]/p/a/text()')
  allCats.extend(breeds);
  print "Cat: Page " + str(pageNum) + " read"
  
print "Total: " + str(len(allCats)) + "\n"