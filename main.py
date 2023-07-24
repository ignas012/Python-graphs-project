import pandas as pd
import matplotlib.pyplot as plt
from pirmas_rodiklis import formatted_quarters, eksportas_numbers, importas_numbers, balansas_numbers
from antras_rodiklis import name, balansas
from trecias_rodiklis import bvp_formatted
from antras_grafikas import save_plot_as_image
import pirmas_grafikas as pg

data = {
'Data': formatted_quarters,
'BVP': bvp_formatted,       
'Bendras paslaugų eksportas': eksportas_numbers,
'Bendras paslaugų importas': importas_numbers,
'Bendras paslaugų pagal šalį balansas': balansas_numbers,
'Bendras paslaugų pagal rūšį ir šalį balansas': balansas
}

df = pd.DataFrame(data)
df_str = df.astype(str)
df = df_str.applymap(lambda x: x.replace('.', ','))
df.to_excel('rodikliai.xlsx', index=False)

fig = pg.figure(df)
fig.savefig("1 Grafikas.png", dpi=300)

save_plot_as_image()