import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris_bunch = load_iris()
iris = pd.DataFrame(iris_bunch.data, columns=iris_bunch.feature_names)

iris['species'] = iris_bunch.target
iris['species'] = iris['species'].map(dict(enumerate(iris_bunch.target_names)))


print("Shape of iris dataset:", iris.shape)
print("\nFirst 5 rows:")
print(iris.head())

print("\nData types and non-nulls:")
print(iris.info())

print("\nSummary statistics:")
print(iris.describe())

print("\nMissing values:")
print(iris.isnull().sum())


print("\nClass distribution:")
print(iris["species"].value_counts())


sns.pairplot(iris, hue='species', diag_kind="kde")
plt.suptitle("Pairplot of Iris Features", y=1.02)
plt.show()


plt.figure(figsize=(8, 6))
sns.heatmap(iris.drop('species', axis=1).corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Matrix")
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(data=iris.drop('species', axis=1))
plt.title("Boxplot for Each Feature")
plt.show()
