# From https://www.tensorflow.org/get_started/get_started 

# Importing TensorFlow lib.
import tensorflow as tf 

# Creating two constant nodes
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly

node3 = tf.add(node1, node2)
print("node3: ", node3)

# Creating and running the session
sess = tf.Session()

print("sess.run(node3): ",sess.run(node3))

# Output: [3.0, 4.0]
