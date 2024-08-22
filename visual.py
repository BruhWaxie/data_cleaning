import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('cleaned.csv')

df['Size'].plot(kind='line')
plt.show()