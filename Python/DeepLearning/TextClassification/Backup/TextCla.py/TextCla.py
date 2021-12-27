#https://keras.io/examples/nlp/text_classification_from_scratch/
#https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f
#https://www.tensorflow.org/tutorials/keras/text_classification_with_hub


import tensorflow as tf
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
from tensorflow.keras import layers
import string
import re
import numpy as np

max_features = 20000
embedding_dim = 128
sequence_length = 500
batch_size = 32

def custom_standardization(input_data):
    lowercase = tf.strings.lower(input_data)
    stripped_html = tf.strings.regex_replace(lowercase, "<br />", " ")
    return tf.strings.regex_replace(
        stripped_html, "[%s]" % re.escape(string.punctuation), ""
    )

# Now that we have our custom standardization, we can instantiate our text
# vectorization layer. We are using this layer to normalize, split, and map
# strings to integers, so we set our 'output_mode' to 'int'.
# Note that we're using the default split function,
# and the custom standardization defined above.
# We also set an explicit maximum sequence length, since the CNNs later in our
# model won't support ragged sequences.
vectorize_layer = TextVectorization(
    standardize=custom_standardization,
    max_tokens=max_features,
    output_mode="int",
    output_sequence_length=sequence_length,
)




def vectorize_text(text, label):
    text = tf.expand_dims(text, -1)
    return vectorize_layer(text), label


def tain_model_vcg():
    batch_size = 32
    raw_train_ds = tf.keras.preprocessing.text_dataset_from_directory(
        "aclImdb/train",
        batch_size=batch_size,
        validation_split=0.2,
        subset="training",
        seed=1337,
    )
    raw_val_ds = tf.keras.preprocessing.text_dataset_from_directory(
        "aclImdb/train",
        batch_size=batch_size,
        validation_split=0.2,
        subset="validation",
        seed=1337,
    )
    raw_test_ds = tf.keras.preprocessing.text_dataset_from_directory(
        "aclImdb/test", batch_size=batch_size
    )

    print(
        "Number of batches in raw_train_ds: %d"
        % tf.data.experimental.cardinality(raw_train_ds)
    )
    print(
        "Number of batches in raw_val_ds: %d" % tf.data.experimental.cardinality(raw_val_ds)
    )
    print(
        "Number of batches in raw_test_ds: %d"
        % tf.data.experimental.cardinality(raw_test_ds)
    )

    for text_batch, label_batch in raw_train_ds.take(1):
        for i in range(5):
            print(text_batch.numpy()[i])
            print(label_batch.numpy()[i])




    # Model constants.
    # max_features = 20000
    # embedding_dim = 128
    # sequence_length = 500

    # # Now that we have our custom standardization, we can instantiate our text
    # # vectorization layer. We are using this layer to normalize, split, and map
    # # strings to integers, so we set our 'output_mode' to 'int'.
    # # Note that we're using the default split function,
    # # and the custom standardization defined above.
    # # We also set an explicit maximum sequence length, since the CNNs later in our
    # # model won't support ragged sequences.
    # vectorize_layer = TextVectorization(
    #     standardize=custom_standardization,
    #     max_tokens=max_features,
    #     output_mode="int",
    #     output_sequence_length=sequence_length,
    # )

    # Now that the vocab layer has been created, call `adapt` on a text-only
    # dataset to create the vocabulary. You don't have to batch, but for very large
    # datasets this means you're not keeping spare copies of the dataset in memory.

    # Let's make a text-only dataset (no labels):
    text_ds = raw_train_ds.map(lambda x, y: x)
    # Let's call `adapt`:
    vectorize_layer.adapt(text_ds)



    # Vectorize the data.
    train_ds = raw_train_ds.map(vectorize_text)
    val_ds = raw_val_ds.map(vectorize_text)
    test_ds = raw_test_ds.map(vectorize_text)

    # Do async prefetching / buffering of the data for best performance on GPU.
    train_ds = train_ds.cache().prefetch(buffer_size=10)
    val_ds = val_ds.cache().prefetch(buffer_size=10)
    test_ds = test_ds.cache().prefetch(buffer_size=10)

    # A integer input for vocab indices.
    inputs = tf.keras.Input(shape=(None,), dtype="int64")

    # Next, we add a layer to map those vocab indices into a space of dimensionality
    # 'embedding_dim'.
    x = layers.Embedding(max_features, embedding_dim)(inputs)
    x = layers.Dropout(0.5)(x)

    # Conv1D + global max pooling
    x = layers.Conv1D(128, 7, padding="valid", activation="relu", strides=3)(x)
    x = layers.Conv1D(128, 7, padding="valid", activation="relu", strides=3)(x)
    x = layers.GlobalMaxPooling1D()(x)

    # We add a vanilla hidden layer:
    x = layers.Dense(128, activation="relu")(x)
    x = layers.Dropout(0.5)(x)

    # We project onto a single unit output layer, and squash it with a sigmoid:
    predictions = layers.Dense(1, activation="sigmoid", name="predictions")(x)

    model = tf.keras.Model(inputs, predictions)

    # Compile the model with binary crossentropy loss and an adam optimizer.
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

    epochs = 3

    # Fit the model using the train and test datasets.
    model.fit(train_ds, validation_data=val_ds, epochs=epochs)

    model.evaluate(test_ds)

    # A string input
    inputs = tf.keras.Input(shape=(1,), dtype="string")
    # Turn strings into vocab indices
    indices = vectorize_layer(inputs)
    # Turn vocab indices into predictions
    outputs = model(indices)

    # Our end to end model
    end_to_end_model = tf.keras.Model(inputs, outputs)
    end_to_end_model.compile(
        loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"]
    )

    # Test it with `raw_test_ds`, which yields raw strings

    end_to_end_model.evaluate(raw_test_ds)

    model.save('my_model.h5')


tain_model_vcg()

new_model = tf.keras.models.load_model('my_model.h5')
new_model.summary()

raw_test_ds = tf.keras.preprocessing.text_dataset_from_directory(
        "aclImdb/test", batch_size=batch_size)
test_ds = raw_test_ds.map(vectorize_text)

predictions_new = new_model.predict(x=test_ds, batch_size=10, verbose=0).flatten()



for text_batch, label_batch in raw_test_ds.take(1):
    for i in range(0, len(predictions_new)):
        print(label_batch.numpy()[i], predictions_new[i])

# print(new_model.get_weights())




