import keras
from keras.datasets import reuters
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
import numpy as np
import pandas as pd


df = pd.read_excel('filename.xlsm', sheetname=0) # can also index sheet by name or fetch all sheets
mylist = df['column name'].tolist()


for i in list: 
    print(i) 
    
x = txt.split(", ")


x_train = ['with reference to your advice that we have no yr acc with zar under reference being a return of funds from thebeneficiary with reason benename and account differ',
		'Good work',
		'Great effort',
		'nice work',
		'Excellent!']

y_train = ['0',
		'1',
		'1',
		'1',
		'1']

x_test = ['Well done!',
		'Good work',
		'Excellent!']

y_test = ['0',
		'1',
		'1']



max_words = 5000

tokenizer = Tokenizer(num_words=max_words)


tokenizer.fit_on_texts(x_train)
tokenizer.fit_on_texts(x_test)

x_train = tokenizer.texts_to_matrix(x_train, mode='binary')
x_test = tokenizer.texts_to_matrix(x_test, mode='binary')

num_classes = 2

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


print(x_train[0])
print(len(x_train[0]))

print(y_train[0])
print(len(y_train[0]))

model = Sequential()
model.add(Dense(512, input_shape=(max_words,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.metrics_names)

batch_size = 32
epochs = 3

history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split=0.1)
score = model.evaluate(x_test, y_test, batch_size=batch_size, verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])


predictions_new = model.predict(x=x_test, batch_size=10, verbose=0)

for i in predictions_new:
    print(i, np.argmax(i), i[np.argmax(i)])