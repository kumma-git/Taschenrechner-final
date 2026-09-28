```html
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Wissenschaftlicher Taschenrechner</title>

<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        user-select: none;
    }

    body {
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background:
            radial-gradient(circle at top, #252a32 0%, #111318 45%, #08090b 100%);
        font-family: Arial, Helvetica, sans-serif;
        color: white;
    }

    .calculator {
        width: 390px;
        padding: 18px;
        border-radius: 25px;
        background: #20242a;
        box-shadow:
            0 25px 60px rgba(0,0,0,0.65),
            inset 0 1px 1px rgba(255,255,255,0.08);
    }

    .brand {
        text-align: center;
        margin-bottom: 12px;
        color: #d7d9dc;
        font-size: 17px;
        font-weight: bold;
        letter-spacing: 2px;
    }

    .model {
        text-align: center;
        font-size: 11px;
        color: #858a91;
        margin-bottom: 12px;
    }

    .display-frame {
        background: #0c0e10;
        border-radius: 12px;
        padding: 9px;
        margin-bottom: 13px;
        border: 2px solid #33383f;
    }

    .status {
        height: 18px;
        color: #9da3a9;
        font-size: 12px;
        display: flex;
        justify-content: space-between;
        padding: 0 5px;
    }

    .display {
        height: 70px;
        background: #c9d0bd;
        color: #10130e;
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding: 8px 12px;
        font-family: "Courier New", monospace;
        font-size: 32px;
        overflow: hidden;
        white-space: nowrap;
        box-shadow:
            inset 0 0 8px rgba(0,0,0,0.3);
    }

    .buttons {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 8px;
    }

    button {
        height: 53px;
        border: none;
        border-radius: 10px;
        background: #343940;
        color: #f1f1f1;
        font-size: 17px;
        font-weight: bold;
        cursor: pointer;
        box-shadow:
            0 4px 0 #17191d,
            inset 0 1px 1px rgba(255,255,255,0.08);
        transition: 0.08s;
    }

    button:hover {
        background: #41464e;
    }

    button:active {
        transform: translateY(3px);
        box-shadow: 0 1px 0 #17191d;
    }

    .function {
        background: #292d33;
        font-size: 14px;
    }

    .function:hover {
        background: #383d44;
    }

    .operator {
        background: #3d4249;
        font-size: 21px;
    }

    .operator:hover {
        background: #4b5159;
    }

    .orange {
        background: #d97813;
    }

    .orange:hover {
        background: #ec8a1d;
    }

    .red {
        background: #b93333;
    }

    .red:hover {
        background: #d04444;
    }

    .green {
        background: #287b46;
    }

    .green:hover {
        background: #329657;
    }

    .wide {
        grid-column: span 2;
    }

    .footer {
        text-align: center;
        color: #656a71;
        font-size: 10px;
        margin-top: 15px;
    }

    @media (max-width: 430px) {
        .calculator {
            width: 95%;
        }

        button {
            height: 48px;
        }

        .display {
            font-size: 27px;
        }
    }
</style>
</head>

<body>

<div class="calculator">

    <div class="brand">CASIO</div>
    <div class="model">SCIENTIFIC CALCULATOR</div>

    <div class="display-frame">

        <div class="status">
            <span id="mode">DEG</span>
            <span id="memory">M</span>
        </div>

        <div class="display" id="display">0</div>

    </div>

    <div class="buttons">

        <!-- Zeile 1 -->
        <button class="function" onclick="toggleAngle()">DEG/RAD</button>
        <button class="function" onclick="insertFunction('sin')">sin</button>
        <button class="function" onclick="insertFunction('cos')">cos</button>
        <button class="function" onclick="insertFunction('tan')">tan</button>
        <button class="red" onclick="clearAll()">AC</button>

        <!-- Zeile 2 -->
        <button class="function" onclick="insertFunction('asin')">sin⁻¹</button>
        <button class="function" onclick="insertFunction('acos')">cos⁻¹</button>
        <button class="function" onclick="insertFunction('atan')">tan⁻¹</button>
        <button class="function" onclick="square()">x²</button>
        <button class="operator" onclick="backspace()">⌫</button>

        <!-- Zeile 3 -->
        <button class="function" onclick="insertText('√(')">√</button>
        <button class="function" onclick="insertText('π')">π</button>
        <button class="function" onclick="insertText('(')">(</button>
        <button class="function" onclick="insertText(')')">)</button>
        <button class="function" onclick="percentage()">%</button>

        <!-- Zeile 4 -->
        <button onclick="insertNumber('7')">7</button>
        <button onclick="insertNumber('8')">8</button>
        <button onclick="insertNumber('9')">9</button>
        <button class="operator" onclick="insertText('÷')">÷</button>
        <button class="operator" onclick="insertText('^')">xʸ</button>

        <!-- Zeile 5 -->
        <button onclick="insertNumber('4')">4</button>
        <button onclick="insertNumber('5')">5</button>
        <button onclick="insertNumber('6')">6</button>
        <button class="operator" onclick="insertText('×')">×</button>
        <button class="function" onclick="insertText('!')">x!</button>

        <!-- Zeile 6 -->
        <button onclick="insertNumber('1')">1</button>
        <button onclick="insertNumber('2')">2</button>
        <button onclick="insertNumber('3')">3</button>
        <button class="operator" onclick="insertText('-')">−</button>
        <button class="function" onclick="insertText('e')">e</button>

        <!-- Zeile 7 -->
        <button class="wide" onclick="insertNumber('0')">0</button>
        <button onclick="insertText('.')">.</button>
        <button class="operator" onclick="insertText('+')">+</button>
        <button class="green" onclick="calculate()">=</button>

        <!-- Zeile 8 -->
        <button class="function wide" onclick="toggleSign()">+/−</button>
        <button class="function" onclick="insertFunction('log')">log</button>
        <button class="function" onclick="insertFunction('ln')">ln</button>

    </div>

    <div class="footer">
        Wissenschaftlicher Taschenrechner
    </div>

</div>

<script>

let expression = "";
let angleMode = "DEG";

const display = document.getElementById("display");
const modeDisplay = document.getElementById("mode");


// ------------------------------------
// DISPLAY
// ------------------------------------

function updateDisplay() {

    display.textContent = expression || "0";

}


// ------------------------------------
// ZAHLEN
// ------------------------------------

function insertNumber(number) {

    expression += number;
    updateDisplay();

}


// ------------------------------------
// TEXT EINFÜGEN
// ------------------------------------

function insertText(text) {

    expression += text;
    updateDisplay();

}


// ------------------------------------
// FUNKTIONEN
// ------------------------------------

function insertFunction(func) {

    expression += func + "(";
    updateDisplay();

}


// ------------------------------------
// LÖSCHEN
// ------------------------------------

function clearAll() {

    expression = "";
    updateDisplay();

}


// ------------------------------------
// RÜCKTASTE
// ------------------------------------

function backspace() {

    expression = expression.slice(0, -1);
    updateDisplay();

}


// ------------------------------------
// DEG / RAD
// ------------------------------------

function toggleAngle() {

    if (angleMode === "DEG") {
        angleMode = "RAD";
    } else {
        angleMode = "DEG";
    }

    modeDisplay.textContent = angleMode;

}


// ------------------------------------
// QUADRAT
// ------------------------------------

function square() {

    expression += "^2";
    updateDisplay();

}


// ------------------------------------
// PROZENT
// ------------------------------------

function percentage() {

    expression += "/100";
    updateDisplay();

}


// ------------------------------------
// PLUS / MINUS
// ------------------------------------

function toggleSign() {

    if (expression === "") {
        expression = "-";
    } else {
        expression = "-(" + expression + ")";
    }

    updateDisplay();

}


// ------------------------------------
// FAKULTÄT
// ------------------------------------

function factorial(n) {

    if (n < 0 || !Number.isInteger(n)) {
        throw new Error();
    }

    if (n === 0 || n === 1) {
        return 1;
    }

    let result = 1;

    for (let i = 2; i <= n; i++) {
        result *= i;
    }

    return result;

}


// ------------------------------------
// WINKEL
// ------------------------------------

function toRadians(value) {

    if (angleMode === "DEG") {
        return value * Math.PI / 180;
    }

    return value;

}


function fromRadians(value) {

    if (angleMode === "DEG") {
        return value * 180 / Math.PI;
    }

    return value;

}


// ------------------------------------
// AUSDRUCK UMBAUEN
// ------------------------------------

function prepareExpression(input) {

    let exp = input;

    // Multiplikationszeichen
    exp = exp.replace(/×/g, "*");
    exp = exp.replace(/÷/g, "/");

    // Pi
    exp = exp.replace(/π/g, "Math.PI");

    // Euler Zahl
    exp = exp.replace(/\be\b/g, "Math.E");

    // Potenz
    while (exp.includes("^")) {
        exp = exp.replace(
            /(\d+(?:\.\d+)?|\([^()]+\))\^(\d+(?:\.\d+)?|\([^()]+\))/,
            "Math.pow($1,$2)"
        );

        if (!exp.includes("^")) {
            break;
        }
    }

    // Quadratwurzel
    exp = exp.replace(/√\(/g, "Math.sqrt(");

    // Logarithmus
    exp = exp.replace(/log\(/g, "Math.log10(");
    exp = exp.replace(/ln\(/g, "Math.log(");

    // Sinus
    exp = exp.replace(
        /sin\(([^()]*)\)/g,
        function(match, value) {
            return "Math.sin(toRadians(" + value + "))";
        }
    );

    // Cosinus
    exp = exp.replace(
        /cos\(([^()]*)\)/g,
        function(match, value) {
            return "Math.cos(toRadians(" + value + "))";
        }
    );

    // Tangens
    exp = exp.replace(
        /tan\(([^()]*)\)/g,
        function(match, value) {
            return "Math.tan(toRadians(" + value + "))";
        }
    );

    // Arcus Sinus
    exp = exp.replace(
        /asin\(([^()]*)\)/g,
        function(match, value) {
            return "fromRadians(Math.asin(" + value + "))";
        }
    );

    // Arcus Cosinus
    exp = exp.replace(
        /acos\(([^()]*)\)/g,
        function(match, value) {
            return "fromRadians(Math.acos(" + value + "))";
        }
    );

    // Arcus Tangens
    exp = exp.replace(
        /atan\(([^()]*)\)/g,
        function(match, value) {
            return "fromRadians(Math.atan(" + value + "))";
        }
    );

    // Fakultät
    exp = exp.replace(
        /(\d+(?:\.\d+)?)!/g,
        "factorial($1)"
    );

    return exp;

}


// ------------------------------------
// BERECHNEN
// ------------------------------------

function calculate() {

    if (!expression) {
        return;
    }

    try {

        let prepared = prepareExpression(expression);

        let result = Function(
            "toRadians",
            "fromRadians",
            "factorial",
            "return " + prepared
        )(toRadians, fromRadians, factorial);

        if (!Number.isFinite(result)) {
            throw new Error();
        }

        result = Number(result.toPrecision(12));

        expression = String(result);

        updateDisplay();

    } catch (error) {

        display.textContent = "Fehler";

        setTimeout(() => {
            expression = "";
            updateDisplay();
        }, 1000);

    }

}


// ------------------------------------
// TASTATUR
// ------------------------------------

document.addEventListener("keydown", function(event) {

    const key = event.key;

    if (key >= "0" && key <= "9") {

        insertNumber(key);

    }

    else if (key === ".") {

        insertText(".");

    }

    else if (key === "+") {

        insertText("+");

    }

    else if (key === "-") {

        insertText("-");

    }

    else if (key === "*") {

        insertText("×");

    }

    else if (key === "/") {

        event.preventDefault();
        insertText("÷");

    }

    else if (key === "^") {

        insertText("^");

    }

    else if (key === "(") {

        insertText("(");

    }

    else if (key === ")") {

        insertText(")");

    }

    else if (key === "%") {

        percentage();

    }

    else if (key === "Enter" || key === "=") {

        calculate();

    }

    else if (key === "Backspace") {

        backspace();

    }

    else if (key === "Escape") {

        clearAll();

    }

});

</script>

</body>
</html>
```
