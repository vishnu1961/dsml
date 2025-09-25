chills=['yes','yes','yes','no','no','no','no','yes']
runningnose=['no','yes','no','yes','no','yes','yes','yes']
headache=['mild','no','strong','mild','no','strong','strong','mild']
fever=['yes','no','yes','yes','no','yes','no','yes',]
flu=['no','yes','yes','yes','no','yes','no','yes']
from heapq import merge
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
chills_encoded=le.fit_transform(chills)
print("Chill:",chills_encoded)
runningnose_encoded=le.fit_transform(runningnose)
print("Running Nose:",runningnose_encoded)
headache_encoded=le.fit_transform(headache)
print("Headache:",headache_encoded)
fever_encoded=le.fit_transform(fever)
print("Fever:",fever_encoded)
label=le.fit_transform(flu)
print("Flu:",label)
features=list(zip(chills_encoded,runningnose_encoded,headache_encoded,fever_encoded))
print(features)
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(features,label)
predicted=model.predict([[0,1,2,1]])
print("Predicted value:",predicted)
print(le.inverse_transform(predicted))