from sklearn.neighbors import KNeighborsClassifier

X = [[167, 51], [182, 62], [176, 69], [173, 64], [172, 65], [174, 56],[169,58],[173,57],[170,55],[169,53]]
y = ['underweight', 'normal', 'normal', 'normal', 'normal', 'underweight','normal','normal','normal','underweight']

classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(X, y)
question= [[172, 57]]
print("question is predicted as:", classifier.predict(question))
