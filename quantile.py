import matplotlib.pyplot as plt
import numpy as np
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
q1 = np.quantile(data, 0.25)
q2 = np.quantile(data, 0.50) 
q3 = np.quantile(data, 0.75)
plt.figure(figsize=(6, 4))
plt.boxplot(data, vert=False, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='black'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'))
plt.text(q1, 1.1, 'Q1', ha='center', fontsize=9, color='blue')
plt.text(q2, 1.1, 'Median (Q2)', ha='center', fontsize=9, color='red')
plt.text(q3, 1.1, 'Q3', ha='center', fontsize=9, color='green')
plt.title("Quantile Visualization using Boxplot")
plt.xlabel("Values")
plt.yticks([])
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
