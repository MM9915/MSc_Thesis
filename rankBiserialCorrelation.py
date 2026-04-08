import pandas as pd
import pingouin as pg

df = pd.read_csv(r"C:\Users\mmikkola\OneDrive - Fresenius\Documents\Personal\Uni\Thesis\THESIS_Data_Final.csv")


milestone = df[df['Structure_Type'] == 'Milestone-Heavy']['Total_FC_Accuracy']
upfront = df[df['Structure_Type'] == 'Upfront-Heavy']['Total_FC_Accuracy']

mwu_results = pg.mwu(milestone, upfront)

print(mwu_results)