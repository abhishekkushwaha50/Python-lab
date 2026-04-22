import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([10, 20, 30, 40])
df = pd.DataFrame(data, columns=['Values'])

print(df.describe())

plt.plot(df['Values'])
plt.show()