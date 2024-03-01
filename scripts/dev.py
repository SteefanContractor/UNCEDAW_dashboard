# %%
import pandas as pd
import plotly.express as px
# %%
data = pd.read_csv('../data/GLOBAL_dataset_180124_V7/COMPLETE_DATASET.csv')
data.dropna(subset=['COUNTRY'], inplace=True)
countries = pd.read_csv('../data/GLOBAL_dataset_180124_V7/countries.csv',usecols=['COUNTRY'])
assert set(data.COUNTRY) == set(countries.COUNTRY)
# %%
# Calculate the number of recommendations per country
recommendations_per_country = data.groupby('COUNTRY')['CEDAW RECOMMENDATION'].count().reset_index()

# Create the plot
px.choropleth(recommendations_per_country, locations='COUNTRY', color='CEDAW RECOMMENDATION',
                    locationmode='country names', title='Number of Recommendations per Country')
