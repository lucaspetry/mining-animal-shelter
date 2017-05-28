import csv

# Open and read original test dataset
with open('../data/test.csv') as f:
	reader = csv.reader(f)
	train_data = list(reader)
    
idx_Name = train_data[0].index('Name')
idx_AnimalType = train_data[0].index('AnimalType')
idx_SexuponOutcome = train_data[0].index('SexuponOutcome')
idx_AgeuponOutcome = train_data[0].index('AgeuponOutcome')
idx_Breed = train_data[0].index('Breed')
idx_Color = train_data[0].index('Color')
    
# Delete header
del train_data[0]

# Open output file and write new header
output = open("../data/preprocessed_test.csv", 'w')
output.truncate()
output.write("hasName,animalType,sex,isIntact," + \
               "monthsOld,breed1,breed2,isMix,color1,color2\n")

# Write new data
count = 1
for line in train_data:  
  # AnimalID,Name,DateTime,OutcomeType,OutcomeSubtype,AnimalType,SexuponOutcome,AgeuponOutcome,Breed,Color
  
  hasName = 'true' if line[idx_Name] != '' else 'false'
  animalType = line[idx_AnimalType]
  sex = ''
  isIntact = ''
  
  if(line[idx_SexuponOutcome] != '' and line[idx_SexuponOutcome] != 'Unknown'):
    sex = 'F' if line[idx_SexuponOutcome].split(' ')[1] == 'Female' else 'M'
    isIntact = 'true' if line[idx_SexuponOutcome].split(' ')[0] == 'Intact' else 'false'
  
  monthsOld = line[idx_AgeuponOutcome]
  
  if(monthsOld != ''):
    if(monthsOld == '5 weeks'):
      monthsOld = '1 month'

    age = monthsOld.split(' ')[0]
    sufAge = monthsOld.split(' ')[1]

    if(('day' in sufAge) or ('week' in sufAge)):
      monthsOld = '0'
    elif('month' in sufAge):
      monthsOld = age
    elif('year' in sufAge):
      monthsOld = str(int(age) * 12)
  
  breed1 = line[idx_Breed].split('/')[0]
  breed2 = line[idx_Breed].split('/')[1] if len(line[idx_Breed].split('/')) > 1 else ''
  
  isMix = 'false'
  
  if(' Mix' in breed1):
    isMix = 'true'
    breed1 = breed1[:-4]
  elif(' Mix' in breed2):
    isMix = 'true'    
    breed2 = breed2[:-4]
  
  color1 = line[idx_Color].split('/')[0]
  color2 = line[idx_Color].split('/')[1] if len(line[idx_Color].split('/')) > 1 else ''
  
  output.write(hasName + "," + animalType + "," + sex + "," + isIntact + "," + monthsOld + "," + \
               breed1 + "," + breed2 + "," + isMix + "," + color1 + "," + color2 + "\n")
  print "Line " + str(count) + " processed!"
  count += 1

output.close()
print "File closed!"