import pandas as pd
import xlsxwriter 

minha_planilha = pd.read_excel('/home/dev03/Downloads/create-plan-total-master/novos-reg/minha_planilha.xlsx')
planilha_base = pd.read_excel('/home/dev03/Downloads/create-plan-total-master/novos-reg/dados_total_cartao_concatenado.xlsx')

novos_registros = planilha_base.loc[~planilha_base['id_sasi'].isin(minha_planilha['id_sasi'])].reset_index(drop=True)

minha_planilha = pd.concat([minha_planilha, novos_registros])

minha_planilha.to_excel("/home/dev03/Downloads/create-plan-total-master/novos-reg/dados_completos.xlsx" , index=False)