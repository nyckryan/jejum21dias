
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
Guia de Oração – Tempo de Consagração Diária

1️⃣ Adoração

Comece seu tempo de oração reconhecendo quem Deus é. A adoração não é pedir algo, mas honrar e exaltar o Senhor por Sua grandeza, santidade, amor e poder. Quando adoramos a Deus, alinhamos nosso coração com a presença dEle e lembramos que Ele é soberano sobre todas as coisas.

Durante esse momento, você pode agradecer a Deus pela vida, pela salvação, pela família e por tudo o que Ele já fez. A adoração prepara o coração para um relacionamento mais profundo com Deus.

Exemplo de oração:

“Senhor Deus, eu te louvo e te agradeço por quem Tu és. Tu és santo, poderoso e digno de toda honra e glória. Obrigado pela vida que me deste, pelo cuidado diário e pela tua graça sobre mim. Hoje eu reconheço que Tu és o centro da minha vida e quero te adorar de todo o meu coração.”

2️⃣ Entrega a Deus

Depois de adorar, o próximo passo é entregar sua vida ao Senhor. A entrega significa confiar a Deus suas decisões, planos, preocupações e desafios. Muitas vezes carregamos pesos emocionais ou preocupações que Deus deseja que coloquemos em Suas mãos.

Esse momento é um tempo para dizer a Deus que você deseja viver segundo a vontade dEle e permitir que Ele guie seus passos.

Exemplo de oração:

“Senhor, hoje eu entrego a Ti meus planos, minhas preocupações e tudo aquilo que está em meu coração. Entrego meus pensamentos, minhas decisões e meus caminhos. Que a tua vontade seja feita na minha vida. Guia meus passos e me ajuda a viver de acordo com os teus propósitos.”

3️⃣ Transformação Espiritual

Neste momento da oração, peça a Deus que transforme seu caráter. O objetivo do jejum espiritual não é apenas cumprir uma prática religiosa, mas permitir que Deus trabalhe em nosso interior.

Peça a Deus para desenvolver em você o fruto do Espírito: amor, alegria, paz, paciência, bondade, fidelidade, mansidão e domínio próprio.

Exemplo de oração:

“Senhor, transforma meu coração. Tira de mim tudo aquilo que não agrada a Ti. Desenvolve em mim o fruto do teu Espírito. Ensina-me a viver com amor, paciência e sabedoria. Quero crescer espiritualmente e me tornar cada dia mais parecido com Cristo.”

4️⃣ Intercessão pelo Pai

Neste momento, ore especificamente por seu pai. A oração de intercessão é quando apresentamos outras pessoas diante de Deus. Ore pela saúde, proteção, direção e principalmente pela vida espiritual dele.

Você pode pedir que Deus alcance o coração dele, abençoe seu trabalho, sua mente e seus caminhos.

Exemplo de oração:

“Senhor, eu coloco diante de Ti a vida do meu pai. Abençoa sua saúde, protege sua vida e guia seus caminhos. Que ele experimente a tua presença e conheça cada vez mais o teu amor. Guarda sua mente, seu coração e todas as áreas da sua vida.”

5️⃣ Intercessão pelos Avós

Agora apresente seus avós a Deus. A Bíblia valoriza muito a família e a honra aos mais velhos. Ore pela saúde, proteção, paz e alegria na vida deles.

Exemplo de oração:

“Senhor, eu também coloco diante de Ti a vida dos meus avós. Abençoa a saúde deles e guarda cada dia da vida deles. Enche a casa deles com tua paz e tua presença. Que eles sintam teu cuidado e tua proteção em todos os momentos.”

6️⃣ Leitura do livro do Jejum

""")

with tabs[3]:
    pai = st.text_area("Pedidos de oração pelo Pai")
    avos = st.text_area("Pedidos de oração pelos Avós")
    if st.button("Salvar"):
        data = {"pai":pai,"avos":avos}
        with open("alvos.json","w") as f:
            json.dump(data,f)
        st.success("Alvos salvos!")
