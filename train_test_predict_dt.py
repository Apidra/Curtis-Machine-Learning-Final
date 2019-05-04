import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#load x and y datasets
x = np.loadtxt('wine_X.csv', skiprows=0, unpack=False, delimiter=',')
y = np.loadtxt('wine_Y.csv', skiprows=0, unpack=False, delimiter=',')

X_train, X_test, y_train, y_test = train_test_split(x, y, stratify = y, random_state = 42)

#Train
print('Training...')
tree1 = DecisionTreeClassifier( random_state = 42 )
#tree2 w/ pruning, found that a depth of 11 was the sweet spot
tree2 = DecisionTreeClassifier( max_depth = 11, random_state = 42 )
tree1.fit (X_train, y_train ) 
tree2.fit (X_train, y_train ) 

print('Testing...')
#test tree1
print("Accuracy on training set: {:.3f}".format(tree1.score( X_train , y_train)))
print( "Accuracy on test set: {:.3f}".format(tree1.score( X_test , y_test)))
#test tree2
print("Accuracy on training set with pruning: {:.3f}".format(tree2.score( X_train , y_train)))
print( "Accuracy on test set with pruning: {:.3f}".format(tree2.score( X_test , y_test)))
#print feature importance
print( "Feature importances: \n {}".format (tree2.feature_importances_ )) 

#predict qualities 3-8
print("Predicting 3 quality...")
print(tree2.predict(np.array([ [7.1,0.875,0.05,5.7,0.08199999999999999,3.0,14.0,0.99808,3.4,0.52,10.2] ])))

print("Predicting 4 quality...")
print(tree2.predict(np.array([ [8.1,0.87,0.0,3.3,0.096,26.0,61.0,1.00025,3.6,0.72,9.8] ])))

print("Predicting 5 quality...")
print(tree2.predict(np.array([ [7.7,0.775,0.42,1.9,0.092,8.0,86.0,0.9959,3.23,0.59,9.5] ])))

print("Predicting 6 quality...")
print(tree2.predict(np.array([ [7.9,0.32,0.51,1.8,0.341,17.0,56.0,0.9969,3.04,1.08,9.2] ])))

print("Predicting 7 quality...")
print(tree2.predict(np.array([ [5.4,0.835,0.08,1.2,0.046,13.0,93.0,0.9924,3.57,0.85,13.0] ])))

print("Predicting 8 quality...")
print(tree2.predict(np.array([ [7.9,0.35,0.46,3.6,0.078,15.0,37.0,0.9973,3.35,0.86,12.8] ])))

