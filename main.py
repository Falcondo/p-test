a=10
print(a)
from sklearn.linear_model import LogisticRegression

model=LogisticRegression()
model.fit(X_train,y_train)

predictions= model.predict(X_test)
predictions[:10]