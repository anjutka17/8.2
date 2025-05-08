import numpy as np
import matplotlib.pyplot as plt

def loe_andmed(failinimi):
    nimed, väärtused = [], []
    with open(failinimi, "r", encoding="utf-8") as fail:
        for joon in fail:
            osad = joon.strip().rsplit(" ", 1)
            nimi = osad[0]
            kõrgus = int(osad[1])
            nimed.append(nimi)
            väärtused.append(kõrgus)
    return nimed, väärtused

def kuva_statistika(nimed, kõrgused_np):
    print("Statistiline ülevaade:")
    print(f"Kokku: {kõrgused_np.sum()} m")
    print(f"Keskmine: {kõrgused_np.mean():.2f} m")
    print(f"Kõrgeim: {nimed[np.argmax(kõrgused_np)]} ({kõrgused_np.max()} m)")
    print(f"Madalaim: {nimed[np.argmin(kõrgused_np)]} ({kõrgused_np.min()} m)")

def joonista_diagramm(nimed, väärtused, pealkiri, failinimi):
    plt.figure(figsize=(12, 7))
    plt.bar(nimed, väärtused, color="mediumslateblue")
    plt.title(pealkiri, fontsize=14)
    plt.xlabel("Mäetipud", fontsize=12)
    plt.ylabel("Kõrgus (m)", fontsize=12)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(failinimi)
    plt.show()

def main():
    fail = "maed.txt"
    nimed, kõrgused = loe_andmed(fail)
    kõrgused_np = np.array(kõrgused)

    kuva_statistika(nimed, kõrgused_np)

    # algandmete diagramm
    joonista_diagramm(nimed, kõrgused_np, "Maailma kõrgeimad mäed", "maed_graafik.png")

    # sorteeritud diagramm
    järjestus = np.argsort(-kõrgused_np)  # kahanev sorteerimine
    sort_nimed = np.array(nimed)[järjestus]
    sort_kõrgused = kõrgused_np[järjestus]

    joonista_diagramm(sort_nimed, sort_kõrgused, "Mäed kõrguse järgi (kahanevalt)", "maed_graafik_sorted.png")



