import csv

# Open and read extra dataset
with open('../data/extra_breeds_list.csv') as f:
	reader = csv.reader(f)
	extra_data = list(reader)
    
idx_type = extra_data[0].index('type')
idx_breed = extra_data[0].index('breed')
idx_other_names = extra_data[0].index('other_names')
idx_size = extra_data[0].index('size')
idx_life_span = extra_data[0].index('life_span')
idx_price = extra_data[0].index('price')
idx_adaptability = extra_data[0].index('adaptability')
idx_child_friendly = extra_data[0].index('child_friendly')
idx_cat_dog_friendly = extra_data[0].index('cat_dog_friendly')
idx_grooming = extra_data[0].index('grooming')
idx_health_issues = extra_data[0].index('health_issues')
idx_intelligence = extra_data[0].index('intelligence')
idx_shedding_level = extra_data[0].index('shedding_level')

# Delete header
del extra_data[0]

# Open output file and write new header
output = open("../data/preprocessed_extra.csv", 'w')
output.truncate()
output.write("type,breed,other_names,size,life_span_low,life_span_high,price_low,price_high,adaptability," + \
             "child_friendly,cat_dog_friendly,grooming,health_issues,intelligence,shedding_level\n")

# Write new data
count = 1
for line in extra_data:
  life_span_low = line[idx_life_span].split(' ')[0].split('-')[0]
  life_span_high = line[idx_life_span].split(' ')[0].split('-')[1]
  
  price = line[idx_price]
  price_low = ''
  price_high = ''
  
  if ',' in price:
    price = price[1:-18].split(' - $')
    price_low = price[0]
    price_high = price[1]
  elif price != '?':
    price = price[9:-4].split(' - $')
    price_low = price[0]
    price_high = price[1]
  
  output.write(line[idx_type] + ",\"" + line[idx_breed] + "\",\"" + line[idx_other_names] + "\"," + \
               line[idx_size] + "," + life_span_low + "," + life_span_high + "," + price_low + "," + \
               price_high + "," + line[idx_adaptability] + "," + line[idx_child_friendly] + "," + \
               line[idx_cat_dog_friendly] + "," + line[idx_grooming] + "," + line[idx_health_issues] + "," + \
               line[idx_intelligence] + "," + line[idx_shedding_level] + "\n")
  output.flush()
  print "Line " + str(count) + " processed!"
  count += 1
  
output.close()
print "File closed!"