from sklearn import datasets
from sklearn import model_selection


X,y = datasets.load_diabetes(return_X_y=True, as_frame=True)
X.info()
X_train, y_train, X_test, y_test = model_selection.train_test_split(X,y,test_size=0.2)
X_train.info()
print(X_train.head())