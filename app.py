
import streamlit as st
import json
from planos import planos

st.set_page_config(page_title="Jejum 21 Dias", page_icon="🙏", layout="centered")

st.title("🙏 Jejum Espiritual - 21 Dias")
st.caption("Tema: Noiva de Cristo")

tabs = st.tabs(["📅 Plano","📖 Versículo","🙏 Orações","🎯 Alvos"])

with tabs[0]:
    progresso = []
    for dia in planos:
        check = st.checkbox(f"Dia {dia['dia']} - {dia['tema']}")
        progresso.append(check)
    if progresso:
        st.progress(sum(progresso)/len(planos))

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
    st.subheader("📚 Aplicação Prática")
    st.write(dia_escolhido["aplicacao"])

with tabs[2]:
    st.subheader("Guia de Oração")
    st.write("""
1️⃣ Adoração  
2️⃣ Entrega a Deus  
3️⃣ Transformação espiritual  
4️⃣ Ore pelo seu pai  
5️⃣ Ore pelos seus avós
""")

with tabs[3]:
    pai = st.text_area("Pedidos de oração pelo Pai")
    avos = st.text_area("Pedidos de oração pelos Avós")
    if st.button("Salvar"):
        data = {"pai":pai,"avos":avos}
        with open("alvos.json","w") as f:
            json.dump(data,f)
        st.success("Alvos salvos!")
