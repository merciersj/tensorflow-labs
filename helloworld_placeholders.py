import tensorflow as tf

# Create TensorFlow placeholder object
x = tf.placeholder(tf.string)

with tf.Session() as sess:
    # Run the tf.placeholder operation in the session
    output = sess.run(x, feed_dict={x : 'Hello World'})
    print(output)