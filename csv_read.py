import pandas as pd
df = pd.read_csv('FEC-presidential-2019.csv', header=1, usecols= [2, 6, 45]) 
df.rename(inplace= True, columns={
    'cycle': 'year',
    'individual_unitemized_contributions_ytd': 'unitemized_ytd',
    'individual_itemized_contributions_ytd': 'itemized_ytd'})

df_filtered = df.query('year > 2017').sort_values(
    by= 'year', ascending=True).dropna()
committee_list = list(df_filtered['committee_name'])
print(committee_list)
