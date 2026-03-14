import streamlit as st
import json
import os
from planos import planos

st.set_page_config(page_title="Jejum 21 Dias", page_icon="🙏", layout="centered")

st.title("🙏 Jejum Espiritual - 21 Dias")
st.caption("Tema: Noiva de Cristo")

# -----------------------------
# ARQUIVO DE PROGRESSO
# -----------------------------

progress_file = "progress.json"

if not os.path.exists(progress_file):
    with open(progress_file, "w") as f:
        json.dump([False]*len(planos), f)

with open(progress_file, "r") as f:
    progresso_salvo = json.load(f)

# -----------------------------
# ARQUIVO DE ALVOS
# -----------------------------

alvos_file = "alvos.json"

if not os.path.exists(alvos_file):
    with open(alvos_file, "w") as f:
        json.dump({"pai":"", "avos":""}, f)

with open(alvos_file, "r") as f:
    alvos_salvos = json.load(f)

# -----------------------------
# TABS
# -----------------------------

tabs = st.tabs(["📅 Plano","📖 Versículo","🙏 Orações","🎯 Alvos"])

# -----------------------------
# ABA PLANO
# -----------------------------

with tabs[0]:

    st.subheader("Plano de 21 dias")

    novo_progresso = []

    for i, dia in enumerate(planos):

        check = st.checkbox(
            f"Dia {dia['dia']} - {dia['tema']}",
            value=progresso_salvo[i],
            key=f"dia_{i}"
        )

        novo_progresso.append(check)

    # salvar progresso
    with open(progress_file, "w") as f:
        json.dump(novo_progresso, f)

    completos = sum(novo_progresso)

    st.divider()

    st.subheader("📊 Progresso")

    st.progress(completos / len(planos))

    st.write(f"{completos} de {len(planos)} dias concluídos")

# -----------------------------
# ABA VERSÍCULO
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
# ABA ORAÇÕES
# -----------------------------

with tabs[2]:

    st.subheader("Guia de Oração")

    st.markdown("""
### Guia de Oração – Tempo de Consagração Diária

### 1️⃣ Adoração

Comece seu tempo de oração reconhecendo quem Deus é. A adação não é pedir algo, mas honrar e exaltar o Senhor por Sua grandeza, santidade, amor e poder.

Exemplo de oração:

“Senhor Deus, eu te louvo e te agradeço por quem Tu és. Tu és santo, poderoso e digno de toda honra e glória.”

---

### 2️⃣ Entrega a Deus

Entregue a Deus seus planos, decisões e preocupações.

Exemplo:

“Senhor, hoje eu entrego minha vida em Tuas mãos. Guia meus passos e me ajuda a viver segundo tua vontade.”

---

### 3️⃣ Transformação Espiritual

Peça que Deus transforme seu caráter.

Exemplo:

“Senhor, transforma meu coração. Desenvolve em mim amor, paciência e sabedoria.”

---

### 4️⃣ Intercessão pelo Pai

Ore pela vida, saúde, proteção e vida espiritual do seu pai.

---

### 5️⃣ Intercessão pelos Avós

Apresente seus avós diante de Deus e peça bênçãos sobre a vida deles.

---

### 6️⃣ Leitura do Livro / Palavra

Leia o versículo do dia e reflita:

• O que Deus quer me ensinar hoje?  
• Existe algo que preciso mudar?  
• Como posso aplicar isso na minha vida?
""")

# -----------------------------
# ABA ALVOS
# -----------------------------

with tabs[3]:

    st.subheader("🎯 Meus Alvos de Oração")

    pai = st.text_area(
        "Pedidos de oração pelo Pai",
        value=alvos_salvos["pai"]
    )

    avos = st.text_area(
        "Pedidos de oração pelos Avós",
        value=alvos_salvos["avos"]
    )

    if st.button("Salvar Alvos"):

        data = {
            "pai": pai,
            "avos": avos
        }

        with open(alvos_file, "w") as f:
            json.dump(data, f)

        st.success("Alvos salvos com sucesso 🙏")
