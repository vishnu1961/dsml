X=[[8,6],[5,6],[7,3],[6,9]]
y=['outsatnding','good','good','outstanding']
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=1)
classifier.fit(X,y)
new_stud=[[5,7]]
print (classifier.predict(new_stud))

