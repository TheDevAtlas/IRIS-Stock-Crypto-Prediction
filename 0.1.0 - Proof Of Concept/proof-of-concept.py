# Imports For Data Display And Manipulation
import datetime as dt # The Date And Time
import numpy as np # Basic Functions
import pandas as pd # Data Manipulation And Translations
import matplotlib.pyplot as plt # Visualization

# Imports From The Web
import pandas_datareader as web # Yahoo Finance, World Bank, Ect

# Imports For Machine Learning
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

#-# Setup Company Data #-#

# Choose A Company - IBM, Google, Ect
company = 'IBM'

# Choose A Date Range
start = dt.datetime(1985,7,1)
end = dt.datetime(2010,1,1)

# Pulls Data From Yahoo Finance Btw Start And End Dates
data = web.DataReader(company, 'yahoo', start, end)

#-# Perpare Data And Process #-#

# Scale The Data And Reshape
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))

# Choose How Many Days To Predict
prediction_days = 60

x_train = []
y_train = []

# Go Through Everyday In Prediction Days
for x in range(prediction_days, len(scaled_data)):
    x_train.append(scaled_data[x-prediction_days:x,0])
    y_train.append(scaled_data[x,0])

# Convert Into NumPy Arrays
x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1],1))

#-# Building The Model #-#

# Create The Network
model = Sequential()

# Create The Layers In The Network
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))

# Compile The Network Model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=10,batch_size=256) # Epochs (25) - how many times models sees the data

#-# Test Model On Existing Data #-#

# Load Test Time And Data
test_start = dt.datetime(2010,1,1)
test_end = dt.datetime.now()
test_data = web.DataReader(company, 'yahoo', test_start, test_end)

# Get The Real Prices
actual_prices = test_data['Close'].values
total_dataset = pd.concat((data['Close'], test_data['Close']), axis=0)

model_inputs = total_dataset[len(total_dataset)-len(test_data)-prediction_days:].values
model_inputs = model_inputs.reshape(-1,1)
model_inputs = scaler.transform(model_inputs)

# Attempt To Make A Prediction
x_test = []

for x in range(prediction_days, len(model_inputs)+1):
    x_test.append(model_inputs[x-prediction_days:x,0])

x_test = np.array(x_test)
x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))

predicted_prices = model.predict(x_test)
predicted_prices = scaler.inverse_transform(predicted_prices)

# Plot The Predictions
plt.plot(actual_prices, color='black')
plt.plot(predicted_prices, color='red')
plt.title(f'{company} Share Price')
plt.xlabel('Time')
plt.ylabel('Share Price')
plt.show()