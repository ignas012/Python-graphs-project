import pandas as pd
import matplotlib.pyplot as plt

def figure(df):
    df["Bendras paslaugų eksportas"] = df["Bendras paslaugų eksportas"].str.replace(",", ".").astype(float)
    df["Bendras paslaugų importas"] = df["Bendras paslaugų importas"].str.replace(",", ".").astype(float)
    df["Bendras paslaugų pagal šalį balansas"] = df["Bendras paslaugų pagal šalį balansas"].str.replace(",", ".").astype(float)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

    ax1.plot(df["Data"], df["Bendras paslaugų eksportas"], label="Paslaugų eksportas")
    ax1.plot(df["Data"], df["Bendras paslaugų importas"], label="Paslaugų importas")
    ax1.plot(df["Data"], df["Bendras paslaugų pagal šalį balansas"], label="Balansas")
    ax1.set_xlabel("Data")
    ax1.set_ylabel("Eurai (milijonai)")
    ax1.set_title("Paslaugų eksportas, importas ir balansas")
    ax1.legend()
    ax1.set_xticklabels(df["Data"], rotation=45, ha="right")
    ax1.set_xticks(range(len(df["Data"])))

    bvp = 100
    df["Eksporto ir importo balansas su BVP"] = (df["Bendras paslaugų eksportas"] - df["Bendras paslaugų importas"]) / bvp
    ax2.plot(df["Data"], df["Eksporto ir importo balansas su BVP"], label="Eksporto ir importo balansas su BVP")
    ax2.set_xlabel("Data")
    ax2.set_ylabel("Procentai %")
    ax2.set_title("Eksporto ir importo balansas su BVP")
    ax2.legend()
    ax2.set_xticks(range(len(df["Data"])))
    ax2.set_xticklabels(df["Data"], rotation=45, ha="right")

    for ax in fig.axes:
        plt.sca(ax)
        plt.xticks(rotation=90)

    plt.tight_layout()

    return fig