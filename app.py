#pip install gradio

#importing libraries
import gradio as gr
import pickle
import pandas as pd
from joblib import dump, load
from sklearn.preprocessing import StandardScaler

#Importing model
model = pickle.load(open("model/model.pkl", "rb"))
sc = pickle.load(open("model/sc.pkl", "rb"))
# sc=load('model/sc.bin')

#List of merchant category
options = ["Entertainment", "Food & Dining", "Gas & Transport", "Grocery - online", "Grocery", "Health & Fitness",
            "Home", "Kids & Pets", "Misc - online", "Misc", "Personal Care", "Shopping - online", "Shopping", "Travel",]

train = pd.read_csv("dataset/train.csv")
sc = StandardScaler()
sc.fit(train)
#Function to predict the type of transaction
def predict(gender, age, zip, category, amt):
    
    if gender == 'F':
        gender = 0
    else:
        gender = 1

    category = options.index(category)
    df = pd.DataFrame.from_dict({'gender': [gender], 'age': [age], 'zip': [int(zip)], 'category': [category], 'amt': [float(amt)]})
    # 
    print(df)
    print(df.dtypes)
    data = sc.transform(df)
    y_pred = model.predict(data)[0]
    print(y_pred)
    if y_pred == 0:
        return "Geniune Transaction"
    else:
        return "Fraudulent Transaction"
    # return {'Geniune Transaction': y_pred[0], 'Fraudulent Transaction': y_pred[1]}

#Getting inputs
gender = gr.inputs.Radio(['F', 'M'], label="Gender")
age = gr.inputs.Slider(minimum=15, maximum=110, default=20, label="Age")
zip = gr.inputs.Number(default=12345, label="Zip Code")
category = gr.inputs.Dropdown(choices=options, default="select", type="value", label="Merchant Category")
amt = gr.inputs.Number(default=10, label="Amount")

#Launching App
gr.Interface(predict, [gender, age, zip, category, amt], "label", live=False).launch(share=True)


