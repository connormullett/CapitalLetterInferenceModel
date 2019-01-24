
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from joblib import dump
import pandas as pd


columns = ['x_box', 'y_box', 'width', 'height',
           'onpix', 'x_bar', 'y_bar', 'x2bar', 'y2bar',
           'xybar', 'x2ybar', 'xy2bar', 'x_edge', 'xegvy',
           'y_edge', 'yegvx']

labels = ['letter']

train_data = pd.read_csv('data/train_letters.csv')

x_train = train_data.drop(columns='letter')
y_train = train_data.ix[:, 0]

# min_max_scaler = preprocessing.MinMaxScaler()

# x_train = min_max_scaler.fit_transform(x_train)

# x_train = preprocessing.normalize(x_train)

model = MLPClassifier(solver='adam', alpha=1e-5,
                      hidden_layer_sizes=(50, 8), random_state=1,
                      max_iter=100, verbose=True)

model.fit(x_train, y_train)

dump(model, 'model.joblib')



