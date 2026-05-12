import pandas as pd
import pingouin as pg
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Dataset
df = pd.read_csv(r"C:\Users\mmikkola\OneDrive - Fresenius\Documents\Personal\Uni\Thesis\THESIS_Data_Final.csv")

# 2. Data Cleaning (Preventing Division by Zero)
df = df.replace(0, 0.0001)

# 3. The "Margin Erosion" Test (Mann-Whitney U)
milestone_gp = df[df['Structure_Type'] == 'Milestone-Heavy']['Total_GP_Accuracy']
upfront_gp = df[df['Structure_Type'] == 'Upfront-Heavy']['Total_GP_Accuracy']


# Run the Mann-Whitney U Test
gp_mwu_results = pg.mwu(upfront_gp, milestone_gp)

# Extract the exact p-value to display on the charts
p_val = gp_mwu_results['p_val'].item()
p_text = f"Mann-Whitney U Test p-value: {p_val:.4f}"

print("--- Margin Erosion Test (Mann-Whitney U) ---")
print(gp_mwu_results)
print(f"\nMedian GP Accuracy (Upfront): {upfront_gp.median():.2f}")
print(f"Median GP Accuracy (Milestone): {milestone_gp.median():.2f}\n")

# 4. Data Preparation for Visual Analytics
df_melted = df.melt(id_vars=['Structure_Type'], 
                    value_vars=['Total_FC_Accuracy', 'Total_GP_Accuracy'], 
                    var_name='Metric', 
                    value_name='Accuracy_Ratio')

df_melted['Metric'] = df_melted['Metric'].replace({
    'Sales_Accuracy': 'Sales Accuracy', 
    'GP_Accuracy_Ratio': 'Gross Profit Accuracy'
})

sns.set_theme(style="whitegrid")

# 5. Visual 1: The "Efficiency Gap" (Grouped Bar Chart)
plt.figure(figsize=(10, 6))
sns.barplot(data=df_melted, x='Structure_Type', y='Accuracy_Ratio', hue='Metric', errorbar=None, palette='muted')

plt.axhline(1.0, color='red', linestyle='--', label='100% Accuracy Target')

# Add titles and the p-value subtitle
plt.title('The Efficiency Gap: Sales vs. Gross Profit Accuracy', fontsize=14, pad=20)
plt.ylabel('Average Accuracy Ratio', fontsize=12)
plt.xlabel('Deal Structure', fontsize=12)
plt.legend(title='Financial Metric')
plt.tight_layout()
plt.show()

# 6. Visual 2: GP Volatility and Subsidiary EBIT (Boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_melted, x='Structure_Type', y='Accuracy_Ratio', hue='Metric', palette='pastel')

plt.axhline(1.0, color='red', linestyle='--', label='100% Accuracy Target')

# Add titles and the p-value subtitle
plt.title('Volatility Analysis: Variance Distribution in Sales vs. Gross Profit', fontsize=14, pad=20)
plt.ylabel('Accuracy Ratio Distribution', fontsize=12)
plt.xlabel('Deal Structure', fontsize=12)
plt.legend(title='Financial Metric')
plt.tight_layout()
plt.show()