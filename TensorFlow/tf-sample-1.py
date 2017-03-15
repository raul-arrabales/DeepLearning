# From https://www.tensorflow.org/get_started/get_started 

# Importing TensorFlow lib.
import tensorflow as tf 

# Creating two constant nodes
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly

print(node1, node2)
# Output: Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)

# Creating and running the session
sess = tf.Session()
print(sess.run([node1, node2]))

# Output: [3.0, 4.0] 


