import pandas as pd
import matplotlib.pyplot as plt

def save_plot_as_image():
    from antras_rodiklis import importas, eksportas
    from pirmas_rodiklis import formatted_quarters

    data = {
        'Data': formatted_quarters,
        'Bendras paslaugų eksportas': eksportas,
        'Bendras paslaugų importas': importas,
    }

    df = pd.DataFrame(data)
    df_str = df.astype(str)
    df = df_str.applymap(lambda x: x.replace('.', ','))

    df = df[(df['Bendras paslaugų eksportas'] != "-") & (df['Bendras paslaugų importas'] != "-")]

    df['Bendras paslaugų eksportas'] = df['Bendras paslaugų eksportas'].str.replace(',', '.').astype(float)
    df['Bendras paslaugų importas'] = df['Bendras paslaugų importas'].str.replace(',', '.').astype(float)

    def annual_change(current, previous):
        return ((current - previous) / abs(previous)) * 100

    export_current = df.iloc[-1]['Bendras paslaugų eksportas']
    export_previous = df.iloc[-5]['Bendras paslaugų eksportas']
    import_current = df.iloc[-1]['Bendras paslaugų importas']
    import_previous = df.iloc[-5]['Bendras paslaugų importas']

    export_change = annual_change(export_current, export_previous)
    import_change = annual_change(import_current, import_previous)

    print(f"Metinis eksporto pokytis: {export_change} %")
    print(f"Metinis importo pokytis: {import_change} %")

    plt.figure(figsize=(14, 7))

    plt.subplot(1, 2, 1)
    plt.plot(df['Data'], df['Bendras paslaugų eksportas'])
    plt.title('Bendras paslaugų eksportas per laikotarpį')
    plt.xlabel('Laikotarpis')
    plt.ylabel('Bendras paslaugų eksportas')

    plt.subplot(1, 2, 2)
    plt.plot(df['Data'], df['Bendras paslaugų importas'])
    plt.title('Bendras paslaugų importas per laikotarpį')
    plt.xlabel('Laikotarpis')
    plt.ylabel('Bendras paslaugų importas')
    plt.tight_layout()

    plt.savefig('2 Grafikas.png', dpi=300)

save_plot_as_image()