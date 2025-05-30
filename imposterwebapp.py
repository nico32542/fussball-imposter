import streamlit as st
import random

# Session-State initialisieren
if 'spieler' not in st.session_state:
    st.session_state.spieler = []
if 'input_count' not in st.session_state:
    st.session_state.input_count = 3
if 'setup_done' not in st.session_state:
    st.session_state.setup_done = False
if 'imposter' not in st.session_state:
    st.session_state.imposter = None
if 'imposter2' not in st.session_state:
    st.session_state.imposter2 = None
if 'baller' not in st.session_state:
    st.session_state.baller = ""
if 'current_player' not in st.session_state:
    st.session_state.current_player = 0
if 'show_card' not in st.session_state:
    st.session_state.show_card = False
if 'anzahlimposter' not in st.session_state:
    st.session_state.anzahlimposter = 1

# Fußballer-Liste (gekürzt)
fussballer = [
    "Lionel Messi", "Cristiano Ronaldo", "Kylian Mbappé", "Neymar Jr.",
    "Erling Haaland", "Kevin De Bruyne", "Mohamed Salah", "Robert Lewandowski",
    "Karim Benzema", "Luka Modrić", "Jude Bellingham", "Pedri",
    "Jamal Musiala", "Bukayo Saka", "Florian Wirtz", "Joško Gvardiol",
    "Adama Traoré", "Allan Saint-Maximin", "Wissam Ben Yedder", "Renato Sanches",
    "Theo Hernández", "Ferland Mendy", "Raphael Varane", "Thibaut Courtois",
    "Alisson Becker", "Jan Oblak", "Manuel Neuer", "Gianluigi Donnarumma",
    "Thomas Müller", "Joshua Kimmich", "Ilkay Gündogan", "Kai Havertz",
    "Leroy Sané", "Timo Werner", "Antonio Rüdiger", "Marc-André ter Stegen",
    "Zlatan Ibrahimović", "Darwin Núñez", "Divock Origi", "Mason Greenwood",
    "Kurt Zouma", "Paul Pogba", "Antony", "Lewandowski",
    "Raphina", "Vini Jr.", "Bale", "Sadio Mane",
    "Coutinho", "Rodrygo", "Ousmane Dembélé", "Rodri",
    "Benzema", "Suarez", "Toni Kroos", "Ramos",
    "Pepe", "Marcelo", "Bellingham", "Harry Kane",
    "Olise", "Omar Marmoush", "Rafael Leao", "Trent Alexander Arnold",
    "Osimhen", "Hakimi", "Havertz", "Lamine Yamal",
    "Désiré Doué", "Khvicha Kvaratskhelia", "Xavi Simons", "Alejandro Garnacho",
    "Nico Williams", "Endrick", "Arda Güler", "Viktor Gyökeres",
    "Cole Palmer", "Jeremy Doku", "Kevin De Bruyne", "Frimpong",
    "Kimmich", "Rashford",
    # Legenden
    "Pelé", "Diego Maradona", "Zinedine Zidane", "Jay-Jay Okocha",
    "Ronaldinho", "Ronaldo Nazário", "David Beckham", "Thierry Henry",
    "Paolo Maldini", "Andrea Pirlo", "Xavi", "Kaka",
    "Didier Drogba", "Fernando Torres"
]

st.title("⚽ Imposter-Spiel mit Fußballern")

# --- SPIELERANZAHL ÄNDERN UND IMPOSER ANZAHL AUSWÄHLEN ---
if st.session_state.setup_done:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Spiel neu starten"):
            # Reset Spiel-Variablen, aber Spieler behalten
            st.session_state.imposter = random.randint(0, len(st.session_state.spieler) - 1)
            if st.session_state.anzahlimposter == 2:
                st.session_state.imposter2 = random.randint(0, len(st.session_state.spieler) - 1)
                while st.session_state.imposter2 == st.session_state.imposter:
                    st.session_state.imposter2 = random.randint(0, len(st.session_state.spieler) - 1)
            else:
                st.session_state.imposter2 = st.session_state.imposter
            st.session_state.baller = random.choice(fussballer)
            st.session_state.current_player = 0
            st.session_state.show_card = False
            st.rerun()
    with col2:
        if st.button("Spieleranzahl ändern"):
            st.session_state.setup_done = False
            st.rerun()

# --- SPIEL SETUP ---
if not st.session_state.setup_done:
    st.header("Spieler hinzufügen")

    st.session_state.input_count = st.slider("Wie viele Spieler?", min_value=2, max_value=10, value=3)
    st.session_state.anzahlimposter = st.selectbox("Wie viele Imposter?", options=[1, 2], index=0)

    eingegebene_spieler = []
    for i in range(st.session_state.input_count):
        name = st.text_input(f"Name Spieler {i+1}", key=f"spieler_{i}")
        if name:
            eingegebene_spieler.append(name)

    if len(eingegebene_spieler) == st.session_state.input_count and st.button("Spiel starten"):
        st.session_state.spieler = eingegebene_spieler
        st.session_state.imposter = random.randint(0, len(eingegebene_spieler) - 1)

        if st.session_state.anzahlimposter == 2:
            st.session_state.imposter2 = random.randint(0, len(eingegebene_spieler) - 1)
            while st.session_state.imposter2 == st.session_state.imposter:
                st.session_state.imposter2 = random.randint(0, len(eingegebene_spieler) - 1)
        else:
            st.session_state.imposter2 = st.session_state.imposter

        st.session_state.baller = random.choice(fussballer)
        st.session_state.current_player = 0
        st.session_state.show_card = False
        st.session_state.setup_done = True
        st.rerun()

# --- SPIEL ABLÄUFT ---
elif st.session_state.current_player < len(st.session_state.spieler):
    player = st.session_state.spieler[st.session_state.current_player]
    st.header(f"{player} ist dran")

    if not st.session_state.show_card:
        if st.button("Karte anzeigen"):
            st.session_state.show_card = True
            st.rerun()
    else:
        if st.session_state.current_player in [st.session_state.imposter, st.session_state.imposter2]:
            st.subheader("🟥 Du bist der IMPOSTER!")
        else:
            st.subheader(f"✅ Du bist: {st.session_state.baller}")

        if st.button("Weiter zum nächsten Spieler"):
            st.session_state.current_player += 1
            st.session_state.show_card = False
            st.rerun()

# --- ALLE SPIELER HABEN IHRE KARTE GESEHEN ---
else:
    starter = random.choice(st.session_state.spieler)
    st.success(f"🎉 Das Spiel beginnt! {starter} startet.")
