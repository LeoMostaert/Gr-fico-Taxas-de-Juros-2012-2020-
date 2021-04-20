import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))

dados = pd.read_excel("Dados.xlsx")
anos = dados["Ano"]

linhas = []
for coluna in dados.keys()[1:]:
    linha, = plt.plot(dados[coluna], label=coluna, marker="o")
    linhas.append(linha) #concatena

plt.axhline(0, color="black", linestyle="-.")
plt.ylim(-5, 15)

plt.legend(handles=linhas)
plt.xticks(range(len(anos)), labels=anos)
plt.xlabel("Ano")
plt.ylabel("Taxas (%)")
plt.show()