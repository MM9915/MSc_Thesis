import pandas as pd
import pingouin as pg
import numpy as np

df = pd.read_csv(r"C:\Users\mmikkola\OneDrive - Fresenius\Documents\Personal\Uni\Thesis\THESIS_Data_Final.csv")

df['Sales_ACT_1'] = df['Sales_ACT_1'].replace(0, 0.0001)
df['Sales_ACT_2'] = df['Sales_ACT_2'].replace(0, 0.0001)
df['Sales_ACT_3'] = df['Sales_ACT_3'].replace(0, 0.0001)

df['Efficiency_Ratio'] = (df['Upfront'] + df['Milestones'] + df['OPEX']) / df['Total_ACT_3Y']

milestone_eff = df[df['Structure_Type'] == 'Milestone-Heavy']['Efficiency_Ratio']
upfront_eff = df[df['Structure_Type'] == 'Upfront-Heavy']['Efficiency_Ratio']

eff_results = pg.mwu(upfront_eff, milestone_eff)

print(eff_results)
print(f"\nMedian Efficiency (Upfront): {upfront_eff.median():.2f}")
print(f"Median Efficiency (Milestone): {milestone_eff.median():.2f}")