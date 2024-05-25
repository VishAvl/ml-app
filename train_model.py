from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import pickle 

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a decision tree classifier
clf = DecisionTreeClassifier() 
clf.fit(X, y) 

prediction = clf.predict([[5.1, 3.5, 1.4, 0.2]])
print(prediction)

# Save the model to a file 
with open('model.pkl', 'wb') as f: 
    pickle.dump(clf, f) 
