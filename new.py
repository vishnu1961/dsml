X=[[8,5],[3,7],[3,6],[7,3]]
y=['fruit','vegtable','protein','fruit']
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=1)
classifier.fit(X,y)
tomato=[[6,4]]
print (classifier.predict(tomato))
carrot=[[4,9]]
print (classifier.predict(carrot))
