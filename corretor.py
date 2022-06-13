import pandas as pd
import numpy

from coletor.calha import nomeCalha
from calha import nomeCalha

nomearquivo = "/home/dev03/Downloads/create-plan-total-master/dados.xlsx"

df_atual = pd.read_excel(nomearquivo)

ids_incorretos = [
    [ numpy.int64(5340106), "MANACAPURU" ], # 0 [0,1]
    [ numpy.int64(5340267), "EIRUNEPÉ" ],
]

ids_para_remover = [
    numpy.int64(5341976)
]

for i in range (len(df_atual)):
    for j in range (len(ids_incorretos)):
        if(ids_incorretos[j][0] == df_atual.loc[i, "id_sasi"]):
            df_atual.loc[i, "municipio"]    = ids_incorretos[j][1]
            df_atual.loc[i, "calha"]        = nomeCalha(df_atual.loc[i, "municipio"])

    for k in range ( len(ids_para_remover) ):
        if(ids_para_remover[k] == df_atual.loc[i, "id_sasi"]):
            df_atual = df_atual.drop(i)

df_atual.to_excel(nomearquivo,index=False)

print("Arquivo corrigido!")