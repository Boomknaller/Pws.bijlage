import numpy as np
class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    def forward(self, input):
        # TODO: return output
        pass

    def backward(self, output_gradient, learning_rate):
        # TODO: update parameters and return input gradient
        pass




    ----

    import numpy as np

    class MSE:
        def mse(y_true, y_pred):
            return np.mean(np.power(y_true - y_pred, 2))

        def mse_prime(y_true, y_pred):
            return 2 * (y_pred - y_true) / np.size(y_true)




        -------

        import numpy as np

        class Dense():
            def __init__(self, input_size, output_size):
                self.weights = np.random.randn(output_size, input_size)
                self.bias = np.random.randn(output_size, 1)

            def forward(self, input):
                self.input = input
                return np.dot(self.weights, self.input) + self.bias

            def backward(self, output_gradient, learning_rate):
                weights_gradient = np.dot(output_gradient, self.input.T)
                input_gradient = np.dot(self.weights.T, output_gradient)
                self.weights -= learning_rate * weights_gradient
                self.bias -= learning_rate * output_gradient
                return input_gradient