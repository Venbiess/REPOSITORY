import math
import tensorflow as tf
import numpy as np
A = np.array( [[4, 3, 2, 1, 1], [3, 2, 0, 0, 0]], dtype=float)
B = np.array( [[4, 3, 2, 0, 0], [3, 2, 0, 0, 0]], dtype=float)
l0 = tf.keras.layers.Dense(units=4, input_shape=([2,5]))
l1 = tf.keras.layers.Dense(units=4)
l2 = tf.keras.layers.Dense(units=5)
model = tf.keras.Sequential([l0, l1, l2])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.01))
model.fit(A, B, epochs=5000, verbose=False)
print("Закончили обучение модели")

C = [[5, 4, 3, 0, 0]]
k = model.predict(C)
print(k)
