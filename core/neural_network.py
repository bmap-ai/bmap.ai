"""
Neural Network Module
"""

import tensorflow as tf
from tensorflow import keras

class NeuralNetwork:
    def __init__(self, input_dim=10):
        self.model = self._build_model(input_dim)
        
    def _build_model(self, input_dim):
        """Build neural network model"""
        model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=(input_dim,)),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(1, activation='sigmoid')
        ])
        return model