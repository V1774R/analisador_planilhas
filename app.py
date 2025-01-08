import pandas as pd
import streamlit as st

caminho = '21_12_2024.xlsx'

df = pd.read_excel(caminho, skiprows=4)

planilha = df.values.tolist()
autorizados = []
naoautorizados = []
pendentes = []

st.title('PATRULHA ANALÍTICA GCMR')
st.write('##### Análise de planilhas da escala extraordinária.')

for i, linha in enumerate(planilha):
    matricula = linha[4]
    nome = linha[5]
    horario = linha[7]
    dia = linha[6]
    pagar = linha[10]
    falta = linha[11]

    if not pd.isna(nome):
        if pagar == True:
            if not linha in autorizados:
                autorizados.append(linha)
        elif falta == True:
            if not linha in naoautorizados:
                naoautorizados.append(linha)
        elif pagar == False and falta == False:
            if not linha in pendentes:
                pendentes.append(linha)
        else:
            print('Erro inesperado.')
    else:        
        print('')

st.write('<br><br>', unsafe_allow_html=True)  
if st.checkbox('Exibir autorizados para pagamento.', value=False):
    st.write(f'## AUTORIZADOS PARA PAGAMENTO - {len(autorizados)}')
    if len(autorizados) > 0:
        for autorizado in autorizados:
                horario = autorizado[6].strftime("%d/%m/%Y %H:%M:%S")
                st.write(f"<p style='color: #228B22;'> [{autorizado[4]}] {autorizado[5]}, DIA: {horario[:-9]}, HORÁRIO: {autorizado[7]} </p>", unsafe_allow_html=True)


if st.checkbox('Exibir não autorizados para pagamento.', value=False):
    st.write(f'## NÃO AUTORIZADOS PARA PAGAMENTO - {len(naoautorizados)}')
    if len(naoautorizados) > 0:
        for naoautorizado in naoautorizados:
                horario = naoautorizado[6].strftime("%d/%m/%Y %H:%M:%S")
                st.write(f"<p style='color: #FF0000;'>[{naoautorizado[4]}] {naoautorizado[5]}, DIA: {horario[:-9]}, HORÁRIO: {naoautorizado[7]} </p>", unsafe_allow_html=True)

if st.checkbox('Exibir pendentes para pagamento.', value=False):
    st.write(f'## PENDENTES - {len(pendentes)}')
    if len(pendentes) > 0:
        for pendente in pendentes:
                horario = pendente[6].strftime("%d/%m/%Y %H:%M:%S")
                st.write(f"<p style='color: #DAA520;'> [{pendente[4]}]  {pendente[5]}, DIA: {horario[:-9]}, HORÁRIO: {pendente[7]} </p>", unsafe_allow_html=True)


st.divider()
totalAgentes = len(autorizados) + len(naoautorizados) + len(pendentes)

st.write(f'## Total de agentes escalados: {totalAgentes}')
st.write(f'<p title="Total de presenças confirmadas após a análise da planilha pelo setor de escalas.">Total de agentes presentes: {len(autorizados)}</p>', unsafe_allow_html=True)
st.write(f'Total de faltas: {len(naoautorizados)}')
st.write(f'Total de pendentes: {len(pendentes)}')

st.divider()
st.write('<p style="font-size: 0.8rem; width: 100%; text-align: center; font-family: sans-serif; font-style: italic;"> DESENVOLVIDO POR GCM. VILLAR e GCM. ERIK LINS <br> @copy 2024 <br> Todos os direitos reservados.</p>', unsafe_allow_html=True)