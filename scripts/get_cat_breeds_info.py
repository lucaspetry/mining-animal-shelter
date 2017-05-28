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
  
print "Total: " + str(len(catsUrl)) + "\n"

# Get breeds detailed info and write to file
catsFile = open("../data/extra_breeds_list.csv", 'a')
catsFile.truncate()

count = 1;
for url in catsUrl:
  page = requests.get(url)
  tree = html.fromstring(page.content)
  cat = tree.xpath('//table[@class="table-01"]/tbody/tr[4]/td[2]/text()')[0]
  otherNames = tree.xpath('//table[@class="table-01"]/tbody/tr[5]/td[2]/text()')[0]
  
  size = tree.xpath('//table[@class="table-01"]/tbody/tr[7]/td[2]/a/text()')[0]
  lifeSpan = tree.xpath('//table[@class="table-01"]/tbody/tr[10]/td[2]/text()')[0]
  price = tree.xpath('//table[@class="table-01"]/tbody/tr[14]/td[2]/text()')[0]
  
  adaptability = tree.xpath('//table[@class="table-01"]/tbody/tr[17]/td[2]/span/text()')[0][:1]
  childFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[19]/td[2]/span[1]/text()')[0][:1]
  dogFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[20]/td[2]/span/text()')[0][:1]
  grooming = tree.xpath('//table[@class="table-01"]/tbody/tr[22]/td[2]/span[1]/text()')[0][:1]
  healthIssues = tree.xpath('//table[@class="table-01"]/tbody/tr[23]/td[2]/span[1]/text()')[0][:1]
  intelligence = tree.xpath('//table[@class="table-01"]/tbody/tr[24]/td[2]/span[1]/text()')[0][:1]
  sheddingLevel = tree.xpath('//table[@class="table-01"]/tbody/tr[25]/td[2]/span[1]/text()')[0][:1]
  strangerFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[27]/td[2]/span/text()')[0][:1]

  catsFile.write("Cat,\"" + cat.encode('ascii', 'replace') + "\",\"" + otherNames.encode('ascii', 'replace') + "\",\"" + size.encode('ascii', 'replace') + "\",\"" + lifeSpan.encode('ascii', 'replace') + \
                 "\",\"" + price.encode('ascii', 'replace') + "\"," + adaptability.encode('ascii', 'replace') + "," + \
                 childFriendly.encode('ascii', 'replace') + "," + dogFriendly.encode('ascii', 'replace') + \
                 "," + grooming.encode('ascii', 'replace') + "," + healthIssues.encode('ascii', 'replace') + "," + \
                 intelligence.encode('ascii', 'replace') + "," + sheddingLevel.encode('ascii', 'replace') + "," + \
                 strangerFriendly.encode('ascii', 'replace') + "\n")
  catsFile.flush()
  print cat + ": DONE (" + str(count) + "/" + str(len(catsUrl)) + ")"
  count += 1
  time.sleep(1)
  
catsFile.close()
print "File closed!"

