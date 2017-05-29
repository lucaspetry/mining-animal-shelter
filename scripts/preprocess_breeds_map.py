import csv

MAX_DISTANCE = 3

# Edit distance between strings
def distance(s1, s2):
	if len(s1) > len(s2):
		s1, s2 = s2, s1

	distances = range(len(s1) + 1)
	for i2, c2 in enumerate(s2):
		distances_ = [i2+1]
		for i1, c1 in enumerate(s1):
			if c1 == c2:
				distances_.append(distances[i1])
			else:
				distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
		distances = distances_
	return distances[-1]


# Open csv files
csv_file = []
with open('../data/preprocessed_train.csv', 'r') as f:
	reader = csv.DictReader(f, delimiter=',')
	for row in reader:
		csv_file.append(row)
        
with open('../data/preprocessed_test.csv', 'r') as f:
	reader = csv.DictReader(f, delimiter=',')
	for row in reader:
		csv_file.append(row)

extra_csv_file = []
with open('../data/preprocessed_extra.csv', 'r') as f:
	reader = csv.DictReader(f, delimiter=',')
	for row in reader:
		extra_csv_file.append(row)

# Generate a map between breed names in both CSVs
breed_map = {}
for i in range(len(csv_file)):
	item = csv_file[i]
	if item['breed1'] not in breed_map:
		breed_map.update({item['breed1']: {'csv': 'OK', 'extra': '', 'distance': 99999}})


approximation_count = 0
for i in range(len(extra_csv_file)):
	breed = extra_csv_file[i]['breed']
	smallest_distance = [99999, '']

	for breed_cmp in breed_map:
		breed_distance = distance(breed.lower(), breed_cmp.lower())
		if (breed_distance <= MAX_DISTANCE) and (breed_distance < smallest_distance[0]):
			smallest_distance[0] = breed_distance # Stores the smallest distance so far
			smallest_distance[1] = breed_cmp # Stores who has the smallest distance so far
		if breed_distance == 0:
			break

	if smallest_distance[0] != 99999:
		breed_map[smallest_distance[1]]['extra'] = breed
		breed_map[smallest_distance[1]]['distance'] = smallest_distance[0]
		if smallest_distance[0] > 0:
			approximation_count += 1
			# print(breed + '\n' + smallest_distance[1] + '\nDistance: ' + str(smallest_distance[0]) + '\n########################################')
# print('Total of breed names approximation: ' + str(approximation_count))
# print('########################################\n')

# print('breeds in '+filename+' without any matches:')

output = open("../data/preprocessed_breed_map.csv", 'w')
output.truncate()
output.write("orig_breed1,extra_breed,edit_distance\n")

count = 0
for item in breed_map:
	output.write("\"" + item + "\",\"" + str(breed_map[item]['extra']) + "\"," + str(breed_map[item]['distance']) + "\n")
	output.flush()
	if breed_map[item]['extra'] is '':
		count += 1

output.close()
print('Total de raças: ', len(breed_map))
print('Total de raças sem match: ', count)