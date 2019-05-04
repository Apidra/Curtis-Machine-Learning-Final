import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 

X = np.loadtxt('wine_X.csv',skiprows=0, unpack=False, delimiter=',')
Y = np.loadtxt('wine_Y.csv',skiprows=0, unpack=False, delimiter=',')
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 42)

print('Training...')
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

print('Testing...')
score = knn.score(X_test, y_test)
print('Test set score: {:.2f}'.format(score))
