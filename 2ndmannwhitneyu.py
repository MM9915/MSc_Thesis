import pandas as pd
import pingouin as pg
import numpy as np

df = pd.read_csv(r"C:\Users\mmikkola\OneDrive - Fresenius\Documents\Personal\Uni\Thesis\THESIS_Data_Final.csv")


# 1. Handle the "Killed" projects to avoid division by zero
# Replace 0 actual sales with 0.0001
df['Sales_ACT_1'] = df['Sales_ACT_1'].replace(0, 0.0001)
df['Sales_ACT_2'] = df['Sales_ACT_2'].replace(0, 0.0001)
df['Sales_ACT_3'] = df['Sales_ACT_3'].replace(0, 0.0001)

# 2. Calculate the Investment Efficiency Ratio
# Note: Ensure your column names match your Excel sheet exactly
df['Efficiency_Ratio'] = (df['Upfront'] + df['Milestones'] + df['OPEX']) / df['Total_ACT_3Y']

# 3. Split into the two groups
milestone_eff = df[df['Structure_Type'] == 'Milestone-Heavy']['Efficiency_Ratio']
upfront_eff = df[df['Structure_Type'] == 'Upfront-Heavy']['Efficiency_Ratio']

# 4. Run the Mann-Whitney U Test with Effect Size
eff_results = pg.mwu(upfront_eff, milestone_eff)

print(eff_results)
print(f"\nMedian Efficiency (Upfront): {upfront_eff.median():.2f}")
print(f"Median Efficiency (Milestone): {milestone_eff.median():.2f}")