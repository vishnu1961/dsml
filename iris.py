import pandas as pd
import numpy as np
import seaborn as sns 
from sklearn.datasets import load_iris
iris_bunch=load_iris()
iris_pd.dataframe(iris_bunch.data,columns=iris_bunch.feature_names)
iris['species']=iris_bunch.target
iris['species']=iris['species'].map(dict(enumerate(iris_bunch.target_names)))
print("shape ")
