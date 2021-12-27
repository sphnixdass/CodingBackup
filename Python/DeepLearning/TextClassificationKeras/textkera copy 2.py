import keras
from keras.datasets import reuters
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
import numpy as np


x_train = ['Well done!',
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


# from keras.preprocessing.text import Tokenizer
# # define 5 documents
# docs = ['Well done!',
# 		'Good work',
# 		'Great effort',
# 		'nice work',
# 		'Excellent!']
# # create the tokenizer
# t = Tokenizer()
# # fit the tokenizer on the documents
# t.fit_on_texts(docs)
# # summarize what was learned
# print(t.word_counts)
# print(t.document_count)
# print(t.word_index)
# print(t.word_docs)
# # integer encode documents
# encoded_docs = t.texts_to_matrix(docs, mode='count')
# print(encoded_docs)


# (x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=None, test_split=0.2)
# word_index = reuters.get_word_index(path="/data/Backup/Coding/Python/DeepLearning/TextClassificationKeras/reuters_word_index.json")

# print('# of Training Samples: {}'.format(len(x_train)))
# print('# of Test Samples: {}'.format(len(x_test)))

# num_classes = max(y_train) + 1
# print('# of Classes: {}'.format(num_classes))

# index_to_word = {}
# for key, value in word_index.items():
#     index_to_word[value] = key

# print(' '.join([index_to_word[x] for x in x_train[0]]))
# print(y_train[0])


max_words = 5000

tokenizer = Tokenizer(num_words=max_words)


# x_train = tokenizer.sequences_to_matrix(x_train, mode='binary')
# x_test = tokenizer.sequences_to_matrix(x_test, mode='binary')

# y_train = keras.utils.to_categorical(y_train, num_classes)
# y_test = keras.utils.to_categorical(y_test, num_classes)

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