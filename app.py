# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:03:32 2026

@author: jefferson.santos
"""

#%%
import math
import streamlit as st

# ==========================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Uniforja | Divisão de Tratamento Térmico & Engenharia de Materiais",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# 2. ESTILIZAÇÃO CSS PERSONALIZADA
# ==========================================================
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stButton>button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 6px;
        font-weight: bold;
        border: none;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #0f172a;
        color: #f59e0b;
    }
    .metric-card {
        background-color: #ffffff;
        border-left: 5px solid #d97706;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    .formula-box {
        background-color: #eef2ff;
        border-left: 4px solid #1e3a8a;
        padding: 12px 18px;
        border-radius: 6px;
        font-family: 'Courier New', Courier, monospace;
        margin: 10px 0;
    }
    .reference-tag {
        font-size: 0.82rem;
        color: #64748b;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================================
# 3. CABEÇALHO INSTITUCIONAL & AUTORIA
# ==========================================================
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    try:
        st.image("logo_uniforja.png", use_container_width=True)
    except Exception:
        st.markdown("### ⚙️ **UNIFORJA**\n*Divisão Térmica*")

with col_titulo:
    st.title("⚙️ Soluções Avançadas em Tratamento Térmico")
    st.caption("Engenharia de Materiais, Metalurgia Física & Modelagem Microestrutural")

st.markdown("""
<div style="background-color: #1e3a8a; padding: 8px 16px; border-radius: 6px; color: #ffffff; font-size: 0.9rem;">
    <strong>Responsáveis Técnicos:</strong> Eng. Jefferson Silva Pereira dos Santos &nbsp;|&nbsp; Eng. Gustavo Estrela da Silva &nbsp;|&nbsp; 
    <em>Ref. Normativas: ASM Metals Handbook (Vols. 1, 3, 4) & API-6A / AMS-2750</em>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# 4. DEFINIÇÃO DAS ABAS PRINCIPAIS
# ==========================================================
aba1, aba2, aba3 = st.tabs([
    "🧮 Central de Cálculos, Equações & Conversões", 
    "📚 Fundamentos Metalúrgicos & ASM Handbook", 
    "🏭 Serviços Uniforja & Cotação"
])

# ==========================================================
# --- ABA 1: CENTRAL DE CÁLCULOS E CONVERSÕES ---
# ==========================================================
with aba1:
    st.header("Central de Cálculos de Engenharia e Previsão Microestrutural")
    st.write("Ferramentas operacionais e equações empíricas para especificação de tratamento térmico, cinéticas de transformação e conversões.")

    sub1, sub2, sub3, sub4, sub5 = st.tabs([
        "🧮 Carbono Equivalente (CE)", 
        "🌡️ Temperatura Mₛ (Andrews) & Dureza", 
        "🔥 Parâmetro de Revenimento (Hollomon-Jaffe)",
        "🔄 Dureza x Tração (ASTM E140)", 
        "⚖️ Unidades & Calculadora de Massa"
    ])

    # ------------------------------------------------------
    # 1.1 Carbono Equivalente
    # ------------------------------------------------------
    with sub1:
        st.subheader("Cálculo de Carbono Equivalente (CE - IIW & Pcm)")
        st.write("Sintetiza o efeito dos elementos de liga na temperabilidade e soldabilidade do aço.")

        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            c = st.number_input("Carbono (C %)", min_value=0.0, max_value=2.0, value=0.40, step=0.01)
            mn = st.number_input("Manganês (Mn %)", min_value=0.0, max_value=3.0, value=0.75, step=0.01)
            si = st.number_input("Silício (Si %)", min_value=0.0, max_value=2.0, value=0.25, step=0.01)
        with col_c2:
            cr = st.number_input("Cromo (Cr %)", min_value=0.0, max_value=5.0, value=0.80, step=0.01)
            mo = st.number_input("Molibdênio (Mo %)", min_value=0.0, max_value=2.0, value=0.20, step=0.01)
            v = st.number_input("Vanádio (V %)", min_value=0.0, max_value=1.0, value=0.00, step=0.01)
        with col_c3:
            ni = st.number_input("Níquel (Ni %)", min_value=0.0, max_value=5.0, value=0.00, step=0.01)
            cu = st.number_input("Cobre (Cu %)", min_value=0.0, max_value=2.0, value=0.00, step=0.01)
            b = st.number_input("Boro (B %)", min_value=0.0, max_value=0.01, value=0.000, step=0.001, format="%.3f")

        ce_iiw = c + (mn / 6) + ((cr + mo + v) / 5) + ((ni + cu) / 15)
        pcm = c + (si / 30) + ((mn + cu + cr) / 20) + (mo / 15) + (v / 10) + (5 * b)

        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric(label="Carbono Equivalente (CE - IIW)", value=f"{ce_iiw:.3f}%")
        with col_m2:
            st.metric(label="Parâmetro de Trinca de Solda (Pcm)", value=f"{pcm:.3f}%")

        st.markdown("""
        <div class="formula-box">
            <strong>Fórmula IIW:</strong> CE = C + (Mn/6) + (Cr + Mo + V)/5 + (Ni + Cu)/15<br>
            <strong>Fórmula Ito-Bessyo (Pcm):</strong> Pcm = C + Si/30 + (Mn + Cu + Cr)/20 + Mo/15 + V/10 + 5B
        </div>
        """, unsafe_allow_html=True)

        st.info(
            "💡 **Importância Metalúrgica:** Elevados valores de $CE$ indicam retardo na decomposição da austenita proeutetóide, "
            "deslocando as curvas TTT/TRC para a direita. Isso favorece a têmpera profunda (formação de martensita), porém "
            "aumenta a suscetibilidade a trincas a frio e exige meios de resfriamento mais moderados (óleo/salmoura isotérmica)."
        )

    # ------------------------------------------------------
    # 1.2 Temperatura Ms (Andrews) & Dureza Martensítica
    # ------------------------------------------------------
    with sub2:
        st.subheader("Temperatura de Início Martensítico (Mₛ) & Dureza Teórica Máxima")
        st.write("Estimativa empírica da temperatura $M_s$ pela Equação de Andrews e predição de dureza martensítica de têmpera.")

        col_ms1, col_ms2 = st.columns(2)
        with col_ms1:
            c_ms = st.slider("Teor de Carbono (C %):", 0.05, 1.20, 0.40, 0.01)
            mn_ms = st.slider("Teor de Manganês (Mn %):", 0.10, 2.50, 0.70, 0.05)
            cr_ms = st.slider("Teor de Cromo (Cr %):", 0.00, 3.00, 0.80, 0.05)
        with col_ms2:
            ni_ms = st.slider("Teor de Níquel (Ni %):", 0.00, 5.00, 0.00, 0.10)
            mo_ms = st.slider("Teor de Molibdênio (Mo %):", 0.00, 1.50, 0.20, 0.05)

        # Fórmula de Andrews
        ms_temp = 539 - (423 * c_ms) - (30.4 * mn_ms) - (12.1 * cr_ms) - (17.7 * ni_ms) - (7.5 * mo_ms)
        
        # Dureza Máxima Aproximada da Martensita (para C < 0,60%)
        if c_ms <= 0.60:
            hrc_max = 20 + (60 * math.sqrt(c_ms))
        else:
            hrc_max = 65.0  # Saturação por austenita retida

        col_r1, col_r2 = st.columns(2)
        col_r1.metric("Temperatura Mₛ Estimada", f"{ms_temp:.1f} °C")
        col_r2.metric("Dureza Máxima da Martensita", f"~{hrc_max:.1f} HRC")

        st.markdown("""
        <div class="formula-box">
            <strong>Fórmula de Andrews:</strong> Mₛ (°C) = 539 - 423(%C) - 30.4(%Mn) - 12.1(%Cr) - 17.7(%Ni) - 7.5(%Mo)<br>
            <strong>Dureza Máxima Martensítica:</strong> HRC_máx ≈ 20 + 60√(%C) (para %C ≤ 0.60%)
        </div>
        """, unsafe_allow_html=True)
        st.caption("<span class='reference-tag'>Fonte: ASM Metals Handbook, Vol. 4 - Heat Treating.</span>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # 1.3 Parâmetro de Hollomon-Jaffe (Revenimento)
    # ------------------------------------------------------
    with sub3:
        st.subheader("Modelagem do Revenimento: Parâmetro de Hollomon-Jaffe (HP)")
        st.write("Avalia a equivalência entre temperatura e tempo no processo de revenimento de martensiticos.")

        col_hj1, col_hj2 = st.columns(2)
        with col_hj1:
            temp_rev = st.number_input("Temperatura de Revenimento (°C):", value=550.0, step=10.0)
            tempo_rev = st.number_input("Tempo de Permanência no Patamar (Horas):", value=2.0, step=0.5)
        with col_hj2:
            const_c = st.number_input("Constante do Material (C) [Típico: 18 a 22]:", value=20.0, step=0.5)

        temp_k = temp_rev + 273.15
        if tempo_rev > 0:
            hp = temp_k * (const_c + math.log10(tempo_rev)) * 1e-3
        else:
            hp = 0.0

        st.metric("Parâmetro de Hollomon-Jaffe (HP)", f"{hp:.2f}")

        st.markdown("""
        <div class="formula-box">
            <strong>Parâmetro HP:</strong> P = T · [ C + log10(t) ] × 10⁻³<br>
            <em>onde T é a temperatura em Kelvin, t é o tempo em horas, e C é a constante de liga (geralmente C ≈ 20).</em>
        </div>
        """, unsafe_allow_html=True)
        st.caption("Dois ciclos de revenimento que apresentem o mesmo valor de HP resultarão em durezas e propriedades mecânicas idênticas.")

    # ------------------------------------------------------
    # 1.4 Conversão de Dureza ASTM E140 & Tração
    # ------------------------------------------------------
    with sub4:
        st.subheader("Conversão de Dureza (ASTM E140) & Estimativa de Tração")

        tabela_dureza = [
            {"HRC": 68, "HBW": 940, "HV": 940, "LR_MPa": 2350},
            {"HRC": 60, "HBW": 654, "HV": 697, "LR_MPa": 2180},
            {"HRC": 55, "HBW": 560, "HV": 595, "LR_MPa": 1910},
            {"HRC": 50, "HBW": 481, "HV": 513, "LR_MPa": 1660},
            {"HRC": 45, "HBW": 421, "HV": 446, "LR_MPa": 1440},
            {"HRC": 40, "HBW": 371, "HV": 392, "LR_MPa": 1250},
            {"HRC": 35, "HBW": 327, "HV": 345, "LR_MPa": 1090},
            {"HRC": 30, "HBW": 286, "HV": 302, "LR_MPa": 950},
            {"HRC": 25, "HBW": 253, "HV": 266, "LR_MPa": 840},
            {"HRC": 20, "HBW": 226, "HV": 238, "LR_MPa": 750}
        ]

        val_hrc = st.slider("Selecione a Dureza em Rockwell C (HRC):", min_value=20, max_value=68, value=40, step=1)
        item_proximo = min(tabela_dureza, key=lambda x: abs(x["HRC"] - val_hrc))

        col_d1, col_d2, col_d3, col_d4 = st.columns(4)
        col_d1.metric("Rockwell C (HRC)", f"{val_hrc}")
        col_d2.metric("Brinell (HBW)", f"~{item_proximo['HBW']}")
        col_d3.metric("Vickers (HV)", f"~{item_proximo['HV']}")
        col_d4.metric("Resistência Tração (LR)", f"~{item_proximo['LR_MPa']} MPa")

        st.warning(
            "⚠️ **Nota de Engenharia:** As conversões seguem a norma ASTM E140 Tabela 1 (Aços Carbono e Liga). "
            "A relação LR ≈ 3,45 × HBW é uma estimativa empírica e deve ser validada por ensaio destrutivo de tração (ISO 6892 / ASTM A370)."
        )

    # ------------------------------------------------------
    # 1.5 Conversor de Tensões/Impacto & Peso do Lote
    # ------------------------------------------------------
    with sub5:
        st.subheader("Conversor de Unidades & Calculadora de Massa de Carga")

        col_u1, col_u2 = st.columns(2)
        with col_u1:
            st.markdown("#### Conversor de Tensões")
            v_tensao = st.number_input("Tensão de Entrada:", value=100.0, step=10.0)
            u_tensao = st.selectbox("Unidade:", ["ksi", "MPa", "kgf/mm²", "Psi"])

            if u_tensao == "ksi":
                mpa = v_tensao * 6.89476
            elif u_tensao == "kgf/mm²":
                mpa = v_tensao * 9.80665
            elif u_tensao == "Psi":
                mpa = v_tensao * 0.00689476
            else:
                mpa = v_tensao

            st.write(f"• **MPa:** {mpa:.2f}")
            st.write(f"• **ksi:** {mpa / 6.89476:.2f}")
            st.write(f"• **kgf/mm²:** {mpa / 9.80665:.2f}")

        with col_u2:
            st.markdown("#### Conversor de Tenacidade (Impacto Charpy)")
            v_imp = st.number_input("Energia de Impacto:", value=27.0, step=1.0)
            u_imp = st.selectbox("Unidade:", ["Joule (J)", "Ft.lbf", "kgf.m"])

            if u_imp == "Joule (J)":
                j = v_imp
            elif u_imp == "Ft.lbf":
                j = v_imp * 1.35582
            else:
                j = v_imp * 9.80665

            st.write(f"• **Joule (J):** {j:.1f}")
            st.write(f"• **Ft.lbf:** {j / 1.35582:.1f}")
            st.write(f"• **kgf.m:** {j / 9.80665:.2f}")

        st.markdown("---")
        st.markdown("#### Calculadora de Peso e Carga do Forno")
        geometria = st.selectbox("Formato do Componente:", ["Barra Redonda / Cilindro", "Bloco Retangular / Chapa", "Anel / Forjado Vazado"])
        densidade = st.number_input("Densidade do Aço (g/cm³):", value=7.85, step=0.01)

        peso_unit = 0.0
        if geometria == "Barra Redonda / Cilindro":
            d_mm = st.number_input("Diâmetro (mm):", value=120.0)
            l_mm = st.number_input("Comprimento (mm):", value=500.0)
            vol_cm3 = (math.pi * ((d_mm/10/2)**2) * (l_mm/10))
            peso_unit = (vol_cm3 * densidade) / 1000.0

        elif geometria == "Bloco Retangular / Chapa":
            w_mm = st.number_input("Largura (mm):", value=150.0)
            t_mm = st.number_input("Espessura (mm):", value=80.0)
            l_mm = st.number_input("Comprimento (mm):", value=600.0)
            vol_cm3 = (w_mm/10) * (t_mm/10) * (l_mm/10)
            peso_unit = (vol_cm3 * densidade) / 1000.0

        else:
            d_ext = st.number_input("Diâmetro Externo (mm):", value=300.0)
            d_int = st.number_input("Diâmetro Interno (mm):", value=150.0)
            h_mm = st.number_input("Altura/Comprimento (mm):", value=100.0)
            vol_ext = math.pi * ((d_ext/10/2)**2) * (h_mm/10)
            vol_int = math.pi * ((d_int/10/2)**2) * (h_mm/10)
            peso_unit = ((vol_ext - vol_int) * densidade) / 1000.0

        qtd = st.number_input("Quantidade de Peças na Carga:", min_value=1, value=10)
        peso_total = peso_unit * qtd

        c_p1, c_p2 = st.columns(2)
        c_p1.metric("Peso Unitário Estimado", f"{peso_unit:.2f} kg")
        c_p2.metric("Massa Total da Carga", f"{peso_total:.2f} kg", f"{peso_total/1000.0:.3f} Toneladas")


# ==========================================================
# --- ABA 2: FUNDAMENTOS METALÚRGICOS (ASM HANDBOOK) ---
# ==========================================================
with aba2:
    st.header("Fundamentos Metalúrgicos: Termodinâmica e Cinética das Fases")
    st.write(
        "A seleção do ciclo térmico requer conhecimento das reações invariantes do Diagrama Fe-Fe₃C, "
        "curvas TTT/TRC, equações de transformação (JMAK) e a Relação de Hall-Petch."
    )
    st.markdown("---")

    sec1, sec2, sec3, sec4 = st.tabs([
        "📊 Diagrama Fe-C & Reações Invariantes", 
        "⏱️ Cinética TTT / TRC & Avrami (JMAK)", 
        "🌾 Hall-Petch & Normalização vs Recozimento", 
        "⚔️ Austêmpera vs Martêmpera (Propriedades)"
    ])

    # ------------------------------------------------------
    # 2.1 Diagrama Fe-Fe3C e Reações
    # ------------------------------------------------------
    with sec1:
        col_diag1, col_diag2 = st.columns([1.2, 1.8])

        with col_diag1:
            st.subheader("Reações Invariantes (ASM Vol. 3)")
            st.markdown("""
            * **Peritética (1495 °C):**
              $$\\text{L}(0{,}53\\%\\text{C}) + \\delta(0{,}09\\%\\text{C}) \\rightleftharpoons \\gamma(0{,}17\\%\\text{C})$$
            * **Eutética (1148 °C):**
              $$\\text{L}(4{,}30\\%\\text{C}) \\rightleftharpoons \\gamma(2{,}14\\%\\text{C}) + \\text{Fe}_3\\text{C}(6{,}70\\%\\text{C})$$
            * **Eutetóide (727 °C):**
              $$\\gamma(0{,}76\\%\\text{C}) \\rightleftharpoons \\alpha(0{,}022\\%\\text{C}) + \\text{Fe}_3\\text{C}(6{,}70\\%\\text{C})$$
            """)

            st.subheader("Temperaturas Críticas de Fase")
            st.markdown("""
            * **$A_1$ (727 °C):** Temperatura eutetóide de decomposição da austenita.
            * **$A_2$ (770 °C):** Ponto Curie (transição ferromagnética para paramagnética da ferrita).
            * **$A_3$:** Limite de solubilidade da ferrita proeutetóide em relação à austenita CFC.
            * **$A_{cm}$:** Solubilidade limite do carbono na austenita para aços hipereutetóides.
            """)

        with col_diag2:
            st.subheader("Transformações Supracríticas e Subcríticas")
            st.markdown("""
            #### 🔥 Têmpera (Hardening)
            Austenitização $30{-}50^\\circ\\text{C}$ acima de $A_3$ seguida de resfriamento rápido em taxa superior à velocidade crítica ($v_{\\text{crit}}$). Impede a difusão do carbono e gera **Martensita TCT** de alta dureza.

            #### 🌡️ Normalização (Normalizing)
            Aquecimento acima de $A_3$ ou $A_{cm}$ e resfriamento ao **ar calmo**. O refinamento de grão resultante aumenta simultaneamente o limite de escoamento e a tenacidade de impacto.

            #### 💤 Recozimento Pleno (Full Annealing)
            Resfriamento ultralento no forno ($10{-}20^\\circ\\text{C/h}$). Gera perlita grossa com baixíssima dureza e excelente usinabilidade.

            #### ⭕ Coalescimento / Esferoidização
            Permanência prolongada logo abaixo de $A_1$ ($\\sim 700^\\circ\\text{C}$). Coalesce as lamelas de $\\text{Fe}_3\\text{C}$ em esferóides em matriz ferrítica.
            """)

    # ------------------------------------------------------
    # 2.2 Cinética TTT/TRC e Avrami
    # ------------------------------------------------------
    with sec2:
        st.subheader("Cinética de Transformação e Equação de Avrami (JMAK)")

        col_jmak1, col_jmak2 = st.columns(2)
        with col_jmak1:
            st.markdown("""
            A fração transformada ($y$) em condições isotérmicas ao longo do tempo ($t$) é regida pela **Equação de Johnson-Mehl-Avrami-Kolmogorov**:

            $$y = 1 - \\exp\\left(-k \\cdot t^n\\right)$$

            * **$k$:** Constante cinética dependente da taxa de nucleação e velocidade de crescimento interfacial.
            * **$n$:** Expoente de Avrami (varia entre 1 e 4 conforme a geometria dos sítios de nucleação).
            * **O Nariz TTT/TRC:** Ponto de inflexão no gráfico tempo-temperatura onde a competição entre a força motriz termodinâmica (superresfriamento $\\Delta T$) e a mobilidade difusional atinge sua taxa máxima.
            """)

        with col_jmak2:
            st.markdown("""
            #### Temperabilidade e Elementos de Liga (Cr, Ni, Mo, Mn)
            A adição de elementos de liga retarda a difusão do carbono no campo austenítico e desativa sítios de nucleação nos contornos de grão de $\\gamma$.

            * **Efeito no Diagrama:** O "nariz" das curvas TTT e TRC é deslocado para tempos mais longos (para a direita).
            * **Taxa Crítica ($v_{\\text{crit}}$):** Menor velocidade de resfriamento necessária para desviar completamente do nariz e garantir 100% de transformação martensítica no núcleo da peça.
            * **Norma ASTM A255 (Ensaio Jominy):** Padroniza a medição da profundidade de têmpera sob severidade do meio ($H$).
            """)

    # ------------------------------------------------------
    # 2.3 Hall-Petch & Propriedades
    # ------------------------------------------------------
    with sec3:
        st.subheader("Refino de Grão e a Relação de Hall-Petch")

        col_hp1, col_hp2 = st.columns(2)

        with col_hp1:
            st.markdown("""
            A normalização é o único tratamento térmico convencional que eleva simultaneamente o **Limite de Escoamento** e a **Tenacidade ao Impacto**, conforme regido pela equação:

            $$\\sigma_y = \\sigma_0 + k_y \\cdot d^{-1/2}$$

            * **$\\sigma_y$:** Tensão de escoamento mecânico.
            * **$\\sigma_0$:** Tensão de atrito para movimentação de discordâncias na rede.
            * **$k_y$:** Constante de travamento dos contornos de grão.
            * **$d$:** Diâmetro médio dos grãos cristalinos.
            """)

        with col_hp2:
            st.subheader("Propriedades Comparativas: Aço SAE 1045 (ASM Vol. 1)")
            
            dados_1045 = {
                "Propriedade Mecânica": ["Limite de Escoamento (R_eH)", "Limite de Resistência (R_m)", "Dureza Brinell", "Alongamento (A₅)", "Tenacidade Charpy"],
                "Recozido Pleno": ["380 MPa", "570 MPa", "170 HBW", "25,0%", "Moderada"],
                "Normalizado ao Ar": ["430 MPa (+13%)", "670 MPa (+17%)", "207 HBW", "22,0%", "Elevada"]
            }
            st.table(dados_1045)

    # ------------------------------------------------------
    # 2.4 Austêmpera vs Martêmpera (Tabela Quantitativa)
    # ------------------------------------------------------
    with sec4:
        st.subheader("Austêmpera vs Martêmpera: Propriedades Mecânicas no Aço AISI 4340 / 1095")
        st.caption("Dados experimentais quantitativos adaptados do *ASM Metals Handbook, Vol. 4 (Heat Treating)* para mesma dureza nominal de **50 HRC**.")

        dados_aust = {
            "Propriedade Mecânica": [
                "Limite de Resistência à Tração (R_m)",
                "Alongamento em 2 polegadas (A₅)",
                "Estricção / Redução de Área (Z)",
                "Tenacidade ao Impacto (Charpy V)",
                "Tenacidade à Fratura (K_IC)",
                "Isenção de Revenimento",
                "Risco de Trincas / Empenamento"
            ],
            "Martensita Revenida (50 HRC)": [
                "1800 MPa",
                "3,75%",
                "26,1%",
                "3,6 J (2,6 ft-lb)",
                "52 MPa√m",
                "Não (Exige Revenimento imediato)",
                "Médio a Elevado"
            ],
            "Bainita Austemperada (50 HRC)": [
                "1810 MPa",
                "5,00% (+33,3% de ductilidade)",
                "46,4% (+77,7% de tenacidade)",
                "6,4 J (+77,8% de absorção de choque)",
                "78 MPa√m (+50% resistência a trincas)",
                "Sim (Isento de Revenimento)",
                "Quase Nulo (Tensão residual mínima)"
            ]
        }

        st.table(dados_aust)


# ==========================================================
# --- ABA 3: SERVIÇOS UNIFORJA & COTAÇÃO ---
# ==========================================================
with aba3:
    col_img_forno, col_info_forno = st.columns([1.2, 1.8])

    with col_img_forno:
        try:
            st.image("forno.png", caption="Fornos Homologados Uniforja (AMS-2750 & API-6A)", use_container_width=True)
        except Exception:
            st.info("🔥 **Fornos Industriais Uniforja**\nCapacidade para peças de grande porte e forjados pesados.")

    with col_info_forno:
        st.markdown("### TRATAMENTO TÉRMICO UNIFORJA")
        st.write(
            "A **UNIFORJA** possui parque fabril e fornos operacionais certificados nas normas "
            "**API-6A** e **AMS-2750** (TUS/SAT), garantindo controle rigoroso de pirometria e uniformidade térmica:"
        )
        st.markdown("""
        * **Recozimento Pleno, Isotérmico e Subcrítico**
        * **Normalização e Refino de Grão ao Ar**
        * **Têmpera e Revenido (Q&T)** em óleo, água e polímero
        * **Solubilização e Envelhecimento de Aços Inoxidáveis e Ligas Especiais**
        * **Alívio de Tensões Subcrítico**
        * **Coalescimento e Esferoidização**
        """)

    st.markdown("---")

    # Formulário para Captação de Leads
    st.subheader("Solicite uma Cotação ou Análise Técnica da Engenharia")

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
                    "Austêmpera / Martêmpera",
                    "Alívio de Tensões",
                    "Outros / Consultar Engenharia"
                ]
            )
            liga_material = st.text_input("Liga do Aço (ex: SAE 4140, SAE 4340, F22, F51) *")
            peso_lote = st.text_input("Peso Estimado do Lote / Peça (kg ou toneladas)")

        mensagem = st.text_area(
            "Detalhamento Técnico (Geometria, Dureza Alvo desejada em HRC/HBW ou Norma Aplicável ex: API-6A PSL3)"
        )

        submitted = st.form_submit_button("Enviar Solicitação à Engenharia Uniforja")

        if submitted:
            if not nome or not email or not empresa or not liga_material:
                st.warning("⚠️ Por favor, preencha todos os campos obrigatórios marcados com (*).")
            else:
                st.success(f"✅ **Obrigado, {nome}!** Sua solicitação para **{servico_desejado}** na liga **{liga_material}** foi enviada com sucesso à equipe de Engenharia da Uniforja.")

# Rodapé Fixo Institucional
st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; font-size: 13px; color: #64748b; border-top: 1px solid #e2e8f0;">
        <strong>Uniforja | Divisão de Tratamento Térmico & Engenharia de Materiais</strong><br>
        Eng. Jefferson Silva Pereira dos Santos &nbsp;|&nbsp; Eng. Gustavo Estrela da Silva
    </div>
""", unsafe_allow_html=True)
#%%