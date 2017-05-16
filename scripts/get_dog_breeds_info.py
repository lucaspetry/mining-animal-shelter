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
dogsFile = open("../data/dogs_breeds_list_info.csv", 'w')
dogsFile.truncate()
dogsFile.write("breed,other_names,size,life_span,height,height_sec,price,adaptability," + \
                "apartment_friendly,barking_tendencies,child_friendly,cat_friendly,dog_friendly," + \
                "exercise_needs,grooming,health_issues,intelligence,playfulness,shedding_level," + \
                "stranger_friendly,trainability\n")

count = 1;
for url in dogsUrl:
  page = requests.get(url)
  tree = html.fromstring(page.content)
  dog = tree.xpath('//table[@class="table-01"]/tbody/tr[4]/td[2]/text()')[0]
  otherNames = tree.xpath('//table[@class="table-01"]/tbody/tr[5]/td[2]/text()')[0]
  
  size = tree.xpath('//table[@class="table-01"]/tbody/tr[8]/td[2]/a/text()')[0]
  lifeSpan = tree.xpath('//table[@class="table-01"]/tbody/tr[10]/td[2]/text()')[0]
    
  height = tree.xpath('//table[@class="table-01"]/tbody/tr[12]/td[2]/text()')[0]
  heightSec = tree.xpath('//table[@class="table-01"]/tbody/tr[12]/td[2]/span/text()')
  
  if(heightSec):
    heightSec = heightSec[0]
  else:
    heightSec = "";
  
  price = tree.xpath('//table[@class="table-01"]/tbody/tr[16]/td[2]/text()')[0]
  
  adaptability = tree.xpath('//table[@class="table-01"]/tbody/tr[19]/td[2]/span/text()')[0]
  apartmentFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[20]/td[2]/span[1]/text()')[0]
  barkingTendencies = tree.xpath('//table[@class="table-01"]/tbody/tr[21]/td[2]/span[1]/text()')[0]
  catFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[22]/td[2]/span/text()')[0]
  childFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[23]/td[2]/span[1]/text()')[0]
  dogFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[24]/td[2]/span/text()')[0]
  exerciseNeeds = tree.xpath('//table[@class="table-01"]/tbody/tr[25]/td[2]/span[1]/text()')[0]
  grooming = tree.xpath('//table[@class="table-01"]/tbody/tr[26]/td[2]/span[1]/text()')[0]
  healthIssues = tree.xpath('//table[@class="table-01"]/tbody/tr[27]/td[2]/span[1]/text()')[0]
  intelligence = tree.xpath('//table[@class="table-01"]/tbody/tr[28]/td[2]/span[1]/text()')[0]
  playfulness = tree.xpath('//table[@class="table-01"]/tbody/tr[29]/td[2]/span/text()')[0]
  sheddingLevel = tree.xpath('//table[@class="table-01"]/tbody/tr[30]/td[2]/span[1]/text()')[0]
  strangerFriendly = tree.xpath('//table[@class="table-01"]/tbody/tr[31]/td[2]/span/text()')[0]
  trainability = tree.xpath('//table[@class="table-01"]/tbody/tr[32]/td[2]/span[1]/text()')[0]
  
#  print dog
#  print otherNames
#  print size
#  print lifeSpan
#  print height
#  print heightSec
#  print price
#  print adaptability
#  print apartmentFriendly
#  print barkingTendencies
#  print catFriendly
#  print childFriendly
#  print dogFriendly
#  print exerciseNeeds
#  print grooming
#  print healthIssues
#  print intelligence
#  print playfulness
#  print sheddingLevel
#  print strangerFriendly
#  print trainability
#  print "\n"
  
  dogsFile.write("\"" + dog.encode('ascii', 'replace') + "\",\"" + otherNames.encode('ascii', 'replace') + "\",\"" + size.encode('ascii', 'replace') + "\",\"" + lifeSpan.encode('ascii', 'replace') + \
                 "\",\"" + height.encode('ascii', 'replace') + "\",\"" + heightSec.encode('ascii', 'replace') + "\",\"" + price.encode('ascii', 'replace') + "\",\"" + adaptability.encode('ascii', 'replace') + "\",\"" + \
                 apartmentFriendly.encode('ascii', 'replace') + "\",\"" + barkingTendencies.encode('ascii', 'replace') + "\",\"" + childFriendly.encode('ascii', 'replace') + "\",\"" + catFriendly.encode('ascii', 'replace') + \
                 "\",\"" + dogFriendly.encode('ascii', 'replace') + "\",\"" + exerciseNeeds.encode('ascii', 'replace') + "\",\"" + grooming.encode('ascii', 'replace') + "\",\"" + healthIssues.encode('ascii', 'replace') + "\",\"" + \
                 intelligence.encode('ascii', 'replace') + "\",\"" + playfulness.encode('ascii', 'replace') + "\",\"" + sheddingLevel.encode('ascii', 'replace') + "\",\"" + strangerFriendly.encode('ascii', 'replace') + "\",\"" + \
                 trainability.encode('ascii', 'replace') + "\"\n")
  dogsFile.flush()
  print dog + ": DONE (" + str(count) + "/" + str(len(dogsUrl)) + ")"
  count += 1
  
dogsFile.close()
print "File closed!"