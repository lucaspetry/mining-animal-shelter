import csv

def load_csv(file):
	csv_file = []
	with open(file, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			csv_file.append(row)

	return csv_file

def write_csv(file, data):
	with open(file, 'w') as f:
		writer = csv.writer(f, quoting=csv.QUOTE_ALL)
		writer.writerows(data)

# open csv files
csv_map = load_csv('../data/preprocessed_breed_map.csv')
extra_csv = load_csv('../data/preprocessed_extra.csv')
breed_train_csv = load_csv('../data/preprocessed_train.csv')
breed_test_csv = load_csv('../data/preprocessed_test.csv')

# column that holds the info about the breed on each csv file
breed_train_index = 5
breed_test_index = 5
breed_extra_index = 1

# map each breed and where it is located in the csv files
extra_indexes = {}
for i in range(len(extra_csv)):
	item = extra_csv[i]
	extra_indexes[item[breed_extra_index]] = i

csv_map_indexes = {}
for i in range(len(csv_map)):
	item = csv_map[i]
	csv_map_indexes[item[1]] = i

train_indexes = {}
for i in range(len(breed_train_csv)):
	item = breed_train_csv[i]
	try:
		train_indexes[item[breed_train_index]].append(i)
	except KeyError:
		train_indexes[item[breed_train_index]] = [i]

test_indexes = {}
for i in range(len(breed_test_csv)):
	item = breed_test_csv[i]
	try:
		test_indexes[item[breed_test_index]].append(i)
	except KeyError:
		test_indexes[item[breed_test_index]] = [i]

# merge train csv
merged_train_csv = []
for row in breed_train_csv:
	new_row = row.copy()

	breed = row[breed_train_index]
	matching_breed = csv_map[csv_map_indexes[breed]][3]

	if matching_breed != '':
		extra_index = extra_indexes[matching_breed]
		extra_line = extra_csv[extra_index]

	for i in range(3, len(extra_line)):
		if matching_breed == '':
			new_row.append('')
		else:
			col = extra_line[i]
			new_row.append(col)

	merged_train_csv.append(new_row)

# merge test csv
merged_test_csv = []
for row in breed_test_csv:
	new_row = row.copy()

	breed = row[breed_test_index]
	matching_breed = csv_map[csv_map_indexes[breed]][3]

	if matching_breed != '':
		extra_index = extra_indexes[matching_breed]
		extra_line = extra_csv[extra_index]

	for i in range(3, len(extra_line)):
		if matching_breed == '':
			new_row.append('')
		else:
			col = extra_line[i]
			new_row.append(col)

	merged_test_csv.append(new_row)

# write to file
write_csv('../data/merged_train.csv', merged_train_csv)
write_csv('../data/merged_test.csv', merged_test_csv)