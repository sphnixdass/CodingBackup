import tensorflow as tf
from tensorflow.python.client import device_lib

tf.function(
    func=None, input_signature=None, autograph=True, experimental_implements=None,
    experimental_autograph_options=None, experimental_relax_shapes=False,
    experimental_compile=True
)


print(device_lib.list_local_devices())
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('XLA_GPU')))