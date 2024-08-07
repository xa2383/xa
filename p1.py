import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Pgm 1-IRIS.csv')
X = dataset.iloc[:,:4].values
y = dataset['species'].values
dataset.head(5)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
y_pred

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(y_test, y_pred))
cm

df = pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred})
df