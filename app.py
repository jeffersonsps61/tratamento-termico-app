# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:03:32 2026

@author: jefferson.santos
"""

#%%
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Divisão de Tratamento Térmico | Calculadora CE",
    page_icon="⚙️",
    layout="wide"
)

# Estilização em CSS para seguir a paleta Uniforja (Azul escuro e cinza industrial)
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .stButton>button {
        background-color: #003366;
        color: white;
        border-radius: 5px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #002244;
        color: #ffffff;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
        border-left: 5px solid #003366;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho / Hero Section
st.title("⚙️ Soluções Avançadas em Tratamento Térmico")
st.subheader("Engenharia de Superfície e Propriedades Mecânicas de Alta Performance")
st.markdown("---")

# Abas do Site
aba1, aba2, aba3 = st.tabs(["🧮 Calculadora de Carbono Equivalente", "📚 Fundamentos de Tratamento Térmico", "✉️ Solicitar Orçamento"])

# --- ABA 1: CALCULADORA ---
with aba1:
    st.header("Calculadora de Carbono Equivalente (CE - Formulação IIW)")
    st.write("Insira a composição química do aço (em % de massa) para avaliar a temperabilidade e os cuidados no reprocessamento térmico:")

    col_input1, col_input2, col_input3 = st.columns(3)

    with col_input1:
        c = st.number_input("Carbono (C %)", min_value=0.0, max_value=2.0, value=0.40, step=0.01)
        mn = st.number_input("Manganês (Mn %)", min_value=0.0, max_value=3.0, value=0.70, step=0.01)

    with col_input2:
        cr = st.number_input("Cromo (Cr %)", min_value=0.0, max_value=5.0, value=0.80, step=0.01)
        mo = st.number_input("Molibdênio (Mo %)", min_value=0.0, max_value=2.0, value=0.20, step=0.01)
        v = st.number_input("Vanádio (V %)", min_value=0.0, max_value=1.0, value=0.00, step=0.01)

    with col_input3:
        ni = st.number_input("Níquel (Ni %)", min_value=0.0, max_value=5.0, value=0.00, step=0.01)
        cu = st.number_input("Cobre (Cu %)", min_value=0.0, max_value=2.0, value=0.00, step=0.01)

    # Cálculo do CE
    ce = c + (mn / 6) + ((cr + mo + v) / 5) + ((ni + cu) / 15)

    st.markdown("---")
    st.markdown("### Resultado da Análise Técnica")
    
    col_res1, col_res2 = st.columns([1, 2])
    
    with col_res1:
        st.metric(label="Valor de Carbono Equivalente (CE)", value=f"{ce:.3f}%")

    with col_res2:
        if ce < 0.35:
            st.success("🟢 **Baixa Temperabilidade / Excelente Soldabilidade:** Aço com baixo risco de trincamento. Têmpera exige meios de resfriamento severos para peças espessas.")
        elif 0.35 <= ce <= 0.45:
            st.warning("🟡 **Média Temperabilidade:** Exige controle moderado de resfriamento. Recomendada atenção no alívio de tensões e planejamento de revenimento.")
        else:
            st.error("🔴 **Alta Temperabilidade / Risco Elevado de Trincas:** Formação facilitada de martensita. Requer rigoroso controle Térmico, pré-aquecimento e escolha adequada do meio quenchar (óleo/polímero).")

    st.markdown("""
    #### Importância do CE no Tratamento Térmico
    O **Carbono Equivalente** correlaciona a composição química à resposta do material ao ciclo térmico. Aços com elevado $CE$ apresentam alta temperabilidade, o que significa que transformam em martensita até o núcleo em peças de maior diâmetro. No entanto, exigem controle térmico preciso para prevenir distorções e trincas de têmpera.
    """)

# --- ABA 2: TEORIA E CONCEITOS ---
with aba2:
    st.header("Tratamento Térmico de Aços")
    st.write("""
    O tratamento térmico é a combinação de operações de aquecimento e resfriamento no estado sólido, visando conferir às ligas metálicas características específicas de dureza, tenacidade e resistência mecânica.
    """)
    
    col_t1, col_t2 = st.columns(2)
    
    with col_t1:
        st.markdown("""
        ### Etapas Fundamentais
        1. **Austenitização:** Aquecimento acima da temperatura crítica para solubilização do carbono na matriz $\gamma$.
        2. **Têmpera:** Resfriamento contínuo em taxa superior à taxa crítica para obtenção de estrutura martensítica.
        3. **Revenido:** Tratamento térmico subcrítico para alívio de tensões e ajuste do compromisso Dureza x Tenacidade.
        """)
        
    with col_t2:
        st.markdown("""
        ### Processos Oferecidos
        * **Têmpera e Revenido (Q&T)**
        * **Normalização e Recozimento Isotérmico**
        * **Solubilização de Inoxidáveis**
        * **Alívio de Tensões**
        """)

# --- ABA 3: CAPTAÇÃO DE LEADS ---
with aba3:
    st.header("Fale com Nossos Engenheiros de Processo")
    st.write("Envie os dados de sua peça ou lote para uma avaliação técnica de tratamento térmico.")

    with st.form("form_contato"):
        nome = st.text_input("Nome Completo")
        empresa = st.text_input("Empresa")
        email = st.text_input("E-mail Corporativo")
        telefone = st.text_input("Telefone / WhatsApp")
        liga = st.text_input("Material / Liga do Aço (ex: SAE 4140, SAE 8620)")
        mensagem = st.text_area("Descrição da Necessidade (Dimensões, Dureza Alvo, Tratamento Desejado)")
        
        submitted = st.form_submit_button("Solicitar Análise Técnica")
        if submitted:
            st.success("Obrigado pelo contato! Nossa equipe de engenharia entrará em contato em breve.")
#%%