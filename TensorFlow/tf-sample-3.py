# Importing TensorFlow lib.
import tensorflow as tf 

# Parametrizin graph using placeholders
# (defined like un a lambda function)
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)

sess = tf.Session()

print(sess.run(adder_node, {a: 3, b:4.5}))
print(sess.run(adder_node, {a: [1,3], b: [2, 4]}))

