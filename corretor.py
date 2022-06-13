import pandas as pd
import numpy

from coletor.calha import nomeCalha
from calha import nomeCalha

nomearquivo = "/home/dev03/Downloads/create-plan-total-master/dados.xlsx"

df_atual = pd.read_excel(nomearquivo)

#Formato altercao [ numpy.int64("id_sasi") , "municipio_correto"  ]

ids_incorretos = [
    [numpy.int64(5229394),	"MANACAPURU"],
    [numpy.int64(5229395),	"MANACAPURU"],
    [numpy.int64(5229397),	"MANACAPURU"],
    [numpy.int64(5229399),	"MANACAPURU"],
    [numpy.int64(5229400),	"MANACAPURU"],
    [numpy.int64(5229401),	"MANACAPURU"],
    [numpy.int64(5230909),	"MANACAPURU"],
    [numpy.int64(5246466),	"MANACAPURU"],
    [numpy.int64(5256909),	"BOCA DO ACRE"],
    [numpy.int64(5258032),	"IPIXUNA"],
    [numpy.int64(5258462),	"CAAPIRANGA"],
    [numpy.int64(5270777),	"CAAPIRANGA"],
    [numpy.int64(5272309),	"EIRUNEPÉ"],
    [numpy.int64(5281385),	"ANAMÃ"],
    [numpy.int64(5283239),	"ANAMÃ"],
    [numpy.int64(5286923),	"MANACAPURU"],
    [numpy.int64(5291837),	"BOCA DO ACRE"],
    [numpy.int64(5301346),	"JURUÁ"],
    [numpy.int64(5304555),	"ITACOATIARA"],
    [numpy.int64(5304806),	"ITACOATIARA"],
    [numpy.int64(5304911),	"BENJAMIN CONSTANT"],
    [numpy.int64(5304993),	"ITACOATIARA"],
    [numpy.int64(5305235),	"ITACOATIARA"],
    [numpy.int64(5305513),	"ITACOATIARA"],
    [numpy.int64(5305599),	"ITACOATIARA"],
    [numpy.int64(5305872),	"IPIXUNA"],
    [numpy.int64(5306366),	"ITACOATIARA"],
    [numpy.int64(5306529),	"ITACOATIARA"],
    [numpy.int64(5306642),	"ITACOATIARA"],
    [numpy.int64(5306745),	"ITACOATIARA"],
    [numpy.int64(5307072),	"ITACOATIARA"],
    [numpy.int64(5307501),	"ITACOATIARA"],
    [numpy.int64(5308989),	"ANAMÃ"],
    [numpy.int64(5312100),	"ITACOATIARA"],
    [numpy.int64(5312194),	"ITACOATIARA"],
    [numpy.int64(5312267),	"ITACOATIARA"],
    [numpy.int64(5312327),	"ITACOATIARA"],
    [numpy.int64(5312434),	"ITACOATIARA"]
    [numpy.int64(5312564),	"ITACOATIARA"],
    [numpy.int64(5313680),	"ANAMÃ"],
    [numpy.int64(5315701),	"MANACAPURU"],
    [numpy.int64(5317576),	"ITACOATIARA"],
    [numpy.int64(5317759),	"ITACOATIARA"],
    [numpy.int64(5317933),	"ITACOATIARA"],
    [numpy.int64(5318201),	"ITACOATIARA"],
    [numpy.int64(5318336),	"ITACOATIARA"],
    [numpy.int64(5318444),	"ITACOATIARA"],
    [numpy.int64(5318583),	"ITACOATIARA"],
    [numpy.int64(5318685),	"ITACOATIARA"],
    [numpy.int64(5318745),	"ITACOATIARA"],
    [numpy.int64(5318835),	"ITACOATIARA"],
    [numpy.int64(5318926),	"ITACOATIARA"],
    [numpy.int64(5318988),	"ITACOATIARA"],
    [numpy.int64(5319082),	"ITACOATIARA"],
    [numpy.int64(5319180),	"ITACOATIARA"],
    [numpy.int64(5319258),	"ITACOATIARA"],
    [numpy.int64(5320477),	"MANACAPURU"],
    [numpy.int64(5321222),	"JURUÁ"],
    [numpy.int64(5324128),	"JURUÁ"],
    [numpy.int64(5324499),	"MANACAPURU"],
    [numpy.int64(5325708),	"AMATURÁ"],
    [numpy.int64(5326659),	"ANAMÃ"],
    [numpy.int64(5355509),  "BENJAMIN CONSTANT"],
    [numpy.int64(5363614),  "BENJAMIN CONSTANT"],
    [numpy.int64(5369168),  "CAREIRO"]
]

#Formato remocao numpy.int64("id_sasi") ,

ids_para_remover = [
    numpy.int64(5230818),
    numpy.int64(5340267),
    numpy.int64(5354090),
    numpy.int64(5368309),
    numpy.int64(5368498),
    numpy.int64(5368638),
    numpy.int64(5369043),
]

for i in range (len(df_atual)):
    for j in range (len(ids_incorretos)):
        if(ids_incorretos[j][0] == df_atual.loc[i, "id_sasi"]):
            df_atual.loc[i, "municipio"]    = ids_incorretos[j][1]
            df_atual.loc[i, "calha"]        = nomeCalha(df_atual.loc[i, "municipio"])

    for k in range ( len(ids_para_remover) ):
        if(ids_para_remover[k] == df_atual.loc[i, "id_sasi"]):
            df_atual = df_atual.drop(i)

#cria nova coluna
df_atual['contagem_ativados'] = ''
df_atual['contagem_ativados'] = df_atual['status_valecard']

df_atual['contagem_ativados'] = df_atual['contagem_ativados'].replace('ATIVO', 1, regex=True)
df_atual['contagem_ativados'] = df_atual['contagem_ativados'].replace('Identificador de cartão inválido.', '', regex=True)
df_atual['contagem_ativados'] = df_atual['contagem_ativados'].replace('Cartão não encontrado para o contrato informado.', '', regex=True)
df_atual['contagem_ativados'] = df_atual['contagem_ativados'].replace('BLOQUEADO', '', regex=True)
df_atual['contagem_ativados'] = df_atual['contagem_ativados'].replace('CANCELADO', '', regex=True)
df_atual['contagem_ativados'] = df_atual['contagem_ativados'].replace('EM_ANALISE', '', regex=True)
df_atual['contagem_ativados'] = df_atual['contagem_ativados'].replace('NULL', '', regex=True)

df_atual.to_excel(nomearquivo,index=False)

print("Arquivo corrigido!")