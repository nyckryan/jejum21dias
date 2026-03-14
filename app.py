import streamlit as st
import json
import os
from planos import planos

st.set_page_config(page_title="Jejum 21 Dias", page_icon="🙏", layout="centered")

st.title("🙏 Jejum Espiritual - 21 Dias")
st.caption("Tema: Noiva de Cristo")

# -----------------------------
# PROGRESSO
# -----------------------------

progress_file = "progress.json"

if not os.path.exists(progress_file):
    progresso_salvo = [False] * len(planos)
else:
    with open(progress_file, "r") as f:
        progresso_salvo = json.load(f)

# garante tamanho correto
if len(progresso_salvo) != len(planos):
    progresso_salvo = [False] * len(planos)

# -----------------------------
# ALVOS
# -----------------------------

alvos_file = "alvos.json"

if not os.path.exists(alvos_file):
    alvos_salvos = {"pai": "", "avos": ""}
else:
    with open(alvos_file, "r") as f:
        alvos_salvos = json.load(f)

# -----------------------------
# TABS
# -----------------------------

tabs = st.tabs(["📅 Plano","📖 Versículo","🙏 Orações","🎯 Alvos"])

# -----------------------------
# PLANO
# -----------------------------

with tabs[0]:

    st.subheader("Plano de 21 dias")

    completos = sum(progresso_salvo)
    total = len(planos)
    porcentagem = int((completos / total) * 100)

    st.markdown("### 📊 Progresso do Jejum")

    st.progress(completos / total)

    st.write(f"**{porcentagem}% concluído — {completos} de {total} dias**")

    st.divider()

    novo_progresso = []

    for i, dia in enumerate(planos):

        valor = False
        if i < len(progresso_salvo):
            valor = progresso_salvo[i]

        check = st.checkbox(
            f"Dia {dia['dia']} - {dia['tema']}",
            value=valor,
            key=f"dia_{i}"
        )

        novo_progresso.append(check)

    with open(progress_file, "w") as f:
        json.dump(novo_progresso, f)

# -----------------------------
# VERSÍCULO
# -----------------------------

with tabs[1]:

    dia_escolhido = st.selectbox(
        "Escolha o dia",
        planos,
        format_func=lambda x: f"Dia {x['dia']} - {x['tema']}"
    )

    st.subheader(dia_escolhido["tema"])

    st.markdown(f"**{dia_escolhido['versiculo_ref']}**")

    st.write(dia_escolhido["versiculo"])

    st.divider()

    st.subheader("🔎 Contexto Histórico")

    st.write(dia_escolhido["contexto"])

    st.divider()

    st.subheader("📚 Aplicação Prática")

    st.write(dia_escolhido["aplicacao"])

# -----------------------------
# ORAÇÃO
# -----------------------------

with tabs[2]:

    st.subheader("Guia de Oração")

    st.markdown("""
### 1️⃣ Adoração
Reconheça quem Deus é e agradeça pela vida.

### 2️⃣ Entrega a Deus
Entregue seus planos, decisões e preocupações.

### 3️⃣ Transformação Espiritual
Peça que Deus transforme seu coração.

### 4️⃣ Intercessão pelo Pai
Ore pela vida, saúde e proteção do seu pai.

### 5️⃣ Intercessão pelos Avós
Apresente seus avós diante de Deus.

### 6️⃣ Leitura da Palavra
Leia o versículo do dia e reflita sobre como aplicar na sua vida.
""")

# -----------------------------
# ALVOS
# -----------------------------

with tabs[3]:

    st.subheader("🎯 Meus Alvos de Oração")

    pai = st.text_area(
        "Pedidos de oração pelo Pai",
        value=alvos_salvos.get("pai","")
    )

    avos = st.text_area(
        "Pedidos de oração pelos Avós",
        value=alvos_salvos.get("avos","")
    )

    if st.button("Salvar Alvos"):

        data = {
            "pai": pai,
            "avos": avos
        }

        with open(alvos_file, "w") as f:
            json.dump(data, f)

        st.success("Alvos salvos com sucesso 🙏")
