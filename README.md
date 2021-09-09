# Capstone Project: Credit Card Fraud Detection (Classification)

## Executive Summary

**Do you want to stay ahead in your niche?** Then it is for you. This can be achieved by ensuring the safety of the customer. Nowadays there is an increase in fraudulent activities happening daily. Due to rapid advancement of technology fraudsters find out new strategies to breach the security and get their hands on others asserts. The loop holes in the security systems should be identified and patched. As  it is the most important aspect to gain trust among the buyers and to increase the brand value.

The challenge is, how to improve security functionalities. The financial institutions should monitor each and every transaction and if a suspicious transaction is found it should be scrutinized. If it is found to be a fraudulent transaction then the same should be informed to the customer, upon confirmation the card should be blocked so that further loss of customer’s money is prevented. **But how to find if the transaction is fraudulent or genuine?**

**Calm Down!** We propose the best possible solution. By analysing the data of transactions that occurred in the past. Various parameters such as age, gender, amount, zip code and  merchant category are found to be the top indication factors for fraudulent transactions. Various machine learning models were built and trained. Among all the models Random Forest Classifier was the best model with the highest accuracy score of around 91%.

Now you are aware of the factors which act as an indication for fraudulent transactions. So that advanced safety measures can be formulated and implemented.

We love to collaborate with an esteemed organization like yours. We will help you to ensure your customer’s have a safer experience.

**Safety isn't a slogan, it is a way of LIFE!**

## Purpose

In most of the financial institutions, fraud is identified only after it occurs. Then preventive Measures are formulated and implemented to avoid such incidents happening in future. Ideally, businesses want to find ways to prevent fraud from taking place, or, if that's not possible, to detect it before significant damage is done.

Credit card fraud costs consumers and the financial institutions billions of dollars annually, and fraudsters continuously try to find new tactics to commit illegal actions. With this level of control, fraudsters don't have the chance to make multiple transactions on a stolen or counterfeit card before the cardholder is aware of the fraudulent activity. This alone can save a significant amount of money that would normally be lost to fraud. 


## Problem Statement
Due to rapid advancement of technology fraudsters find out new strategies to breach the security and get their hands on others asserts. The best solution is to monitor the transactions, especially credit card transactions. Our objective is to analyse the past transactions and identify the features which acts as an important indicators for a fradulent transactions. To build and train several classification model and find the best suitable model for credit card fraud detection. 

## Data Cleaning 
Here the work starts with importing the dataset. The dataset contains 61080 rows and 21 columns. The data cleaning part includes the following steps :
- data types of each column are checked and converted appropriately.
- Then null check is done and removed if any.
- The columns are renamed appropriately.
- Unwanted columns are dropped.
- The cleaned data set is then exported to carry on EDA.

## Feature Engineering
- Age column is engineered from the dob column with the help of the datetime library.
- Name column is created by concatenating first name and last name columns.

## EDA
The EDA starts with importing the cleaned dataset. Then the data dictionary is created, which is really helpful as it catalogs and communicates the structure and content of data, and provides meaningful descriptions for individually named data objects.

### Data Dictionary
|Feature|Type|Description|
|---|---|---|
|cc_num|int64|Credit Card Number of Customer|
|name|object|Name of Credit Card Holder| 
|gender|object|Gender of Credit Card Holder| 
|age|int64|Age of Credit Card Holder| 
|job | object|Job of Credit Card Holder| 
|city_pop|int64|Credit Card Holder's City Population|
|zip|int64|Zipcode of Credit Card Holder| 
|merchant | object|Merchant Name| 
|category|object|Category of Merchant| 
|amt | float64|Amount of Transaction| 
|unix_time|int64|UNIX Time of transaction| 
|merch_lat | float64|Latitude Location of Merchant| 
|merch_long|float64|Longitude Location of Merchant| 
|is_fraud | int64| Fraud Flag <--- Target Class| 

- The Distribution of Age is **bimodal**
- Most of the fraudsters Age falls between **25** and **60**  
- The Street with most no. of fraudulent activities - **43235 Mckenzie Views Apt. 837**
- The City with most no. of fraudulent activities - **Houston**
- The State with most no. of fraudulent activities - **New York**
- The Merchant with more fraudulent transactions - **fraud_Rau and Sons**
- The Merchant Category with more fraudulent transactions - **grocery_pos**
- First name of most of the card holders with fraudulent transactions - **Christopher, Robert**
- The highest amount in fraudulent transactions - **1376.04**
- The job of most of the male card holders with fraudulent transactions - **Exhibition designer**
- The job of most of the female card holders with fraudulent transactions - **Prison officer**
- The months with higher fraudulent activities - **March and May**
- The fraudulent activities are higher at **Weekends** (Fri, Sat, Sun)
- The fraudulent activities are higher at around **10th, 20th and 30th** days of the month

## Preprocessing and Modeling
Here, we have divided the target --> Y and features --> X from the cleaned dataset.
 - The features with Object type are encoded using LabelEncoder().
 - The the entire feature set is scaled uniformly with StandarScaler().
 - The scaled data is then splitted into  train and test sets (70% and 30% ratios). 
 - Several machine learning models including Logistic Regression, Random Forest Classifier, CNN were built, trained and tested.

### Evaluation and Conceptual Understanding
It focused on the F1 score(the higher the better) for grading, which is derived from the precision and recall. Various model results are given below

#### Performance Summary
|Model	| F1 Training| F1 Testing|
| --- | ---| --- |
|Logistic Regression      |0.6448      |0.6448      |
|K-Neighbors Classifier   |0.8928      |0.8552      |
|Decision Tree Classifier |1.0         |0.8886      |
|Random Forest Classifier |1.0         |0.9128      |
|AdaBoost Classifier      |0.7836      |0.7771      |
|Support Vector classifer |0.8265      |0.8206      |
|Bagging Classifier       |0.992       |0.901       |
|CNN                      |0.8374      |0.8335      |



### Features to consider
 The Features such as age, gender, amount, zip code and  merchant category are found to be the top indication factors for fraudulent transactions.

### Conclusion and Recommendations
The Random Forest Classifier was the best model with the highest score of around 91% for test data. It has higher F1 score than all other models comparatively. The Best model is saved using pickle library, which can be used later for classification. The saved model is then used to develop an App using Gradio, which takes user inputs and gives the corresponding prediction.

The performance of the model can be further improved by identifying more features which play a significant role in fraudulent transactions. One of the major obstacle faced here is that most of the credit card dataset's feature name and values are encoded to ensure user privacy and safety, which can't be used here. By Overcoming that, the model can be improved.

