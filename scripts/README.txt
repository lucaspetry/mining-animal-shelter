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



=======================================================================================
Merging the original dataset and the additional data
=======================================================================================
