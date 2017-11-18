import tensorflow as tf

# Create TensorFlow objects that do basic math
n_features = 120
n_labels = 5
weights = tf.Variable(tf.truncated_normal((n_features, n_labels)))
bias = tf.Variable(tf.zeros(n_labels))
init = tf.global_variables_initializer()

with tf.Session() as sess:
    # Run the tf. operation in the session
    output = sess.run(init)
    print(output)