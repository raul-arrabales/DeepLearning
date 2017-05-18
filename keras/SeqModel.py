from keras.models import Sequential
from keras.layers import Dense, Activation

# Create the sequential model (a linear stack of layers)
model = Sequential([
    Dense(32, input_shape=(784,)),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])

# Adding layers can also be done with add()
# model = Sequential()
# model.add(Dense(32, input_dim=784))
# model.add(Activation('relu'))
# model.add(Dense(10))
# model.add(Activation('softmax'))

# Specifying the input shape
model = Sequential()
model.add(Dense(32, input_dim=784))

# Compiling - Parametrization of the model

# For a multi-class classification problem
# model.compile(optimizer='rmsprop',
#              loss='categorical_crossentropy',
#              metrics=['accuracy'])

# For a binary classification problem
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# For a mean squared error regression problem
# model.compile(optimizer='rmsprop',
#              loss='mse')

# For custom metrics
# import keras.backend as K

# def mean_pred(y_true, y_pred):
#     return K.mean(y_pred)  # mean function from TensorFlow

# model.compile(optimizer='rmsprop',
#               loss='binary_crossentropy',
#               metrics=['accuracy', mean_pred])


