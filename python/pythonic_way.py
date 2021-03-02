#!/usr/bin/env python3

'''
Machine Learning = Data -> Observe -> Experiments -> Statistic Analyzing -> Result

github token: 09d343c26fa8b49a1e009cc1fb4ac903a2a1e3fa
ngrok authtoken 1n0UgkY8oIQ6nDII5wv1FFWNLuW_wWZgAQSc268x1TUoZuWi

# Code to prevent colab disconnect (paste it in console browser) 
function KeepWorking(){
 console.log("Working");
 document.querySelector("colab-toolbar-button#connect").click()   
}setInterval(KeepWorking, 60000)
------
Solar Colors:
------
blue: #b58900;
indigo: #6610f2;
purple: #6f42c1;
pink: #e83e8c;
red: #d33682;
orange: #fd7e14;
yellow: #cb4b16;
green: #2aa198;
teal: #20c997;
cyan: #268bd2;
white: #fff;
gray: #839496;
gray-dark: #073642;
primary: #b58900;
secondary: #839496;
success: #2aa198;
info: #268bd2;
warning: #cb4b16;
danger: #d33682;
light: #fdf6e3;
dark: #073642;
'''

# pythonic loop
loop = [result[var] for var in data]

# Merged all csv files to Data Frame
from glob import glob
dataset = glob('../data_*.csv') 
datas = [pd.read_csv(data) for data in dataset]
df_list = pd.concat(datas)
df_list.to_csv('datas.csv', index=False) # export all files to 1 file
df = pd.read_csv('datas.csv')

# To find NaN value, you have to change it to numeric
df = df.apply (pd.to_numeric, errors='coerce')
# See how many rows of NaN
nan_df = df[df.isna().any(axis=1)] # axis=0 is row, axis=1 is column
df = df.dropna() # Drop rows of NaN
df.head() # you'll see the index will be mess up
df.reset_index(drop=True) # Reset the index to be normal

# Make new column with new value
df['new col'] = df['col1'] * df['col2']

# Make new column (City) and take the values from old column (Purchase Address)
'''
-----------------------------------
| Purchase Address                |
-----------------------------------
| 944 Walnut St, Boston, MA 02215 |
-----------------------------------'''
def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]

df['City'] = df['Purchase Address'].apply(lambda x: f'{get_city(x)} ({get_state(x)})')

# Get the group of result by summing every Sales in the City
result = df.groupby('City').sum()['Sales']
result.sort_values(ascending=False) # Sort it from the highest
cities = list(result.index) # get name of the cities from the result

df['ColName'].nunique() # Count distinct values
df['ColName'].count() # Count only non-null values
df['ColName'].size # Count total values including null values

#  Change format to date and time
'''
-----------------------
| Order Date          |
-----------------------
| 2019-01-22 21:25:00 |
-----------------------'''
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Hour'] = df['Order Date'].dt.hour
df['Minute'] = df['Order Date'].dt.minute


# Find the product sold together
# False: Mark all duplicates as True. copy() because it copy from original df
df_list = df[df['Order ID'].duplicated(keep=False)].copy()
# Make a new column and separate the values with comma
df_list['Sold Together'] = dfl.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
# Drop duplicates values
df_list = df_list[['Order ID', 'Sold Together']].drop_duplicates()


