import pandas as pd
import numpy as np
breast = pd.read_csv("data.csv")
breast.head()
breast['diagnosis'].value_counts()
breast.shape
breast.isnull().sum()
breast.duplicated().sum()
breast.info()
breast.corr()
