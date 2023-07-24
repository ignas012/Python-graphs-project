import pandas as pd
import requests
import io

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def process_data(url, headers, skiprows):
    response = requests.get(url, headers=headers)
    response_content = response.content
    df = pd.read_excel(io.BytesIO(response_content), engine='openpyxl', skiprows=skiprows)
    
    return df

quarters = [f'2020-Q{i}' for i in range(1, 5)] + [f'2021-Q{i}' for i in range(1, 5)]

qauter_second_rodiklis = []
eksportas_numbers_second = []
importas_numbers_second = []
balansas_numbers_second = []
name = []

for quarter in quarters:
    url = f'https://www.lb.lt/lt/m_statistika/t-paslaugu-eksportas-ir-importas-pagal-paslaugos-rusi-ir-sali/?ff=1&date_interval={quarter}&export=xlsx'
    df = process_data(url, headers, 9)
    
    year, quarter_info = df.columns[1:2][0].split(' - ')
    quarter_num = quarter_info.split()[0]
    qauter_second_rodiklis.append(year + 'Q' + quarter_num)
    
    row_index = 3
    while not pd.isna(df.iloc[row_index, 1]):
        eksportas_numbers_second.extend(df.iloc[row_index, 1:2].tolist())
        importas_numbers_second.extend(df.iloc[row_index+1, 1:2].tolist())
        balansas_numbers_second.extend(df.iloc[row_index+2, 1:2].tolist())
        row_index += 4
    
    row_index = 2
    name = []
    while not pd.isna(df.iloc[row_index, 0]):
        name.extend(df.iloc[row_index, 0:1].tolist())
        row_index += 4
    another_var = name[:13]

balansas_numbers_second_copy = balansas_numbers_second.copy()

indices_to_remove = [i for i in range(0, len(balansas_numbers_second_copy), 13)]
indices_to_remove = sorted(indices_to_remove, reverse=True)

for index in indices_to_remove:
    del balansas_numbers_second_copy[index]
    
bendras_balansas = balansas_numbers_second[::13]

n = 12
chunks = [balansas_numbers_second_copy[i:i + n] for i in range(0, len(balansas_numbers_second_copy), n)]
Q1_2020, Q2_2020, Q3_2020, Q4_2020, Q1_2021, Q2_2021, Q3_2021, Q4_2021 = chunks[:8]

hyphens = ['-'] * 20

balansas = hyphens + bendras_balansas
importas = hyphens + importas_numbers_second[::13]
eksportas = hyphens + eksportas_numbers_second[::13]