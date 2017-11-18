import tensorflow as tf

# Create TensorFlow placeholder objects
x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    # Run the tf.placeholder operation in the session
    output = sess.run(x, feed_dict={x : 'Test string', y: 123, z: 45.67})
    print(output)