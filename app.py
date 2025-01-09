import pandas as pd
import streamlit as st
import os
from funcoes import funcoes
import about
import plotly.express as px

st.set_page_config(initial_sidebar_state='expanded')




def home_page():
    msg = ''
    df = ''

    if os.path.isfile("uploads/planilha.xlsx"):
        os.remove("uploads/planilha.xlsx")


    st.title('PATRULHA ANALÍTICA GCMR')
    st.write(' Análise de planilhas da escala extraordinária.')

    st.divider()  


    # Caso a planilha venha a partir de uma seleção

    arquivo = st.file_uploader('Selecione um arquivo.')

    if arquivo is not None:
        st.write(f"<p style='width: 100vw; margin-bottom: -30px;'>{funcoes.fazerUpload(arquivo)}</p>", unsafe_allow_html=True)

    st.divider()

    if os.path.isfile("uploads/planilha.xlsx"):
        df = pd.read_excel('uploads/planilha.xlsx', skiprows=4)
        planilha = df.values.tolist()
        autorizados = []
        naoautorizados = []
        pendentes = []
        total_agentes = []
        total_agentes_faltosos = []

        for i, linha in enumerate(planilha):
            matricula = linha[4]
            nome = linha[5]
            horario = linha[7]
            dia = linha[6]
            pagar = linha[10]
            falta = linha[11]

            if not pd.isna(nome):
                # Obter o total de agentes (sem repetir)
                agente = {
                    "graduacao": linha[3],
                    "nome": nome,
                    "matricula": matricula
                }
                if agente not in total_agentes:
                    total_agentes.append(agente)
                
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

        # gerar os agentes que faltaram
        for agente in naoautorizados:
            agenteString = f'{[agente[4]]} {agente[3]} {agente[5]} - FALTA'
            if agenteString not in total_agentes_faltosos:
                total_agentes_faltosos.append(agenteString)

        st.write('### Opções de exibição')
        st.write('<br>', unsafe_allow_html=True)  
        if st.checkbox('Exibir quotas autorizadas para pagamento.', value=False):
            st.write(f'## QUOTAS AUTORIZADAS PARA PAGAMENTO - {len(autorizados)}')
            if len(autorizados) > 0:
                for autorizado in autorizados:
                        horario = autorizado[6].strftime("%d/%m/%Y %H:%M:%S")
                        st.write(f"<p style='color: #228B22;'> [{autorizado[4]}] {autorizado[3]} {autorizado[5]}, DIA: {horario[:-9]}, HORÁRIO: {autorizado[7]} </p>", unsafe_allow_html=True)


        if st.checkbox('Exibir quotas não autorizadas para pagamento.', value=False):
            st.write(f'## QUOTAS NÃO AUTORIZADAS PARA PAGAMENTO - {len(naoautorizados)}')
            if len(naoautorizados) > 0:
                for naoautorizado in naoautorizados:
                        horario = naoautorizado[6].strftime("%d/%m/%Y %H:%M:%S")
                        st.write(f"<p style='color: #FF0000;'>[{naoautorizado[4]}] {naoautorizado[5]}, DIA: {horario[:-9]}, HORÁRIO: {naoautorizado[7]} </p>", unsafe_allow_html=True)

        if st.checkbox('Exibir quotas pendentes de avaliação.', value=False):
            st.write(f'## QUOTAS PENDENTES - {len(pendentes)}')
            if len(pendentes) > 0:
                for pendente in pendentes:
                        horario = pendente[6].strftime("%d/%m/%Y %H:%M:%S")
                        st.write(f"<p style='color: #DAA520;'> [{pendente[4]}]  {pendente[5]}, DIA: {horario[:-9]}, HORÁRIO: {pendente[7]} </p>", unsafe_allow_html=True)


        st.divider()
        totalAgentes = len(autorizados) + len(naoautorizados) + len(pendentes)

        st.write('### Resumo da análise de quotas')

        # Criar um gráfico de barras com Plotly 
        status_contagem = { "Presenças": len(autorizados), "Faltas": len(naoautorizados), "Pendências de avaliação": len(pendentes), "Número de agentes": len(total_agentes), "Número de Faltosos": len(total_agentes_faltosos) } 
        fig = px.bar(x=status_contagem.keys(), y=status_contagem.values(), labels={'x': '', 'y': 'Número de Escalações por Quota de Extra'})
        st.plotly_chart(fig)

        st.write(f'Total de escalações por quota: {totalAgentes}')
        st.write(f'<p>Total de presenças confirmadas por quota: {len(autorizados)}</p>', unsafe_allow_html=True)
        st.write(f'Total de faltas confirmadas por quota: {len(naoautorizados)}')
        st.write(f'Total de pendências de avaliação: {len(pendentes)}')
        st.write(f'Total de agentes utilizados nesta escala: {len(total_agentes)}')
        st.write(f'Total de agentes que faltaram o serviço extra: {len(total_agentes_faltosos)}')
        st.divider()    

    st.write('<p style="font-size: 0.8rem; width: 100%; text-align: center; font-family: sans-serif; font-style: italic;"> DESENVOLVIDO POR GCM. VILLAR e GCM. ERIK LINS <br> @copy 2024 <br> Todos os direitos reservados.</p>', unsafe_allow_html=True)    
    

if pagina == "Inicio":
    home_page()
elif pagina == "Sobre":
    about.about_page()
