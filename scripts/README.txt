=======================================================================================
Preproessing the original dataset
=======================================================================================
We ran preprocess_breeds.py on the original datasets ("train.csv" and "test.csv"):
$ python preprocess_breeds_train.py
$ python preprocess_breeds_test.py
This resulted in two new files "preprocessed_train.csv" and "preprocessed_test.csv".



=======================================================================================
Getting extra dog/cat breed information
=======================================================================================
We got extra information from the websites:
- http://www.dogbreedslist.info
- http://www.catbreedslist.com

All the extra data was crawled from the web pages and extracted to
"breeds_list_info.csv". To do that we ran these scripts in this order:
$ python get_dog_breeds_info.py
$ python get_cat_breeds_info.py

After getting the data into "breeds_list_info.csv", we preprocess the data and
write the processed data to "preprocessed_extra.csv"
$ python preprocess_breeds_extra.py



=======================================================================================
Merging the original dataset and the additional data
=======================================================================================
Now we want to merge "preprocessed_extra.csv" with "preprocessed_train.csv" and
"preprocessed_test.csv". To do so we first map the breeds from the datasets
using the edit distance similarity measure:
$ python3 preprocess_breed_map.py

This will create the file "preprocessed_breed_map.csv", which we then manually adjust
so all the breeds have a correspondent line in the extra dataset. Afterwards, we ran
the script merge_data.py to build the final preprocessed files "merged_train.csv" and
"merged_test.csv".
$ python3 merge_data.py
