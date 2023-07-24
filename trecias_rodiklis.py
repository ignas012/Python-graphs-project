import pandas as pd

def read_google_sheet(url):
    doc_id = url.split('/')[-2]
    export_link = f'https://docs.google.com/spreadsheets/d/{doc_id}/export?format=csv'
    df = pd.read_csv(export_link)
    return df

url = 'https://docs.google.com/spreadsheets/d/1aEnaCDZfHirV8bPlD146dGRMd--WyltI3G_fjMuzvYg/edit?usp=sharing'

df = read_google_sheet(url)

columns = ["Reikšmė"]
new_df = df[columns]
val = new_df.values
reverse_val = val[::-1]
bvp = reverse_val[:, 0]
bvp_formatted = [f"{x:.1f}" for x in bvp]