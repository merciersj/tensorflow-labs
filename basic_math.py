import tensorflow as tf

# Create TensorFlow objects that do basic math
x = tf.add(5, 2)
y = tf.subtract(tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))
z = tf.multiply(2, 5)

with tf.Session() as sess:
    # Run the tf. operation in the session
    output = sess.run(x)
    print(output)
    output = sess.run(y)
    print(output)
    output = sess.run(z)
    print(output)