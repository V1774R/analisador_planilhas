import streamlit as st

def about_page():
    st.title('Sobre o App')

    st.write("""
        
    > #### Como Utilizar
    > - O usuário faz o upload da planilha gerada pelo setor de escalas.
    > - O sistema processa a planilha e gera um resumo automático.
    > - O usuário pode visualizar o resumo na interface do sistema.

    ---    
    > #### IMPORTANTE
    > É **imprescindível** que as planilhas a serem analisadas, sigam o padrão utilizado pelo sistema. [Clique aqui](https://tse3.mm.bing.net/th?id=OIP.PNfvf4nE41zepUac5qdZnAHaEK&rs=1&pid=ImgDetMain) para visualizar o modelo.
    --- 
    >#### Visão Geral
    > Este sistema foi desenvolvido para otimizar a gestão de escalas e melhorar a eficiência na avaliação da presença dos agentes no serviço extra.
    > Através do processamento de planilhas, gera resumo das informações dos agentes. O sistema fornece uma resumo sobre os agentes que:
    > - Compareceram ao serviço extra
    > - Faltaram ao serviço extra
    > - Estão pendentes de avaliação
    --- 
    #### Funcionalidades
    > - **Leitura de Planilha**: O sistema importa a planilha gerada pelo setor de escalas.
    > - **Processamento de Dados**: Os dados da planilha são processados para identificar o status de cada agente.
    > - **Geração de Resumo**: O sistema gera um resumo detalhado do número de agentes que faltaram, compareceram e estão pendentes de avaliação.
    > - **Interface Interativa**: Utiliza Streamlit para uma interface web intuitiva e interativa.
    --- 
    #### Tecnologias Utilizadas
    > - **Linguagem de Programação**: Python
    > - **Bibliotecas**:
    > - `pandas`: Para manipulação e análise de dados
    > - `openpyxl`: Para trabalhar com arquivos Excel
    > - `streamlit`: Para a interface web interativa
    > - **Sistema Operacional**: Compatível com Windows, macOS e Linux
    ---              
    #### Resumo da Análise
    > - **Total de Agentes Escalados**: Exibe o número total de agentes escalados.
    > - **Agentes Presentes**: Exibe o número de agentes que compareceram ao serviço extra.
    > - **Faltas**: Exibe o número de agentes que faltaram ao serviço extra.
    > - **Pendentes**: Exibe o número de agentes que estão pendentes de avaliação.
    --- 
    #### Contato
    > Para mais informações, entre em contato com a equipe de desenvolvimento.       

    <hr>
    <p style="font-size: 0.8rem; width: 100%; text-align: center; font-family: sans-serif; font-style: italic;"> DESENVOLVIDO POR GCM. VILLAR e GCM. ERIK LINS <br> @copy 2024 <br> Todos os direitos reservados.</p>               
""", unsafe_allow_html=True)

