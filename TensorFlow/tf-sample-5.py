import tensorflow as tf 

sess = tf.Session()

# Adding variables (with initial value and type)
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b

# Vbes are not initialized automatically
# Initialization is triggered by: 
init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(linear_model, {x:[1,2,3,4]}))

