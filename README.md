# Modeling FB User Willingness

## Installation
1. Jupyter Notebook with Python 3
2. All the python packages that are used in the library, e.g.:
   1. numpy
   2. pandas
   3. matplotlib
   4. scikit-learn
   5. xgboost
   6. active learning
   7. ... 

## Description

### Introduction
1. The goal is to predict the willingness of Facebook users to provide their private data to social experiments with certain amount of money
2. The model is trained with the public data of the users and the label of their willingness(yes/no) 
3. The model is trained to predict the willingness of users with the public data of them
4. The project is divided into three parts:
   1. Crawling
   2. Preprocessing
   3. Training
5. Before we enter the code part, this is also part of a social experiment, so we use some questionnaires to collect the accounts and willingness of FB users
   1. ~1000 data were collected
   2. 70% positive

### Crawling
1. The crawled data are all the public data of each user
2. We also take the sum of 'Likes' and sum of posts into consider
3. In total of 60 attributes

### Preprocessing
1. Drop the empty or too scarce columns 
2. Group simliar attributes into one 
3. Rank by 'Education'
4. Group by 'Blood', 'Gender' and 'Religion'
5. Group by 'Hometown' and 'Current City'
6. 37 attributes are extracted from the original 60 ones.

### Training
1. Use upsampling to balance the data
2. Use 5-fold cross-validation as our method to train the data
3. We have tried many different model, e.g.:SVM, random forest ...
4. The highest accuracy is about 81%

### Active Learning
1. Use linear SVM as our learner and try to use the AL as our method
2. We build our own initial strategy and query startegy to choose the data point
3. And combine them in pairs
4. Use upsampling to balance the data
5. Use 5-fold cross-validation as our method to train the data
6. The AL can reach the highest accuracy at about 77%
7. Can be used in other culture since social experiement is culture-dependent.
