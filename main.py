import numpy as np
import matplotlib.pyplot as plt

# Create x-values
x = np.arange(0, 20, 1)

# Different geometric sequences
a = 1
y_growth = a * (1.2 ** x)        # r > 1 (growth)
y_decay = a * (0.8 ** x)         # 0 < r < 1 (decay)
y_oscillate = a * ((-1.2) ** x)  # r < 0 (oscillating sign)
y_explosive = a * (1.5 ** x)     # larger r (explosive growth)

# Create figure with subplots
plt.figure(figsize=(12, 8))

# 1. Growth
plt.subplot(2, 2, 1)
plt.plot(x, y_growth, linewidth=2)
plt.title("Geometric Growth (r = 1.2)")
plt.grid(True)

# 2. Decay
plt.subplot(2, 2, 2)
plt.plot(x, y_decay, linewidth=2)
plt.title("Geometric Decay (r = 0.8)")
plt.grid(True)

# 3. Oscillating
plt.subplot(2, 2, 3)
plt.plot(x, y_oscillate, linewidth=2)
plt.title("Oscillating Geometric (r = -1.2)")
plt.grid(True)

# 4. Explosive Growth
plt.subplot(2, 2, 4)
plt.plot(x, y_explosive, linewidth=2)
plt.title("Explosive Growth (r = 1.5)")
plt.grid(True)

plt.tight_layout()
plt.show()