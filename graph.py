import numpy as np
import matplotlib.pyplot as plt

# Define x range for plotting
x = np.linspace(-10, 10, 400)

# Define activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Subtract max(x) for numerical stability
    return exp_x / np.sum(exp_x)

# Plotting
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Sigmoid
axs[0].plot(x, sigmoid(x), label='Sigmoid', color='blue')
axs[0].set_title("Sigmoid Function")
axs[0].set_xlabel("x")
axs[0].set_ylabel("σ(x)")
axs[0].grid(True)

# ReLU
axs[1].plot(x, relu(x), label='ReLU', color='green')
axs[1].set_title("ReLU Function")
axs[1].set_xlabel("x")
axs[1].set_ylabel("f(x)")
axs[1].grid(True)

# Softmax (illustrative example with 3 values)
x_values = np.array([x, x, x])  # To illustrate softmax with a 3D input
softmax_values = np.array([softmax(x_values[:, i]) for i in range(len(x))])
axs[2].plot(x, softmax_values[:, 0], label='Softmax (class 1)', color='red')
axs[2].plot(x, softmax_values[:, 1], label='Softmax (class 2)', color='orange')
axs[2].plot(x, softmax_values[:, 2], label='Softmax (class 3)', color='purple')
axs[2].set_title("Softmax Function")
axs[2].set_xlabel("x")
axs[2].set_ylabel("σ(x)")
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()
