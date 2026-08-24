import streamlit as st
import math

st.set_page_config(
    page_title="Taschenrechner von Maksym",
    page_icon="🧮",
    layout="centered"
)

# Design im Casio FX Style
st.markdown("""
<style>
    /* Gesamthintergrund */
    .stApp {
        background-color: #0d0f12;
        color: #e0e0e0;
    }
    
    /* Rechner-Gehäuse */
    .main .block-container {
        max-width: 410px;
        padding: 24px 18px 30px 18px;
        background: radial-gradient(circle at 50% 0%, #2b303c 0%, #171920 100%);
        border-radius: 32px;
        border: 2px solid #363c4a;
        box-shadow: 0px 25px 60px rgba(0, 0, 0, 0.9), inset 0px 1px 2px rgba(255, 255, 255, 0.15);
        margin-top: 15px;
        margin-bottom: 15px;
    }
    
    /* Titel */
    h1 {
        text-align: center;
        color: #c5cbd3;
        font-family: Arial, sans-serif;
        font-size: 18px;
        font-weight: 800;
        letter-spacing: 2px;
        margin-top: 0px;
        margin-bottom: 12px;
        text-transform: uppercase;
    }
    
    /* LCD Bildschirm */
    .lcd-screen {
        background: linear-gradient(180deg, #9eb3a0 0%, #8ca18e 100%);
        color: #121c13;
        border-radius: 6px;
        padding: 10px 14px;
        margin-bottom: 18px;
        text-align: right;
        font-family: 'Courier New', monospace;
        font-size: 28px;
        font-weight: bold;
        min-height: 65px;
        box-shadow: inset 3px 3px 6px rgba(0,0,0,0.5), inset -2px -2px 4px rgba(255,255,255,0.3);
        border: 3px solid #111113;
    }

    .lcd-sub {
        font-size: 11px;
        color: #2b3a2d;
        text-align: left;
        font-family: sans-serif;
        font-weight: bold;
    }

    /* Standard-Button Basis (Wissenschaftliche Tasten) */
    div.stButton > button {
        width: 100%;
        height: 36px;
        border-radius: 12px / 8px; /* Ovalere Wölbung */
        border: 1px solid #181a20;
        background: linear-gradient(180deg, #3d4352 0%, #252933 100%);
        color: #d1d5db;
        font-size: 13px;
        font-weight: bold;
        box-shadow: 0px 4px 0px #111318, 0px 5px 6px rgba(0,0,0,0.6);
        transition: all 0.05s ease;
        margin-bottom: 6px;
    }
    
    div.stButton > button:active {
        transform: translateY(3px);
        box-shadow: 0px 1px 0px #111318, 0px 2px 3px rgba(0,0,0,0.6);
    }

    /* Ziffern-Tasten (Helle Tasten) */
    .btn-num div.stButton > button {
        height: 44px;
        border-radius: 6px;
        background: linear-gradient(180deg, #f2f4f7 0%, #cbd1d9 100%);
        color: #111827;
        font-size: 19px;
        box-shadow: 0px 4px 0px #8b929e, 0px 5px 8px rgba(0,0,0,0.5);
    }
    .btn-num div.stButton > button:hover {
        background: linear-gradient(180deg, #ffffff 0%, #d8deee 100%);
        color: #000000;
    }

    /* Operatoren-Tasten (+, -, ×, ÷) */
    .btn-op div.stButton > button {
        height: 44px;
        border-radius: 6px;
        background: linear-gradient(180deg, #e2e8f0 0%, #b8c1cc 100%);
        color: #000000;
        font-size: 18px;
        box-shadow: 0px 4px 0px #7a828e, 0px 5px 8px rgba(0,0,0,0.5);
    }

    /* DEL / AC Tasten (Blau) */
    .btn-del div.stButton > button, .btn-ac div.stButton > button {
        height: 44px;
        border-radius: 6px;
        background: linear-gradient(180deg, #3b82f6 0%, #1d4ed8 100%);
        color: #ffffff;
        font-size: 15px;
        box-shadow: 0px 4px 0px #1e3a8a, 0px 5px 8px rgba(0,0,0,0.5);
    }

    /* Gleichheitszeichen = */
    .btn-eq div.stButton > button {
        height: 44px;
        border-radius: 6px;
        background: linear-gradient(180deg, #e2e8f0 0%, #b8c1cc 100%);
        color: #000000;
        font-size: 20px;
        box-shadow: 0px 4px 0px #7a828e, 0px 5px 8px rgba(0,0,0,0.5);
    }
</style>
""", unsafe_allow_html=True)

# Session State
if "display" not in st.session_state:
    st.session_state.display = "0"
if "reset_next" not in st.session_state:
    st.session_state.reset_next = False

def add_char(char):
    if st.session_state.reset_next:
        if char in ["+", "−", "×", "÷", "^"]:
            st.session_state.reset_next = False
        else:
            st.session_state.display = ""
            st.session_state.reset_next = False
        
    if st.session_state.display == "0" and char not in [".", "+", "−", "×", "÷", "^"]:
        st.session_state.display = char
    else:
        st.session_state.display += char

def clear_all():
    st.session_state.display = "0"
    st.session_state.reset_next = False

def delete_char():
    if len(st.session_state.display) > 1 and not st.session_state.reset_next:
        st.session_state.display = st.session_state.display[:-1]
    else:
        st.session_state.display = "0"
        st.session_state.reset_next = False

def calculate():
    expr = st.session_state.display
    try:
        expr_clean = expr.replace("×", "*").replace("÷", "/").replace("−", "-").replace("^", "**")
        res = eval(expr_clean, {"__builtins__": None}, {"sin": math.sin, "cos": math.cos, "tan": math.tan, "sqrt": math.sqrt})
        if res == int(res):
            st.session_state.display = str(int(res))
        else:
            st.session_state.display = str(round(res, 8))
    except Exception:
        st.session_state.display = "Fehler"
    st.session_state.reset_next = True

# UI
st.title("Taschenrechner von Maksym")

st.markdown(
    f'<div class="lcd-screen"><div class="lcd-sub">CLASSWIZ</div>{st.session_state.display}</div>',
    unsafe_allow_html=True
)

# Funktions-Buttons oben (kleiner & rundlich)
sci_rows = [
    [("x²", "^2"), ("xⁿ", "^"), ("sin", "sin("), ("cos", "cos("), ("tan", "tan(")],
    [("√", "sqrt("), ("log", "log("), ("ln", "ln("), ("(", "("), (")", ")")]
]

for row in sci_rows:
    cols = st.columns(5)
    for idx, (label, val) in enumerate(row):
        with cols[idx]:
            st.button(label, key=f"btn_{label}", on_click=add_char, args=(val,))

st.write("")

# Haupt-Tastenfeld
num_grid = [
    [("7", "num"), ("8", "num"), ("9", "num"), ("DEL", "del"), ("AC", "ac")],
    [("4", "num"), ("5", "num"), ("6", "num"), ("×", "op"), ("÷", "op")],
    [("1", "num"), ("2", "num"), ("3", "num"), ("+", "op"), ("−", "op")],
    [("0", "num"), (".", "num"), ("%", "op"), ("Ans", "op"), ("=", "eq")]
]

for row in num_grid:
    cols = st.columns(5)
    for idx, (label, btn_style) in enumerate(row):
        with cols[idx]:
            st.markdown(f'<div class="btn-{btn_style}">', unsafe_allow_html=True)
            if label == "AC":
                st.button(label, key="btn_AC", on_click=clear_all)
            elif label == "DEL":
                st.button(label, key="btn_DEL", on_click=delete_char)
            elif label == "=":
                st.button(label, key="btn_EQ", on_click=calculate)
            else:
                st.button(label, key=f"btn_{label}", on_click=add_char, args=(label,))
            st.markdown('</div>', unsafe_allow_html=True)
