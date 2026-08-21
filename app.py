# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:03:32 2026

@author: jefferson.santos
"""

#%%
import streamlit as st

# ==========================================================
# 1. Configuração da Página
# ==========================================================
st.set_page_config(
    page_title="Uniforja | Divisão de Tratamento Térmico",
    page_icon="⚙️",
    layout="wide"
)

# ==========================================================
# 2. Estilização CSS Personalizada
# ==========================================================
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
    .calc-box {
        background-color: #ffffff;
        border-left: 5px solid #003366;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================================
# 3. Cabeçalho Institucional
# ==========================================================
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    try:
        st.image("logo_uniforja.png", use_container_width=True)
    except Exception:
        st.markdown("### ⚙️ **UNIFORJA**\n*Divisão Térmica*")

with col_titulo:
    st.title("⚙️ Soluções Avançadas em Tratamento Térmico")
    st.subheader("Engenharia de Superfície e Propriedades Mecânicas de Alta Performance")

st.markdown("---")

# ==========================================================
# 4. Definição das Abas Principais
# ==========================================================
aba1, aba2, aba3 = st.tabs([
    "🧮 Central de Cálculos & Conversões", 
    "📚 Fundamentos Metalúrgicos (Fe-Fe₃C)", 
    "🏭 Serviços Uniforja & Cotação"
])

# ==========================================================
# Tabela Oficial ASTM E140 (Aços Carbono e Baixa Liga)
# ==========================================================
TABELA_ASTM_E140 = [
    (20.0, 226, 238), (21.0, 231, 243), (22.0, 237, 248), (23.0, 243, 254), (24.0, 248, 260),
    (25.0, 253, 266), (26.0, 259, 273), (27.0, 264, 279), (28.0, 271, 286), (29.0, 278, 294),
    (30.0, 286, 302), (31.0, 294, 311), (32.0, 301, 318), (33.0, 311, 327), (34.0, 319, 336),
    (35.0, 327, 345), (36.0, 336, 354), (37.0, 344, 363), (38.0, 353, 373), (39.0, 362, 382),
    (40.0, 371, 392), (41.0, 381, 402), (42.0, 390, 412), (43.0, 400, 423), (44.0, 410, 434),
    (45.0, 421, 446), (46.0, 432, 458), (47.0, 443, 470), (48.0, 455, 483), (49.0, 467, 497),
    (50.0, 481, 513), (51.0, 496, 528), (52.0, 512, 545), (53.0, 528, 562), (54.0, 543, 578),
    (55.0, 560, 595), (56.0, 577, 613), (57.0, 595, 633), (58.0, 614, 653), (59.0, 634, 675),
    (60.0, 654, 697), (61.0, 674, 720), (62.0, 697, 746), (63.0, 720, 772), (64.0, 745, 800),
    (65.0, 772, 829), (66.0, 800, 860), (67.0, 829, 892), (68.0, 861, 940)
]

def converter_hrc_para_hbw(val_hrc):
    """Interpolação linear precisa para HRC -> HBW conforme ASTM E140"""
    if val_hrc < 20.0 or val_hrc > 68.0:
        return None, None
    for i in range(len(TABELA_ASTM_E140) - 1):
        hrc_a, hbw_a, hv_a = TABELA_ASTM_E140[i]
        hrc_b, hbw_b, hv_b = TABELA_ASTM_E140[i+1]
        if hrc_a <= val_hrc <= hrc_b:
            fator = (val_hrc - hrc_a) / (hrc_b - hrc_a)
            hbw_calc = hbw_a + fator * (hbw_b - hbw_a)
            hv_calc = hv_a + fator * (hv_b - hv_a)
            return round(hbw_calc, 1), round(hv_calc, 1)
    return None, None

def converter_hbw_para_hrc(val_hbw):
    """Interpolação linear precisa para HBW -> HRC conforme ASTM E140"""
    hbw_min = TABELA_ASTM_E140[0][1]
    hbw_max = TABELA_ASTM_E140[-1][1]
    if val_hbw < hbw_min or val_hbw > hbw_max:
        return None, None
    for i in range(len(TABELA_ASTM_E140) - 1):
        hrc_a, hbw_a, hv_a = TABELA_ASTM_E140[i]
        hrc_b, hbw_b, hv_b = TABELA_ASTM_E140[i+1]
        if hbw_a <= val_hbw <= hbw_b:
            fator = (val_hbw - hbw_a) / (hbw_b - hbw_a)
            hrc_calc = hrc_a + fator * (hrc_b - hrc_a)
            hv_calc = hv_a + fator * (hv_b - hv_a)
            return round(hrc_calc, 1), round(hv_calc, 1)
    return None, None


# ==========================================================
# --- ABA 1: CENTRAL DE CÁLCULOS E CONVERSÕES ---
# ==========================================================
with aba1:
    st.header("Central de Cálculos de Engenharia e Conversões")
    st.write("Ferramentas operacionais para especificação de tratamento térmico, dimensionamento e conversões mecânicas.")

    sub1, sub2, sub3, sub4, sub5 = st.tabs([
        "🧮 Carbono Equivalente (CE)", 
        "🔄 Conversão de Dureza HRC ⇄ HBW", 
        "💪 Relação Dureza x Resistência",
        "📐 Conversor de Tensões e Impacto", 
        "⚖️ Calculadora de Peso e Massa"
    ])

    # ------------------------------------------------------
    # 1.1 Carbono Equivalente
    # ------------------------------------------------------
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
        **Por que o CE é Vital no Tratamento Térmico?**
        O Carbono Equivalente sintetiza o efeito combinado dos elementos de liga na temperabilidade do aço. Valores elevados de $CE$ indicam retardo na transformação austeno-ferrítica, facilitando a formação de martensita profunda, porém aumentando o risco de trincas de têmpera e exigindo meios de resfriamento moderados (óleo/polímero) e rigoroso controle de alívio de tensões.
        """)

    # ------------------------------------------------------
    # 1.2 Conversão de Dureza HRC <-> HBW (ASTM E140)
    # ------------------------------------------------------
    with sub2:
        st.subheader("Calculadora de Conversão Direta de Dureza (ASTM E140)")
        st.write("Escolha o sentido da conversão, insira o valor desejado e obtenha a equivalência exata calculada por interpolação normativa.")

        sentido = st.radio(
            "Selecione o Sentido da Conversão:",
            ["Rockwell C (HRC)  ➔  Brinell (HBW)", "Brinell (HBW)  ➔  Rockwell C (HRC)"],
            horizontal=True
        )

        col_conv1, col_conv2 = st.columns(2)

        if "HRC" in sentido.split("➔")[0]:
            with col_conv1:
                val_input = st.number_input(
                    "Digite a Dureza em Rockwell C (HRC):",
                    min_value=20.0,
                    max_value=68.0,
                    value=40.0,
                    step=0.5
                )
                
            res_hbw, res_hv = converter_hrc_para_hbw(val_input)

            with col_conv2:
                if res_hbw:
                    st.metric("Dureza Brinell Calculada (HBW)", f"{res_hbw:.1f} HBW")
                    st.caption(f"💡 Equivalência estimada em Vickers: **~{res_hv:.1f} HV**")
                else:
                    st.error("Valor fora da faixa permitida pela norma ASTM E140 (20.0 a 68.0 HRC).")

        else:
            with col_conv1:
                val_input = st.number_input(
                    "Digite a Dureza em Brinell (HBW - 3000 kgf):",
                    min_value=226.0,
                    max_value=861.0,
                    value=371.0,
                    step=1.0
                )

            res_hrc, res_hv = converter_hbw_para_hrc(val_input)

            with col_conv2:
                if res_hrc:
                    st.metric("Dureza Rockwell C Calculada (HRC)", f"{res_hrc:.1f} HRC")
                    st.caption(f"💡 Equivalência estimada em Vickers: **~{res_hv:.1f} HV**")
                else:
                    st.error("Valor fora da faixa permitida pela norma ASTM E140 (226 a 861 HBW).")

        st.markdown("---")
        st.markdown("#### 🔍 Tabela Simplificada de Referência Rápida (ASTM E140 - Aços Carbono e Liga)")

        col_t1, col_t2, col_t3 = st.columns(3)
        col_t1.write("**Dureza Rockwell C (HRC)**\n* 20 HRC\n* 30 HRC\n* 40 HRC\n* 50 HRC\n* 60 HRC\n* 65 HRC")
        col_t2.write("**Brinell Equivalente (HBW)**\n* ~226 HBW\n* ~286 HBW\n* ~371 HBW\n* ~481 HBW\n* ~654 HBW\n* ~772 HBW")
        col_t3.write("**Vickers Equivalente (HV)**\n* ~238 HV\n* ~302 HV\n* ~392 HV\n* ~513 HV\n* ~697 HV\n* ~829 HV")

    # ------------------------------------------------------
    # 1.3 Estimativa de Resistência à Tração
    # ------------------------------------------------------
    with sub3:
        st.subheader("Estimativa Teórica da Resistência à Tração (LR)")
        st.write("Estime o Limite de Resistência à Tração aproximado a partir da Dureza Brinell (HBW):")

        col_r1, col_r2 = st.columns(2)

        with col_r1:
            hbw_in = st.number_input("Dureza Brinell (HBW):", min_value=100, max_value=750, value=300, step=5)
            familia_aco = st.selectbox(
                "Família de Liga do Aço:",
                [
                    "Aço ao Carbono / Manganês (Ex: SAE 1030, 1045)",
                    "Aço Liga / Cr-Mo (Ex: SAE 4140, 4340)"
                ]
            )

        with col_r2:
            if "Carbono" in familia_aco:
                fator = 3.53
                fator_kg = 0.35
            else:
                fator = 3.33
                fator_kg = 0.35

            lr_mpa = hbw_in * fator
            lr_kg = hbw_in * fator_kg
            lr_ksi = lr_mpa / 6.89476

            st.metric("Limite de Resistência Estimado (MPa)", f"{lr_mpa:.0f} MPa")
            st.metric("Equivalente em ksi", f"{lr_ksi:.1f} ksi", f"{lr_kg:.0f} kgf/mm²")

        st.info(
            "⚠️ **Nota Técnica:** A correlação entre dureza e limite de resistência à tração é estritamente **teórica e aproximada**. "
            "Valores exatos devem ser validados mediante ensaio destrutivo de tração conforme norma ISO 6892 / ASTM A370."
        )

    # ------------------------------------------------------
    # 1.4 Conversor de Tensões e Impacto
    # ------------------------------------------------------
    with sub4:
        st.subheader("Conversor de Unidades de Resistência e Impacto")
        col_t1, col_t2 = st.columns(2)

        with col_t1:
            st.markdown("#### Tensões (Mecânica de Tração)")
            valor_tensao = st.number_input("Valor de Tensão de Entrada:", value=100.0, step=10.0)
            unid_tensao = st.selectbox("Unidade de Entrada:", ["ksi", "Psi", "MPa", "Kgf/mm²"])

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

    # ------------------------------------------------------
    # 1.5 Calculadora de Peso e Massa
    # ------------------------------------------------------
    with sub5:
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

# ==========================================================
# --- ABA 2: FUNDAMENTOS METALÚRGICOS (DIAGRAMA Fe-Fe3C) ---
# ==========================================================
with aba2:
    st.header("Fundamentos Metalúrgicos: Diagrama Ferro-Carbono (Fe-Fe₃C)")
    st.write(
        "A especificação da temperatura de tratamento térmico é rigorosamente balizada pelas "
        "linhas críticas de transformação do diagrama de fases: **A₁ (727 °C - Linha Eutetóide)**, "
        "**A₃ (Transformação Ferrita-Austenita)** e **A(cm) (Limite de Solubilidade da Cimentita)**."
    )
    st.markdown("---")

    col_fec1, col_fec2 = st.columns(2)

    with col_fec1:
        st.subheader("1. Tratamentos Supracríticos (Acima de A₃ / A₁)")

        st.markdown("""
        #### 🔥 Têmpera (Hardening)
        * **Faixa Térmica:** $30^\circ\text{C}$ a $50^\circ\text{C}$ acima de **$A_3$** para aços hipoeutetoides ($C < 0{,}77\%$).
        * **Mecanismo:** Austenitização completa ($\gamma$). O resfriamento rápido (óleo/polímero) impede a difusão do carbono, forçando a transformação em **martensita** (estrutura tetragonal de corpo centrado).
        * **Custo Operacional:** **Alto** (Exige duplo ciclo térmico e insumos de resfriamento ativado).

        #### 🌡️ Normalização (Normalizing)
        * **Faixa Térmica:** $30^\circ\text{C}$ a $50^\circ\text{C}$ acima de **$A_3$** (hipoeutetoides) ou **$A_{cm}$** (hipereutetoides).
        * **Mecanismo:** Homogeneização completa da estrutura no campo austenítico. O resfriamento ao ar calmo promove refinamento do tamanho de grão ($\gamma \rightarrow \alpha + Fe_3C$ fina).
        * **Custo Operacional:** **Médio** (Focado no tempo de forno, sem fluido no resfriamento).

        #### 💤 Recozimento Pleno (Full Annealing)
        * **Faixa Térmica:** $30^\circ\text{C}$ a $50^\circ\text{C}$ acima de **$A_3$** (hipoeutetoides) e entre **$A_1$ e $A_{cm}$** (hipereutetoides).
        * **Mecanismo:** Resfriamento ultralento dentro do próprio forno, garantindo a transformação no patamar superior da curva TTT para geração de perlita grossa de baixíssima dureza.
        * **Custo Operacional:** **Médio a Alto** (Devido à longa permanência e ocupação do forno).
        """)

    with col_fec2:
        st.subheader("2. Tratamentos Subcríticos e Intercríticos")

        st.markdown("""
        #### ⭕ Coalescimento / Esferoidização
        * **Faixa Térmica:** Mantido por longo período **logo abaixo de $A_1$ ($~700^\circ\text{C}$)** ou oscilando ao redor de $727^\circ\text{C}$.
        * **Mecanismo:** As lamelas de cimentita ($Fe_3C$) se fraturam e assumem formato esférico para minimizar a energia superficial, proporcionando a menor dureza possível para usinagem severa.
        * **Custo Operacional:** **Médio a Alto** (Longo tempo de encharque térmico).

        #### 🧊 Alívio de Tensões
        * **Faixa Térmica:** Estritamente subcrítico, entre **$550^\circ\text{C}$ e $650^\circ\text{C}$**.
        * **Mecanismo:** Não cruza as linhas de transformação de fase. Atua unicamente na aniquilação de discordâncias e reorganização cristalina sem alterar as fases presentes na matriz.
        * **Custo Operacional:** **Baixo a Médio**.

        #### 🧪 Solubilização (Inoxidáveis)
        * **Faixa Térmica:** $1000^\circ\text{C}$ a $1150^\circ\text{C}$.
        * **Mecanismo:** Solubilização total de carbonetos de cromo nos contornos de grão em matriz austeníca, seguida de resfriamento ultrarrápido em água.
        * **Custo Operacional:** **Muito Alto** (Altíssimo consumo energético por elevação de temperatura).
        """)

# ==========================================================
# --- ABA 3: SERVIÇOS UNIFORJA & COTAÇÃO ---
# ==========================================================
with aba3:
    col_img_forno, col_info_forno = st.columns([1.2, 1.8])

    with col_img_forno:
        try:
            st.image("forno.png", caption="Fornos operacionais Uniforja", use_container_width=True)
        except Exception:
            st.info("🔥 **Fornos Industriais Uniforja**\nHomologados para processos de alta precisão.")

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

    # Formulário para Captação de Leads
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
                st.success(f"✅ **Obrigado, {nome}!** Sua solicitação para **{servico_desejado}** na liga **{liga_material}** foi enviada à engenharia Uniforja.")

# Rodapé Fixo Institucional
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; font-size: 13px; color: #666; border-top: 1px solid #e0e0e0;">
        Created by: <b>Jefferson Santos - Materials Engineering</b>
    </div>
""", unsafe_allow_html=True)
#%%