import streamlit as st
import random
import time

st.subheader("🎯 Jeu : Trouve la cible (Score + Timer)")

# Paramètres du jeu
width, height = 8, 6
temps_total = 30  # secondes

# Initialisation
if "target_pos" not in st.session_state:
    st.session_state.target_pos = (random.randint(0, width-1), random.randint(0, height-1))
if "score_simple" not in st.session_state:
    st.session_state.score_simple = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "jeu_termine" not in st.session_state:
    st.session_state.jeu_termine = False

# Lancer la partie
if st.button("🚀 Démarrer le jeu", key="start_game"):
    st.session_state.score_simple = 0
    st.session_state.start_time = time.time()
    st.session_state.jeu_termine = False
    st.session_state.target_pos = (random.randint(0, width-1), random.randint(0, height-1))
    st.rerun()

# Si le jeu est en cours
if st.session_state.start_time and not st.session_state.jeu_termine:
    temps_ecoule = int(time.time() - st.session_state.start_time)
    temps_restant = max(0, temps_total - temps_ecoule)

    st.write(f"⏳ Temps restant : {temps_restant} sec")
    st.write(f"🏆 Score : {st.session_state.score_simple}")

    if temps_restant <= 0:
        st.session_state.jeu_termine = True
        st.success(f"🎉 Temps écoulé ! Score final : {st.session_state.score_simple}")

    else:
        # Choix du joueur
        x_choice = st.slider("Position X", 0, width-1, 0, key="x_choice")
        y_choice = st.slider("Position Y", 0, height-1, 0, key="y_choice")

        if st.button("Tirer 🎯", key="tir_simple"):
            if (x_choice, y_choice) == st.session_state.target_pos:
                st.success("🎯 Touché ! +1 point")
                st.session_state.score_simple += 1
                st.session_state.target_pos = (random.randint(0, width-1), random.randint(0, height-1))
            else:
                st.warning("Raté...")

        # Affichage de la grille avec émojis
        for y in range(height):
            cols = st.columns(width)
            for x in range(width):
                if (x, y) == st.session_state.target_pos:
                    cols[x].markdown("🎯", unsafe_allow_html=True)
                elif (x, y) == (x_choice, y_choice):
                    cols[x].markdown("❌", unsafe_allow_html=True)
                else:
                    cols[x].markdown("⬜", unsafe_allow_html=True)

# Si le jeu est terminé
if st.session_state.jeu_termine:
    st.write("🔄 Cliquez sur **Démarrer le jeu** pour rejouer.")
