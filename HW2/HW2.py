import pandas as pd


# Read the file
booli_data = pd.read_csv('Booli_sold.csv')


# Creates a new column, PPSQM = Price Per Square Meter
booli_data['PPSQM'] = booli_data['soldPrice'] / booli_data['livingArea']


print(booli_data[['soldPrice', 'livingArea', 'PPSQM']].head())


# Sorts the values in descending order. 
top_5_expensive = booli_data.sort_values(by='PPSQM', ascending=False).head(5)


#Creates a new file with the added column. 
booli_data.to_csv('Booli_with_price_per_sqm.csv', index=False)




# Show a styled DataFrame in Jupyter Notebook (if using a notebook environment)
top_5_expensive[['soldPrice', 'livingArea', 'PPSQM', 'location.address.streetAddress', 'location.region.municipalityName']].style.format({
    'soldPrice': "{:,.0f} SEK",
    'livingArea': "{:.1f} sqm",
    'ppsqm': "{:,.2f} SEK/sqm"
}).set_caption("Top 5 Most Expensive Apartments by Price per Square Meter")
