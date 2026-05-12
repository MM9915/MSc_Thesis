import pandas as pd
import pingouin as pg
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu, fisher_exact

df = pd.read_csv(r"C:\Users\mmikkola\OneDrive - Fresenius\Documents\Personal\Uni\Thesis\THESIS_Data_Final.csv")

df['GP_ACT_1'] = df['GP_ACT_1'].replace(0, 0.0001)
df['GP_ACT_2'] = df['GP_ACT_2'].replace(0, 0.0001)
df['GP_ACT_3'] = df['GP_ACT_3'].replace(0, 0.0001)

df['Efficiency_Ratio'] = (df['GP_ACT_1'] + df['GP_ACT_2'] + df['GP_ACT_3']) / (df['Sales_ACT_1'] + df['Sales_ACT_2'] + df['Sales_ACT_3'])

milestone_eff = df[df['Structure_Type'] == 'Milestone-Heavy']['Efficiency_Ratio']
upfront_eff = df[df['Structure_Type'] == 'Upfront-Heavy']['Efficiency_Ratio']

eff_results = pg.mwu(upfront_eff, milestone_eff)


u_stat, p_val_mw = mannwhitneyu(upfront_eff, milestone_eff)



print(eff_results)
print(f"\nMedian Efficiency (Upfront): {upfront_eff.median():.2f}")
print(f"Median Efficiency (Milestone): {milestone_eff.median():.2f}")

plt.figure(figsize=(10, 6))
sns.boxplot(x='Structure_Type', y='Total_GP_Accuracy', data=df, palette='Pastel1')
sns.swarmplot(x='Structure_Type', y='Total_GP_Accuracy', data=df, color="0.25")
plt.title(f'3-Year GP Accuracy by Deal Structure\n(Mann-Whitney p-value: {p_val_mw:.4f})')
plt.ylabel('Accuracy Ratio (ACT/FC)')
plt.axhline(1.0, color='red', linestyle='--', label='Perfect Forecast')
plt.legend()
plt.show()