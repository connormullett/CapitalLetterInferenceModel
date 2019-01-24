
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
import pandas as pd
from joblib import load

test_data = pd.read_csv('data/test_letters.csv')

y_test = test_data.ix[:, 0]
x_test = test_data.drop(columns='letter')

# min_max_scaler = preprocessing.MinMaxScaler()

# x_test = min_max_scaler.fit_transform(x_test)
# x_test = preprocessing.normalize(x_test)

model = load('model.joblib')

predictions = []

for i in x_test.values:
    pred = model.predict([i])
    predictions.append(pred)


actuals = []

for i in y_test.values:
    actuals.append(i)

acc = accuracy_score(actuals, predictions, normalize=True)

print(predictions[:5])
print(actuals[:5])

print(acc)


# prediction1 = model.predict([x_test.iloc[0]])
# for i, x in enumerate(y_test):
#     true = y_test[i]
#     pred = model.predict([x_test.iloc[i]])[0]
#     if true == pred:
#         correct += 1
#     total += 1

# print(correct, total)

