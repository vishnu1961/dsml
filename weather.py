# weather=['sunny','sunny','overcast','Rainy','Rainy','Rainy','overcast','sunny','sunny','Rainy','sunny','overcast','overcast','rainy']
# temp=['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
# play=['No','No','yes','yes','yes','No','yes','No','yes','yes','yes','yes','yes','No']
# # from heap import merge 
# from sklearn import preprocessing 
# le=preprocessing.LabelEncoder()
# weather_encoded=le.fit_transform(weather)
# print("weather:",weather_encoded)
# temp_encoded=le.fit_transform(play)
# label=play_le.fit_transform(play) 
# print("Temp:",temp_encoded)
# print("Play:",label)
# features=list(zip(weather_encoded,temp_encoded))
# print(features)
# from sklearn.naive_bayes
# import GaussianNP
# model=GaussianNP()
# model.fit(features,label)
# predicted=model.predict([[0,2]])
# print("predicted value:",predicted)
# print(inverse_transform(predicted))

# weather=['sunny','sunny','overcast','Rainy','Rainy','Rainy','overcast','sunny','sunny','Rainy','sunny','overcast','overcast','rainy']
# temp=['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
# play=['No','No','yes','yes','yes','No','yes','No','yes','yes','yes','yes','yes','No']
# from heapq import merge 
# from sklearn import preprocessing 
# le = preprocessing.LabelEncoder()

# weather_encoded = le.fit_transform(weather)
# print("weather:", weather_encoded)

# temp_encoded = le.fit_transform(temp)   # fixed: was play by mistake
# play_le = preprocessing.LabelEncoder()  # separate encoder for labels
# label = play_le.fit_transform(play)     # fixed: play_le instead of undefined play_le

# print("Temp:", temp_encoded)
# print("Play:", label)

# features = list(zip(weather_encoded, temp_encoded))
# print(features)

# from sklearn.naive_bayes import GaussianNB   # fixed import
# model = GaussianNB()                         # fixed: GaussianNP → GaussianNB
# model.fit(features, label)

# predicted = model.predict([[0, 2]])
# print("predicted value:", predicted)
# print(play_le.inverse_transform(predicted))  # fixed: use play_le for decoding


weather=['sunny','sunny','overcast','Rainy','Rainy','Rainy','overcast','sunny','sunny','Rainy','sunny','overcast','overcast','rainy']
temp=['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
play=['No','No','yes','yes','yes','No','yes','No','yes','yes','yes','yes','yes','No']
from heapq import merge 
from sklearn import preprocessing 
le=preprocessing.LabelEncoder()
weather_encoded=le.fit_transform(weather)
print("weather:",weather_encoded)
temp_encoded=le.fit_transform(temp)
play_le=preprocessing.LabelEncoder()
label=play_le.fit_transform(play) 
print("Temp:",temp_encoded)
print("Play:",label)
features=list(zip(weather_encoded,temp_encoded))
print(features)
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(features,label)
predicted=model.predict([[0,2]])
print("predicted value:",predicted)
print(play_le.inverse_transform(predicted))