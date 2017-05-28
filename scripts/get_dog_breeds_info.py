from lxml import html
import requests
import time

# Get dogs urls
dogsUrl = []
for pageNum in range(1, 20):
  page = requests.get('http://www.dogbreedslist.info/all-dog-breeds/list_1_' + str(pageNum) + '.html')
  tree = html.fromstring(page.content)
  urls = tree.xpath('//div[@class="list"]/div[1]/div[2]/div[1]/p/a/@href')
  dogsUrl.extend(urls);
  print "Crawling dogbreedslist.info: page " + str(pageNum) + "/19"
  time.sleep(1)

print "Total: " + str(len(dogsUrl)) + "\n"

# Get breeds detailed info and write to file
dogsFile = open("../data/extra_breeds_list.csv", 'w')
dogsFile.truncate()
dogsFile.write("type,breed,other_names,size,life_span,price,adaptability," + \
                "child_friendly,cat_dog_friendly," + \
                "grooming,health_issues,intelligence,shedding_level," + \
                "stranger_friendly\n")

count = 1;
for url in dogsUrl:
  page = requests.get(url)
  tree = html.fromstring(page.content)
  dog = tree.xpath('//table[@class="table-01"]/tbody/tr[4]/td[2]/text()')[0]
  otherNames = tree.xpath('//table[@class="table-01"]/tbody/tr[5]/td[2]/text()')[0]
  
  size = tree.xpath('//table[@class="table-01"]/tbody/tr[8]/td[2]/a/text()')[0]
  lifeSpan = tree.xpath('//table[@class="table-01"]/tbody/tr[10]/td[2]/text()')[0]  
  price = tree.xpath('//table[@class="table-01"]/tbody/tr[16]/td[2]/text()')[0]
  
  adaptability = tree.xpath('//table[@class="table-01"]/tbody/tr[19]/td[2]/span/text()')[0][:1]
  apartmentFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[20]/td[2]/span[1]/text()')[0][:1]
  catFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[22]/td[2]/span/text()')[0][:1]
  childFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[23]/td[2]/span[1]/text()')[0][:1]
  grooming = tree.xpath('//table[@class="table-01"]/tbody/tr[26]/td[2]/span[1]/text()')[0][:1]
  healthIssues = tree.xpath('//table[@class="table-01"]/tbody/tr[27]/td[2]/span[1]/text()')[0][:1]
  intelligence = tree.xpath('//table[@class="table-01"]/tbody/tr[28]/td[2]/span[1]/text()')[0][:1]
  sheddingLevel = tree.xpath('//table[@class="table-01"]/tbody/tr[30]/td[2]/span[1]/text()')[0][:1]
  strangerFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[31]/td[2]/span/text()')[0][:1]
  
  dogsFile.write("Dog,\"" + dog.encode('ascii', 'replace') + "\",\"" + otherNames.encode('ascii', 'replace') + "\",\"" + size.encode('ascii', 'replace') + "\",\"" + lifeSpan.encode('ascii', 'replace') + \
                 "\",\"" + price.encode('ascii', 'replace') + "\"," + adaptability.encode('ascii', 'replace') + "," + \
                 childFriendly.encode('ascii', 'replace') + "," + catFriendly.encode('ascii', 'replace') + \
                 "," + grooming.encode('ascii', 'replace') + "," + healthIssues.encode('ascii', 'replace') + "," + \
                 intelligence.encode('ascii', 'replace') + "," + sheddingLevel.encode('ascii', 'replace') + "," + \
                 strangerFriendly.encode('ascii', 'replace') + "\n")
  dogsFile.flush()
  print dog + ": DONE (" + str(count) + "/" + str(len(dogsUrl)) + ")"
  count += 1
  
dogsFile.close()
print "File closed!"