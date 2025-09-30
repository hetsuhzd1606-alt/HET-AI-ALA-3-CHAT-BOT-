from flask import Flask, render_template, request, jsonify
from langdetect import detect

app = Flask(__name__)

# --- Chatbot logic with only if-else ---
def chatbot_response(user_input):
    try:
        lang = detect(user_input)
    except:
        lang = "en"

    user_input_lower = user_input.lower()

    # --- English Responses ---
    if lang == "en":
        if "hello" in user_input_lower or "hi" in user_input_lower:
            return "Hello! I can answer math questions and tell you about AI. Ask me something!"
        elif "your name" in user_input_lower:
            return "I am Freddy, your chatbot assistant."
        elif "bye" in user_input_lower:
            return "Goodbye! Have a wonderful day!"
        elif "what is ai" in user_input_lower or "ai" in user_input_lower:
            return "AI (Artificial Intelligence) is the simulation of human intelligence by machines."
        elif "machine learning" in user_input_lower:
            return "Machine Learning is a subset of AI that enables machines to learn from data without explicit programming."
        elif "deep learning" in user_input_lower:
            return "Deep Learning is a branch of machine learning using neural networks with many layers to model complex patterns."
        elif "nlp" in user_input_lower or "natural language processing" in user_input_lower:
            return "NLP helps computers understand human language."
        elif "add" in user_input_lower or "+" in user_input_lower:
            parts = [int(s) for s in user_input_lower.replace("+", " ").split() if s.isdigit()]
            if len(parts) == 2:
                return f"The answer is {parts[0] + parts[1]}"
            return "Please ask like: add 5 and 10"
        else:
            return "I can answer math (add, subtract, multiply, divide, square) and AI basics. Try asking me!"

    # --- Hindi Responses ---
    elif lang == "hi":
        if "namaste" in user_input_lower or "hello" in user_input_lower:
            return "नमस्ते! मैं गणित और AI से जुड़े प्रश्नों का उत्तर दे सकता हूँ।"
        elif "tumhara naam" in user_input_lower or "name" in user_input_lower:
            return "मेरा नाम Freddy है।"
        elif "alvida" in user_input_lower or "bye" in user_input_lower:
            return "अलविदा! आपका दिन शुभ हो।"
        elif "ai" in user_input_lower:
            return "AI का मतलब कृत्रिम बुद्धिमत्ता है।"
        elif "jodo" in user_input_lower or "add" in user_input_lower:
            return "जोड़ने के लिए कृपया उदाहरण दें: 5 + 10"
        else:
            return "मैं गणित और AI के बारे में हिंदी में भी बता सकता हूँ।"

    # --- Spanish Responses ---
    elif lang == "es":
        if "hola" in user_input_lower:
            return "¡Hola! Puedo responder preguntas de matemáticas y de IA."
        elif "tu nombre" in user_input_lower:
            return "Mi nombre es Freddy."
        elif "adiós" in user_input_lower or "bye" in user_input_lower:
            return "¡Adiós! Que tengas un gran día."
        elif "ai" in user_input_lower:
            return "La IA es inteligencia artificial: máquinas que imitan la inteligencia humana."
        elif "sumar" in user_input_lower or "add" in user_input_lower:
            return "Por favor pregunta como: sumar 5 y 10"
        else:
            return "Puedo responder preguntas de matemáticas y conceptos básicos de IA en español."

    # --- Fallback ---
    else:
        return f"Sorry, I don’t support full responses in '{lang}' yet. Try English, Hindi, or Spanish."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.json.get("message")
    bot_reply = chatbot_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
