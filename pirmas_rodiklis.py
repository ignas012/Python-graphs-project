import pandas as pd
import requests
import io

url = 'https://www.lb.lt/lt/m_statistika/t-paslaugu-eksportas-ir-importas-pagal-sali-1/?ff=1&date_interval%5Bfrom%5D=2015-Q1&date_interval%5Bto%5D=2021-Q4&export=xlsx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def process_data(url, headers, skiprows):
    response = requests.get(url, headers=headers)
    response_content = response.content
    df = pd.read_excel(io.BytesIO(response_content), engine='openpyxl', skiprows=skiprows)
    
    return df

skiprows = 11
df = process_data(url, headers, skiprows)

formatted_quarters = []

roman_to_arabic = {'I': '1', 'II': '2', 'III': '3', 'IV': '4'}

for quarter in df.columns[1:29]:
    year, quarter_info = quarter.split(' - ')
    quarter_num = roman_to_arabic[quarter_info.split()[0]]
    formatted_quarters.append(year + 'Q' + quarter_num)

eksportas_numbers = df.iloc[1, 1:29].to_list()
importas_numbers = df.iloc[2, 1:29].to_list()
balansas_numbers = df.iloc[3, 1:29].to_list()