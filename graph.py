import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\mmikkola\OneDrive - Fresenius\Documents\Personal\Uni\Thesis\THESIS_Data_Final.csv")

# Using your filtered dataframe 'df'
plt.figure(figsize=(8, 5))

# Plot the Empirical Cumulative Distribution Function (ECDF)
sns.ecdfplot(data=df, x='Total_FC_Accuracy', hue='Structure_Type', palette=['#1f77b4', '#7f7f7f'])

plt.title('Stochastic Dominance: Milestone vs. Upfront Heavy')
plt.xlabel('3-Year Accuracy Ratio (ACT/FC)')
plt.ylabel('Cumulative Proportion of Sample')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()