import numpy as np
import matplotlib.pyplot as plt

# Customized line plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)', color='red', linewidth=2, marker='o')
plt.plot(x, y2, label='cos(x)', color='blue', linestyle='dotted')
plt.title('Trig functions')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True, linestyle='--', color='gray', alpha=0.6)
plt.show()