# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:03:32 2026

@author: jefferson.santos
"""

#%%
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Uniforja | Divisão de Tratamento Térmico",
    page_icon="⚙️",
    layout="wide"
)

# Estilização em CSS para seguir a paleta Uniforja (Azul institucional e cinza industrial)
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
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO COM LOGO INSTITUCIONAL ---
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    # Exibe a logo oficial salva na pasta do projeto
    st.image("logo_uniforja.png", use_container_width=True)

with col_titulo:
    st.title("⚙️ Soluções Avançadas em Tratamento Térmico")
    st.subheader("Engenharia de Superfície e Propriedades Mecânicas de Alta Performance")

st.markdown("---")

# Abas Navegáveis do Site
aba1, aba2, aba3 = st.tabs([
    "🧮 Calculadora de Carbono Equivalente (CE) & D_I", 
    "📚 Fundamentos Metalúrgicos", 
    "🏭 Serviços de Tratamento Térmico & Cotação"
])

# --- ABA 1: CALCULADORA DE CE E DI ---
with aba1:
    st.header("Análise de Temperabilidade (CE - IIW & D_I - ASTM A255)")
    st.write("Insira a composição química do aço (em % de massa) para calcular o Carbono Equivalente e o Diâmetro Crítico Ideal:")

    col_input1, col_input2, col_input3 = st.columns(3)

    with col_input1:
        c = st.number_input("Carbono (C %)", min_value=0.0, max_value=2.0, value=0.40, step=0.01)
        mn = st.number_input("Manganês (Mn %)", min_value=0.0, max_value=3.0, value=0.70, step=0.01)
        si = st.number_input("Silício (Si %)", min_value=0.0, max_value=2.0, value=0.25, step=0.01)

    with col_input2:
        cr = st.number_input("Cromo (Cr %)", min_value=0.0, max_value=5.0, value=0.80, step=0.01)
        mo = st.number_input("Molibdênio (Mo %)", min_value=0.0, max_value=2.0, value=0.20, step=0.01)
        v = st.number_input("Vanádio (V %)", min_value=0.0, max_value=1.0, value=0.00, step=0.01)

    with col_input3:
        ni = st.number_input("Níquel (Ni %)", min_value=0.0, max_value=5.0, value=0.00, step=0.01)
        cu = st.number_input("Cobre (Cu %)", min_value=0.0, max_value=2.0, value=0.00, step=0.01)

    # Cálculo do Carbono Equivalente (IIW)
    ce = c + (mn / 6) + ((cr + mo + v) / 5) + ((ni + cu) / 15)

    # Cálculo do Diâmetro Crítico Ideal (D_I) segundo Grossmann / ASTM A255 (Grão ASTM 7)
    d_base = 0.54 * (c ** 0.5) if c > 0 else 0
    f_mn = 1 + (3.33 * mn)
    f_si = 1 + (0.70 * si)
    f_cr = 1 + (2.16 * cr)
    f_mo = 1 + (3.00 * mo)
    f_ni = 1 + (0.36 * ni)
    f_cu = 1 + (0.36 * cu)

    di_pol = d_base * f_mn * f_si * f_cr * f_mo * f_ni * f_cu  # polegadas
    di_mm = di_pol * 25.4  # mm

    st.markdown("---")
    st.markdown("### Resultado da Avaliação Técnica")
    
    col_res1, col_res2 = st.columns([1, 2])
    
    with col_res1:
        st.metric(label="Carbono Equivalente (CE - IIW)", value=f"{ce:.3f}%")
        st.metric(label="Diâmetro Crítico Ideal (D_I)", value=f"{di_mm:.1f} mm", delta=f"{di_pol:.2f} pol")

    with col_res2:
        if ce < 0.35:
            st.info(
                "🟢 **Baixa Temperabilidade (CE < 0,35%)**\n\n"
                f"* **Diâmetro Crítico Ideal ($D_I$):** ~{di_mm:.1f} mm.\n"
                "* **Comportamento Térmico:** Formação de martensita limitada a seções finas sob alta severidade de resfriamento (água/polímero).\n"
                "* **Soldabilidade:** Excelente."
            )
        elif 0.35 <= ce < 0.45:
            st.success(
                "🟡 **Moderada Temperabilidade (0,35% ≤ CE < 0,45%)**\n\n"
                f"* **Diâmetro Crítico Ideal ($D_I$):** ~{di_mm:.1f} mm.\n"
                "* **Comportamento Térmico:** Excelente resposta a Têmpera e Revenido (Q&T) para peças cilíndricas de médio porte até o diâmetro calculado.\n"
                "* **Cuidados:** Baixo/Moderado risco de trincas."
            )
        elif 0.45 <= ce < 0.60:
            st.warning(
                "🟠 **Alta Temperabilidade (0,45% ≤ CE < 0,60%)**\n\n"
                f"* **Diâmetro Crítico Ideal ($D_I$):** ~{di_mm:.1f} mm.\n"
                "* **Comportamento Térmico:** Alta profundidade de temperabilidade. Exige resfriamento em óleo para evitar distorções ou trincas de têmpera.\n"
                "* **Cuidados:** Necessário pré-aquecimento em etapas de soldagem."
            )
        else:
            st.error(
                "🔴 **Muito Alta Temperabilidade (CE ≥ 0,60%)**\n\n"
                f"* **Diâmetro Crítico Ideal ($D_I$):** ~{di_mm:.1f} mm.\n"
                "* **Comportamento Térmico:** Núcleo temperado em seções robustas. Exige têmpera em óleo aquecido, martêmpera ou resfriamento escalonado.\n"
                "* **Cuidados:** Elevado risco de trincamento e empenamento. Exige alívio de tensões/revenimento imediato."
            )

# --- ABA 2: TEORIA E CONCEITOS ---
with aba2:
    st.header("Tratamento Térmico de Aços")
    st.write(
        "O tratamento térmico é a combinação de operações de aquecimento e resfriamento no estado sólido, "
        "visando conferir às ligas metálicas características específicas de dureza, tenacidade e resistência mecânica."
    )
    
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
        ### Parâmetros Controlados
        * **Taxa de Resfriamento:** Determina as microestruturas formadas (Ferrita, Perlita, Bainita ou Martensita).
        * **Tempo de Encharque:** Garante a homogeneização da temperatura e dissolução total dos carbonetos no núcleo.
        * **Atmosfera Controlada:** Previne a descarbonetação e oxidação superficial durante os ciclos.
        """)

# --- ABA 3: SERVIÇOS UNIFORJA E COTAÇÃO ---
with aba3:
    col_img_forno, col_info_forno = st.columns([1.2, 1.8])

    with col_img_forno:
        # Exibe a imagem local do forno
        st.image("forno.png", caption="Fornos operacionais Uniforja", use_container_width=True)

    with col_info_forno:
        st.markdown("### TRATAMENTO TÉRMICO UNIFORJA")
        st.write(
            "A **UNIFORJA** possui fornos para Tratamento Térmico homologados conforme as normas "
            "**API-6A** e **AMS-2750**, atendendo às mais diversas especificações e demandas do mercado:"
        )
        st.markdown("""
        * **Recozimento (Pleno, Isotérmico e Subcrítico)**
        * **Normalização**
        * **Têmpera e Revenido (Q&T)**
        * **Solubilização e Envelhecimento**
        * **Alívio de Tensões**
        * **Coalescimento e Esferoidização**
        * **Ciclos Especiais (sob consulta)**
        """)

    st.markdown("---")

    # Formulário de Cotação
    st.subheader("Solicite uma Cotação ou Análise Técnica")
    
    with st.form("form_orcamento_uniforja"):
        col_f1, col_f2 = st.columns(2)
        
        with col_f1:
            nome = st.text_input("Nome do Solicitante *")
            empresa = st.text_input("Empresa / Razão Social *")
            email = st.text_input("E-mail Corporativo *")
            telefone = st.text_input("Telefone / WhatsApp com DDD *")

        with col_f2:
            servico_desejado = st.selectbox(
                "Tratamento Térmico Desejado *",
                [
                    "Têmpera e Revenido (Q&T)",
                    "Normalização",
                    "Recozimento Pleno / Isotérmico",
                    "Solubilização de Inoxidáveis",
                    "Alívio de Tensões",
                    "Outros / Consultar Engenharia"
                ]
            )
            liga_material = st.text_input("Liga do Aço (ex: SAE 4140, SAE 8620, F22, F51) *")
            peso_lote = st.text_input("Peso Estimado do Lote / Peça (kg ou toneladas)")

        mensagem = st.text_area(
            "Detalhamento Técnico (Dimensões das peças, Dureza Alvo desejada em HRC/HBW ou norma aplicável)"
        )
        
        submitted = st.form_submit_button("Enviar Solicitação de Cotação")
        
        if submitted:
            if not nome or not email or not empresa or not liga_material:
                st.warning("⚠️ Por favor, preencha todos os campos obrigatórios marcados com (*).")
            else:
                st.success(
                    f"✅ **Obrigado, {nome}!** Sua solicitação para o tratamento de **{servico_desejado}** "
                    f"na liga **{liga_material}** foi enviada à equipe de engenharia Uniforja."
                )
#%%