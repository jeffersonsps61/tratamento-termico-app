# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:03:32 2026

@author: jefferson.santos
"""

#%%
import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="Uniforja | Divisão de Tratamento Térmico",
    page_icon="⚙️",
    layout="wide"
)

# 2. Estilização CSS
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

# 3. Cabeçalho com Logo
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    st.image("logo_uniforja.png", use_container_width=True)

with col_titulo:
    st.title("⚙️ Soluções Avançadas em Tratamento Térmico")
    st.subheader("Engenharia de Superfície e Propriedades Mecânicas de Alta Performance")

st.markdown("---")

# 4. Definição das Abas Principais (Declaração de aba1, aba2, aba3)
aba1, aba2, aba3 = st.tabs([
    "🧮 Central de Cálculos & Conversões", 
    "📚 Fundamentos Metalúrgicos", 
    "🏭 Serviços Uniforja & Cotação"
])

# --- ABA 1: CALCULADORAS E FERRAMENTAS ---
with aba1:
    st.header("Central de Cálculos de Engenharia e Conversões")
    st.write("Ferramentas operacionais para especificação de tratamento térmico, dimensionamento e conversões mecânicas.")

    # Sub-abas internas
    sub1, sub2, sub3, sub4 = st.tabs([
        "🧮 Carbono Equivalente (CE)", 
        "🔄 Conversão de Dureza (ASTM E140)", 
        "📐 Conversor de Tensões e Impacto", 
        "⚖️ Calculadora de Peso e Massa"
    ])

    # 1. CARBONO EQUIVALENTE
    with sub1:
        st.subheader("Cálculo de Carbono Equivalente (CE - IIW)")
        
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            c = st.number_input("Carbono (C %)", min_value=0.0, max_value=2.0, value=0.40, step=0.01)
            mn = st.number_input("Manganês (Mn %)", min_value=0.0, max_value=3.0, value=0.70, step=0.01)
        with col_c2:
            cr = st.number_input("Cromo (Cr %)", min_value=0.0, max_value=5.0, value=0.80, step=0.01)
            mo = st.number_input("Molibdênio (Mo %)", min_value=0.0, max_value=2.0, value=0.20, step=0.01)
            v = st.number_input("Vanádio (V %)", min_value=0.0, max_value=1.0, value=0.00, step=0.01)
        with col_c3:
            ni = st.number_input("Níquel (Ni %)", min_value=0.0, max_value=5.0, value=0.00, step=0.01)
            cu = st.number_input("Cobre (Cu %)", min_value=0.0, max_value=2.0, value=0.00, step=0.01)

        ce = c + (mn / 6) + ((cr + mo + v) / 5) + ((ni + cu) / 15)

        st.metric(label="Carbono Equivalente (CE - IIW)", value=f"{ce:.3f}%")
        
        st.markdown("""
        **Importância do CE no Tratamento Térmico:**
        O Carbono Equivalente sintetiza o efeito combinado dos elementos de liga na temperabilidade do aço. Valores elevados de $CE$ indicam retardo na transformação austeno-ferrítica, facilitando a formação de martensita profunda, porém aumentando o risco de trincas de têmpera e exigindo meios de resfriamento moderados (óleo/polímero) e rigoroso controle de alívio de tensões.
        """)

    # 2. CONVERSÃO DE DUREZA
    with sub2:
        st.subheader("Conversão de Dureza (Aços Não Ligados e Ligas - ASTM E140)")
        
        tabela_dureza = [
            {"HRC": 68, "HBW": 940, "HV": 940},
            {"HRC": 60, "HBW": 654, "HV": 697},
            {"HRC": 55, "HBW": 560, "HV": 595},
            {"HRC": 50, "HBW": 481, "HV": 513},
            {"HRC": 45, "HBW": 421, "HV": 446},
            {"HRC": 40, "HBW": 371, "HV": 392},
            {"HRC": 35, "HBW": 327, "HV": 345},
            {"HRC": 30, "HBW": 286, "HV": 302},
            {"HRC": 25, "HBW": 253, "HV": 266},
            {"HRC": 20, "HBW": 226, "HV": 238}
        ]

        val_hrc = st.slider("Selecione a Dureza em Rockwell C (HRC):", min_value=20, max_value=68, value=40, step=1)
        item_proximo = min(tabela_dureza, key=lambda x: abs(x["HRC"] - val_hrc))
        
        col_d1, col_d2, col_d3 = st.columns(3)
        col_d1.metric("Rockwell C (HRC)", f"{val_hrc}")
        col_d2.metric("Brinell (HBW - 3000 kgf)", f"~{item_proximo['HBW']}")
        col_d3.metric("Vickers (HV)", f"~{item_proximo['HV']}")

    # 3. CONVERSOR DE TENSÕES E IMPACTO
    with sub3:
        st.subheader("Conversor de Unidades de Resistência e Impacto")
        col_t1, col_t2 = st.columns(2)
        
        with col_t1:
            st.markdown("#### Tensões (Mecânica de Tração)")
            valor_tensao = st.number_input("Valor de Tensão de Entrada:", value=100.0, step=10.0)
            unid_tensao = st.selectbox("Unidade de Entrada:", ["ksi", "Psi", "Mpa", "Kgf/mm²"])
            
            if unid_tensao == "ksi":
                mpa = valor_tensao * 6.89476
            elif unid_tensao == "Psi":
                mpa = valor_tensao * 0.00689476
            elif unid_tensao == "Kgf/mm²":
                mpa = valor_tensao * 9.80665
            else:
                mpa = valor_tensao

            st.write(f"**MPa:** {mpa:.2f}")
            st.write(f"**ksi:** {mpa / 6.89476:.2f}")
            st.write(f"**Psi:** {mpa / 0.00689476:.1f}")
            st.write(f"**Kgf/mm²:** {mpa / 9.80665:.2f}")

        with col_t2:
            st.markdown("#### Ensaios de Impacto (Charpy)")
            valor_impacto = st.number_input("Valor de Energia de Entrada:", value=27.0, step=1.0)
            unid_impacto = st.selectbox("Unidade de Entrada:", ["Joule (J)", "Kgf x m", "Ft.lbf"])
            
            if unid_impacto == "Joule (J)":
                j = valor_impacto
            elif unid_impacto == "Kgf x m":
                j = valor_impacto * 9.80665
            else:
                j = valor_impacto * 1.35582

            st.write(f"**Joule (J):** {j:.1f}")
            st.write(f"**Kgf x m:** {j / 9.80665:.2f}")
            st.write(f"**Ft.lbf:** {j / 1.35582:.1f}")

    # 4. CALCULADORA DE PESO
    with sub4:
        st.subheader("Estimativa de Massa e Peso do Lote")
        geometria = st.selectbox("Formato da Peça:", ["Cilindro / Barra Redonda", "Bloco Retangular / Chapa", "Tubo / Anel"])
        densidade = st.number_input("Densidade do Material (g/cm³):", value=7.85, step=0.01)
        
        peso_unitario = 0.0

        if geometria == "Cilindro / Barra Redonda":
            diametro = st.number_input("Diâmetro (mm):", value=100.0, step=5.0)
            comprimento = st.number_input("Comprimento (mm):", value=500.0, step=10.0)
            volume = (3.14159 * ((diametro/10/2)**2) * (comprimento/10))
            peso_unitario = (volume * densidade) / 1000

        elif geometria == "Bloco Retangular / Chapa":
            largura = st.number_input("Largura (mm):", value=100.0, step=5.0)
            espessura = st.number_input("Espessura (mm):", value=50.0, step=5.0)
            comprimento = st.number_input("Comprimento (mm):", value=500.0, step=10.0)
            volume = (largura/10) * (espessura/10) * (comprimento/10)
            peso_unitario = (volume * densidade) / 1000

        elif geometria == "Tubo / Anel":
            d_ext = st.number_input("Diâmetro Externo (mm):", value=200.0, step=5.0)
            d_int = st.number_input("Diâmetro Interno (mm):", value=100.0, step=5.0)
            altura = st.number_input("Altura / Comprimento (mm):", value=100.0, step=5.0)
            v_ext = 3.14159 * ((d_ext/10/2)**2) * (altura/10)
            v_int = 3.14159 * ((d_int/10/2)**2) * (altura/10)
            volume = v_ext - v_int
            peso_unitario = (volume * densidade) / 1000

        qtd_pecas = st.number_input("Quantidade de Peças no Lote:", min_value=1, value=1, step=1)
        peso_total = peso_unitario * qtd_pecas

        col_p1, col_p2 = st.columns(2)
        col_p1.metric("Peso Unitário Estimado", f"{peso_unitario:.2f} kg")
        col_p2.metric("Peso Total do Lote", f"{peso_total:.2f} kg", f"{peso_total/1000:.3f} t")

# --- ABA 2: FUNDAMENTOS ---
with aba2:
    st.header("Tratamento Térmico de Aços")
    st.write("Operações térmicas no estado sólido para ajuste de microestrutura e propriedades mecânicas.")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("""
        ### Etapas Fundamentais
        1. **Austenitização:** Aquecimento acima da linha crítica.
        2. **Têmpera:** Resfriamento rápido para formação de martensita.
        3. **Revenido:** Alívio de tensões e ajuste de tenacidade.
        """)
    with col_t2:
        st.markdown("""
        ### Parâmetros Controlados
        * **Taxa de Resfriamento**
        * **Tempo de Encharque**
        * **Atmosfera de Aquecimento**
        """)

# --- ABA 3: SERVIÇOS E COTAÇÃO ---
with aba3:
    col_img_forno, col_info_forno = st.columns([1.2, 1.8])

    with col_img_forno:
        st.image("forno.png", caption="Fornos operacionais Uniforja", use_container_width=True)

    with col_info_forno:
        st.markdown("### TRATAMENTO TÉRMICO UNIFORJA")
        st.write("Fornos homologados conforme as normas **API-6A** e **AMS-2750**.")
        st.markdown("""
        * **Recozimento (Pleno, Isotérmico e Subcrítico)**
        * **Normalização**
        * **Têmpera e Revenido (Q&T)**
        * **Solubilização e Envelhecimento**
        * **Alívio de Tensões**
        """)

    st.markdown("---")
    st.subheader("Solicite uma Cotação Técnica")
    
    with st.form("form_orcamento_uniforja"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            nome = st.text_input("Nome do Solicitante *")
            empresa = st.text_input("Empresa *")
            email = st.text_input("E-mail Corporativo *")
        with col_f2:
            servico_desejado = st.selectbox("Tratamento Térmico *", ["Têmpera e Revenido (Q&T)", "Normalização", "Recozimento", "Solubilização", "Alívio de Tensões"])
            liga_material = st.text_input("Liga do Aço *")

        mensagem = st.text_area("Detalhamento Técnico")
        submitted = st.form_submit_button("Enviar Cotação")
        
        if submitted:
            if not nome or not email or not empresa or not liga_material:
                st.warning("⚠️ Preencha os campos obrigatórios (*).")
            else:
                st.success(f"✅ Solicitação enviada com sucesso!")
#%%