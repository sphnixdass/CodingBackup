import keras
from keras.datasets import reuters
import numpy as np

(x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=None, test_split=0.2)
word_index = reuters.get_word_index()
num_classess = max(y_train) + 1

from keras.preprocessing.text import Tokenizer

max_words = 10000
tokenizer = Tokenizer(num_words=max_words)
#for only tfidf
#tokenizer.fit_on_sequences(x_train)

x_train = tokenizer.sequences_to_matrix(x_train, mode='binary')
x_test = tokenizer.sequences_to_matrix(x_test, mode='binary')
# x_train = tokenizer.sequences_to_matrix(x_train, mode='count')
# x_test = tokenizer.sequences_to_matrix(x_test, mode='count')
# x_train = tokenizer.sequences_to_matrix(x_train, mode='freq')
# x_test = tokenizer.sequences_to_matrix(x_test, mode='freq')
# x_train = tokenizer.sequences_to_matrix(x_train, mode='tfidf')
# x_test = tokenizer.sequences_to_matrix(x_test, mode='tfidf')

y_train = keras.utils.to_categorical(y_train, num_classess)
y_test = keras.utils.to_categorical(y_test, num_classess)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation

model = Sequential()
model.add(Dense(512, input_shape=(max_words, )))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classess))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

batch_size = 32
epochs = 2

_ = model.fit(x_train, y_train, batch_size=32, epochs=2, verbose=1, validation_split=0.1)
score = model.evaluate(x_test, y_test, batch_size=32,verbose=1)

print(score)

