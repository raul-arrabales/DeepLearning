import tensorflow as tf 

sess = tf.Session()

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

# Calculate prediction loss (sum of square deltas)
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

# New node for gradient descent optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)

# Loss minimizer node
train = optimizer.minimize(loss)

sess.run(init) # reset values to incorrect defaults.
for i in range(1000):
  sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})

print(sess.run([W, b]))
