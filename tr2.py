import streamlit as st

st.set_page_config(
    page_title="Taschenrechner von Maksym",
    page_icon="🧮",
    layout="centered"
)

# Design
st.markdown("""
<style>
    .stApp {
        background-color: white;
    }

    .main .block-container {
        max-width: 430px;
        padding-top: 30px;
    }

    h1 {
        text-align: center;
        color: #111111;
        font-family: Arial, sans-serif;
        margin-bottom: 25px;
    }

    /* Ausgabefeld */
    .display {
        background-color: black;
        color: white;
        border-radius: 12px;
        padding: 22px 15px;
        margin-bottom: 18px;
        text-align: right;
        font-size: 32px;
        font-weight: bold;
        min-height: 48px;
        overflow-wrap: anywhere;
    }

    /* Normale Buttons */
    div.stButton > button {
        width: 100%;
        height: 58px;
        border-radius: 10px;
        border: 1px solid #999999;
        background-color: #f2f2f2;
        color: #111111;
        font-size: 23px;
        font-weight: bold;
        margin-bottom: 8px;
    }

    div.stButton > button:hover {
        background-color: #d9d9d9;
        color: black;
    }

    /* Rechnen-Button */
    .calculate div.stButton > button {
        background-color: #16803c !important;
        color: white !important;
        border: none !important;
        height: 62px;
        font-size: 26px;
    }

    .calculate div.stButton > button:hover {
        background-color: #0e5e2b !important;
        color: white !important;
    }

    /* Löschen- und Zurück-Buttons */
    .special div.stButton > button {
        background-color: #eeeeee;
    }
</style>
""", unsafe_allow_html=True)


# Speicher für den Taschenrechner
if "display" not in st.session_state:
    st.session_state.display = "0"

if "neue_eingabe" not in st.session_state:
    st.session_state.neue_eingabe = True


# Funktionen
def zahl_eingeben(zeichen):
    if st.session_state.neue_eingabe or st.session_state.display == "0":
        st.session_state.display = zeichen
        st.session_state.neue_eingabe = False
    else:
        st.session_state.display += zeichen


def zeichen_eingeben(zeichen):
    if st.session_state.neue_eingabe:
        st.session_state.neue_eingabe = False

    # Zeichen für Python-Auswertung
    if zeichen == "×":
        zeichen = "*"
    elif zeichen == "÷":
        zeichen = "/"
    elif zeichen == "^":
        zeichen = "^"

    st.session_state.display += zeichen


def loeschen():
    st.session_state.display = "0"
    st.session_state.neue_eingabe = True


def zurueck():
    if len(st.session_state.display) > 1:
        st.session_state.display = st.session_state.display[:-1]
    else:
        st.session_state.display = "0"


def berechnen():
    ausdruck = st.session_state.display

    try:
        # Nur erlaubte Zeichen zulassen
        erlaubte_zeichen = "0123456789+-*/().%^ "

        if not all(zeichen in erlaubte_zeichen for zeichen in ausdruck):
            raise ValueError

        # Potenzzeichen in Python-Schreibweise umwandeln
        ausdruck = ausdruck.replace("^", "**")

        # Auswertung ohne zusätzliche Bibliothek
        ergebnis = eval(ausdruck, {"__builtins__": None}, {})

        if ergebnis == int(ergebnis):
            st.session_state.display = str(int(ergebnis))
        else:
            st.session_state.display = str(round(ergebnis, 8))

        st.session_state.neue_eingabe = True

    except ZeroDivisionError:
        st.session_state.display = "Fehler"
        st.session_state.neue_eingabe = True

    except:
        st.session_state.display = "Fehler"
        st.session_state.neue_eingabe = True


# Überschrift
st.title("Taschenrechner von Maksym")

# Anzeige oben
st.markdown(
    f'<div class="display">{st.session_state.display}</div>',
    unsafe_allow_html=True
)


# Erste Button-Reihe
spalte1, spalte2, spalte3, spalte4 = st.columns(4)

with spalte1:
    if st.button("C"):
        loeschen()

with spalte2:
    if st.button("⌫"):
        zurueck()

with spalte3:
    if st.button("("):
        zeichen_eingeben("(")

with spalte4:
    if st.button(")"):
        zeichen_eingeben(")")


# Zahlen und Grundrechenarten
reihen = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["0", ".", "%", "+"],
    ["^", "(", ")", "="]
]

for reihe in reihen:
    spalten = st.columns(4)

    for nummer, taste in enumerate(reihe):
        with spalten[nummer]:

            if taste == "=":
                st.markdown('<div class="calculate">', unsafe_allow_html=True)
                if st.button("=", key=f"taste_{taste}_{len(reihe)}"):
                    berechnen()
                st.markdown("</div>", unsafe_allow_html=True)

            elif taste.isdigit() or taste == ".":
                if st.button(taste, key=f"taste_{taste}_{len(reihe)}"):
                    zahl_eingeben(taste)

            else:
                if taste == "−":
                    echtes_zeichen = "-"
                else:
                    echtes_zeichen = taste

                if st.button(taste, key=f"taste_{taste}_{len(reihe)}"):
                    zeichen_eingeben(echtes_zeichen)
