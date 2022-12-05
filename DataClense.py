import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv");

print (data.head())

#before cleansing the data
sns.lineplot(data=data, x="Item", y="Units")
plt.title("Before cleanse")
plt.show()

cleansed_data = data.groupby('Item').sum().reset_index()
print (cleansed_data)

#After cleanse
cleansed_data.to_csv("cleaned_data.csv",index=False)
sns.lineplot(data=cleansed_data, x="Item", y="Units")
plt.title("After cleanse")
plt.show()
