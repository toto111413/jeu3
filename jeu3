import streamlit as st
import random

st.subheader("🎯 Jeu : Trouve la cible (version sans module externe)")

# Dimensions de la grille
width, height = 8, 6

# Initialisation de la position et du score
if "target_pos" not in st.session_state:
    st.session_state.target_pos = (random.randint(0, width-1), random.randint(0, height-1))
    st.session_state.score_simple = 0

# Choix du joueur
x_choice = st.slider("Position X", 0, width-1, 0, key="x_choice")
y_choice = st.slider("Position Y", 0, height-1, 0, key="y_choice")

# Bouton pour tirer
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

st.write(f"Score : {st.session_state.score_simple}")
