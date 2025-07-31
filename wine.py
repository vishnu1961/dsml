import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine_bunch = load_wine()
wine = pd.DataFrame(wine_bunch.data, columns=wine_bunch.feature_names)

wine['target'] = wine_bunch.target
wine['target'] = wine['target'].map(dict(enumerate(wine_bunch.target_names)))
print("Shape of dataset:", wine.shape)
print("\nFirst 5 rows:")
print(wine.head())
print("\nData types and non-nulls:")
print(wine.info())
print("\nSummary statistics:")
print(wine.describe())
print("\nMissing values:")
print(wine.isnull().sum())
print("\nClass distribution:")
print(wine['target'].value_counts())

sns.pairplot(wine, hue='target', diag_kind="kde")
plt.suptitle("Pairplot of Wine Features", y=1.02)
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(wine.drop('target', axis=1).corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Matrix")
plt.show()

plt.figure(figsize=(14, 10))
sns.boxplot(data=wine.drop('target', axis=1), orient='h')
plt.title("Boxplot for Each Feature")
plt.tight_layout()
plt.show()
