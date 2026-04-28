import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu, fisher_exact

df = pd.read_csv(r"C:\Users\mmikkola\OneDrive - Fresenius\Documents\Personal\Uni\Thesis\THESIS_Data_Final.csv")

# Convert Total_FC_Accuracy to numeric
df['Total_FC_Accuracy'] = pd.to_numeric(df['Total_FC_Accuracy'], errors='coerce')

# Convert sales columns to numeric
df['Sales_ACT_1'] = pd.to_numeric(df['Sales_ACT_1'], errors='coerce')
df['Sales_ACT_2'] = pd.to_numeric(df['Sales_ACT_2'], errors='coerce')
df['Sales_ACT_3'] = pd.to_numeric(df['Sales_ACT_3'], errors='coerce')

group1 = df[df['Structure_Type'] == 'Milestone-Heavy']['Total_FC_Accuracy']
group2 = df[df['Structure_Type'] == 'Upfront-Heavy']['Total_FC_Accuracy']

u_stat, p_val_mw = mannwhitneyu(group1, group2)

contingency_table = pd.crosstab(df['Structure_Type'], df['Survival'])
odds_ratio, p_val_fisher = fisher_exact(contingency_table)

# --- VISUALIZATION ---

# Plot A: Fisher's Exact Test - Heatmap of Contingency Table
plt.figure(figsize=(8, 5))
sns.heatmap(contingency_table, annot=True, fmt='d', cmap='YlOrRd', cbar_kws={'label': 'Count'})
plt.title(f'Survival Contingency Table by Deal Structure\n(Fisher Exact p-value: {p_val_fisher:.4f}, Odds Ratio: {odds_ratio:.2f})')
plt.ylabel('Deal Structure')
plt.xlabel('Survival Status')
plt.show()

# Plot B: Fisher's Exact Test - Stacked Bar Chart
contingency_pct = contingency_table.div(contingency_table.sum(axis=1), axis=0) * 100
plt.figure(figsize=(10, 6))
contingency_pct.plot(kind='bar', stacked=True, color=['#ff9999', '#66b3ff'])
plt.title(f'Survival Rate by Deal Structure\n(Fisher Exact p-value: {p_val_fisher:.4f})')
plt.ylabel('Percentage (%)')
plt.xlabel('Deal Structure')
plt.legend(title='Survival', labels=['No', 'Yes'])
plt.xticks(rotation=45)
plt.ylim([0, 100])
plt.show()

# Plot C: Boxplot with Swarm (The 'Scientific' View)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Structure_Type', y='Total_FC_Accuracy', data=df, palette='Pastel1')
sns.swarmplot(x='Structure_Type', y='Total_FC_Accuracy', data=df, color="0.25")
plt.title(f'3-Year Forecast Accuracy by Deal Structure\n(Mann-Whitney p-value: {p_val_mw:.4f})')
plt.ylabel('Accuracy Ratio (ACT/FC)')
plt.axhline(1.0, color='red', linestyle='--', label='Perfect Forecast')
plt.legend()
plt.show()

# Plot B: 3-Year Trend (The 'Narrative' View)
# Melting data to show Year 1, 2, and 3 side-by-side
df_melted = df.melt(id_vars=['Case_ID', 'Structure_Type'], 
                    value_vars=['Sales_ACT_1', 'Sales_ACT_2', 'Sales_ACT_3'],
                    var_name='Year', value_name='Actual_Sales')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_melted, x='Year', y='Actual_Sales', hue='Structure_Type', marker='o')
plt.title('Commercial Performance Trajectory: Milestone vs Upfront Heavy')
plt.show()