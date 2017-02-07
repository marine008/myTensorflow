import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("/home/marine/tensorflow/mnist_data", one_hot=True)

#x = tf.placeholder("float",[None, 784])
#w = tf.Variable(tf.zeros([784, 10]))
