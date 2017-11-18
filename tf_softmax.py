import tensorflow as tf

# Create TensorFlow objects that do basic math
x = tf.nn.softmax([2.0, 1.0, 0.2])

with tf.Session() as sess:
    # Run the tf. operation in the session
    output = sess.run(x)
    print(output)