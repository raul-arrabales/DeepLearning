import tensorflow as tf
hola = tf.constant('Hi TensorFlow!')
sess = tf.Session()
print(sess.run(hola))


