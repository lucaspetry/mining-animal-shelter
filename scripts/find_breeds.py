import csv

with open('../data/trainProcessed_2.csv') as f:
	reader = csv.reader(f)
	csv_data = list(reader)

with open('../data/extra_dog_breed_size.csv') as f:
	reader = csv.reader(f)
	csv_breeds = list(reader)


data_breeds_index = csv_data[0].index('breed1')
breeds_index = csv_breeds[0].index('Breed')

del csv_data[0]
del csv_breeds[0]

breeds_data = []
breeds_breeds = []

for item in csv_data:
	breed = item[data_breeds_index].lower()
	if breed not in breeds_data:
		breeds_data.append(breed)

for item in csv_breeds:
	breed = item[breeds_index].lower()
	if breed not in breeds_breeds:
		breeds_breeds.append(breed)

print(set(breeds_data) - (set(breeds_data) & set(breeds_breeds)))
