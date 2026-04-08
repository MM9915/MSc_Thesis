import pandas as pd
from scipy.stats import wilcoxon

df = pd.read_csv(r"C:\Users\mmikkola\OneDrive - Fresenius\Documents\Personal\Uni\Thesis\THESIS_Data_Final.csv")

# Convert sales columns to numeric, handling missing values
sales_cols = ['Sales_FC_1', 'Sales_FC_2', 'Sales_FC_3', 'Sales_ACT_1', 'Sales_ACT_2', 'Sales_ACT_3']
for col in sales_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['Forecast_Bias'] = (df['Sales_FC_1']+df['Sales_FC_2']+df['Sales_FC_3'])-(df['Sales_ACT_1']+df['Sales_ACT_2']+df['Sales_ACT_3'])

# 2. Split the data into your two groups (N=8 each), dropping NaN values
milestone_bias = df[df['Structure_Type'] == 'Milestone-Heavy']['Forecast_Bias'].dropna()
upfront_bias = df[df['Structure_Type'] == 'Upfront-Heavy']['Forecast_Bias'].dropna()

# 3. Run the One-Sample Wilcoxon Test for Milestone-Heavy
stat_m, p_val_m = wilcoxon(milestone_bias)
print("--- Milestone-Heavy Bias Test ---")
print(f"Median Bias: {milestone_bias.median():.0f}")
print(f"Wilcoxon p-value (vs 0): {p_val_m:.4f}\n")

# 4. Run the One-Sample Wilcoxon Test for Upfront-Heavy
stat_u, p_val_u = wilcoxon(upfront_bias)
print("--- Upfront-Heavy Bias Test ---")
print(f"Median Bias: {upfront_bias.median():.0f}")
print(f"Wilcoxon p-value (vs 0): {p_val_u:.4f}")