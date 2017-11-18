import tensorflow as tf

# Create TensorFlow objects that handle cross entropy
x = tf.reduce_sum([1, 2, 3, 4, 5])
x = tf.log(100.0)

with tf.Session() as sess:
    # Run the tf. operation in the session
    output = sess.run(x)
    print(output)