import streamlit as st

# Seiteneinstellungen
st.set_page_config(
    page_title="Taschenrechner von Maksym",
    page_icon="🧮",
    layout="centered"
)

# Eigenes Design
st.markdown("""
<style>
    /* Gesamter Hintergrund */
    .stApp {
        background-color: white;
    }

    /* Hauptbereich */
    .main .block-container {
        max-width: 700px;
        padding-top: 40px;
    }

    /* Überschrift */
    h1 {
        color: #111111;
        text-align: center;
        font-family: Arial, sans-serif;
        margin-bottom: 35px;
    }

    /* Beschriftungen */
    label, .stMarkdown p {
        color: #222222 !important;
        font-size: 16px;
    }

    /* Eingabefelder */
    input {
        background-color: #f5f5f5 !important;
        color: #111111 !important;
        border: 1px solid #bbbbbb !important;
        border-radius: 8px !important;
    }

    /* Alle Buttons */
    div.stButton > button {
        width: 100%;
        height: 48px;
        border-radius: 8px;
        border: 1px solid #222222;
        background-color: white;
        color: #111111;
        font-size: 18px;
        font-weight: bold;
    }

    /* Button beim Darüberfahren */
    div.stButton > button:hover {
        background-color: #222222;
        color: white;
        border-color: #222222;
    }

    /* Ergebnisfeld */
    .result-box {
        background-color: black;
        color: white;
        padding: 22px;
        border-radius: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    /* Rechnen-Button */
    .calculate-button button {
        background-color: black !important;
        color: white !important;
        border: 1px solid black !important;
        margin-top: 20px;
    }

    .calculate-button button:hover {
        background-color: #333333 !important;
    }
</style>
""", unsafe_allow_html=True)


# Titel
st.title("Taschenrechner von Maksym")

# Zahlen eingeben
zahl1 = st.number_input(
    "Erste Zahl",
    value=0.0,
    step=1.0,
    format="%.2f"
)

zahl2 = st.number_input(
    "Zweite Zahl",
    value=0.0,
    step=1.0,
    format="%.2f"
)

# Anfangswert für die ausgewählte Operation
if "operation" not in st.session_state:
    st.session_state.operation = "+"

# Überschrift für Operationen
st.markdown("### Rechenart auswählen")

# Operationsbuttons
spalte1, spalte2, spalte3, spalte4 = st.columns(4)

with spalte1:
    if st.button("+"):
        st.session_state.operation = "+"

with spalte2:
    if st.button("-"):
        st.session_state.operation = "-"

with spalte3:
    if st.button("×"):
        st.session_state.operation = "*"

with spalte4:
    if st.button("÷"):
        st.session_state.operation = "/"

st.write(
    f"Aktuelle Rechenart: **{st.session_state.operation}**"
)

# Berechnung
with st.container():
    st.markdown('<div class="calculate-button">', unsafe_allow_html=True)
    berechnen = st.button("Berechnen")
    st.markdown("</div>", unsafe_allow_html=True)

if berechnen:
    operation = st.session_state.operation

    if operation == "+":
        ergebnis = zahl1 + zahl2

    elif operation == "-":
        ergebnis = zahl1 - zahl2

    elif operation == "*":
        ergebnis = zahl1 * zahl2

    elif operation == "/":
        if zahl2 == 0:
            st.error("Eine Division durch 0 ist nicht möglich.")
            ergebnis = None
        else:
            ergebnis = zahl1 / zahl2

    if ergebnis is not None:
        # Ganze Zahlen ohne Nachkommastellen anzeigen
        if ergebnis == int(ergebnis):
            ergebnis_text = str(int(ergebnis))
        else:
            ergebnis_text = f"{ergebnis:.2f}"

        st.markdown(
            f'<div class="result-box">Ergebnis: {ergebnis_text}</div>',
            unsafe_allow_html=True
        )
