from flask import Flask, render_template, request, jsonify
import math
import re

app = Flask(__name__)

# --- Chatbot logic ---
def chatbot_response(user_input):
    user_input_lower = user_input.lower().strip()

    # --- Greetings ---
    if re.search(r"\b(hello|hi|hey)\b", user_input_lower):
        return "Hello! I’m Freddy 🤖. I can solve math problems, answer IT-related questions, and tell you about animals and birds. Ask me anything!"
    elif "your name" in user_input_lower:
        return "I’m Freddy, your friendly chatbot assistant!"
    elif "bye" in user_input_lower:
        return "Goodbye! Have a great day! 👋"

    # --- AI & IT Knowledge ---
    if "what is ai" in user_input_lower:
        return "AI (Artificial Intelligence) means machines performing tasks that usually require human intelligence."
    elif "machine learning" in user_input_lower:
        return "Machine Learning is a branch of AI that teaches computers to learn from data."
    elif "deep learning" in user_input_lower:
        return "Deep Learning is a type of machine learning that uses multi-layered neural networks."
    elif "nlp" in user_input_lower or "natural language processing" in user_input_lower:
        return "NLP enables computers to understand, interpret, and generate human language."

    # --- Programming Languages Knowledge ---
    elif "python" in user_input_lower:
        return "Python is a versatile programming language widely used for web development, data analysis, AI, and automation."
    elif "java" in user_input_lower:
        return "Java is a robust, object-oriented language used for building enterprise applications and Android apps."
    elif "html" in user_input_lower:
        return "HTML (HyperText Markup Language) is used to structure web pages."
    elif "css" in user_input_lower:
        return "CSS (Cascading Style Sheets) is used to style web pages and make them visually appealing."
    elif "javascript" in user_input_lower:
        return "JavaScript is used to make web pages interactive and dynamic."
    elif "c++" in user_input_lower or "cpp" in user_input_lower:
        return "C++ is a powerful, fast, object-oriented language often used for system programming and game development."
    elif "sql" in user_input_lower:
        return "SQL (Structured Query Language) is used to manage and query data in databases."

    # --- Animal & Bird Knowledge ---
    elif "lion" in user_input_lower:
        return "The lion 🦁 is known as the king of the jungle and is a powerful carnivore found in Africa and Asia."
    elif "elephant" in user_input_lower:
        return "Elephants 🐘 are the largest land animals, known for their intelligence and memory."
    elif "dog" in user_input_lower:
        return "Dogs 🐶 are loyal companions and come in many breeds, known for their intelligence and affection."
    elif "cat" in user_input_lower:
        return "Cats 🐱 are independent and curious animals, often kept as pets."
    elif "parrot" in user_input_lower:
        return "Parrots 🦜 are colorful birds known for their ability to mimic sounds and human speech."
    elif "peacock" in user_input_lower:
        return "Peacocks 🦚 are famous for their beautiful, colorful tail feathers and are the national bird of India."
    elif "eagle" in user_input_lower:
        return "Eagles 🦅 are powerful birds of prey known for their sharp eyesight and hunting skills."

    # --- Food & Cuisine Knowledge ---
    elif "pizza" in user_input_lower:
        return "Pizza 🍕 is an Italian dish made with dough, tomato sauce, cheese, and toppings."
    elif "sushi" in user_input_lower:
        return "Sushi 🍣 is a Japanese dish made with vinegared rice, seafood, and vegetables."
    elif "biryani" in user_input_lower:
        return "Biryani 🍛 is a South Asian rice dish made with aromatic spices and meat or vegetables."
    elif "pasta" in user_input_lower:
        return "Pasta 🍝 is a staple Italian dish made from wheat flour, served with sauces like tomato or Alfredo."
    elif "taco" in user_input_lower:
        return "Tacos 🌮 are a Mexican dish made with tortillas filled with meat, beans, and cheese."

    # --- Math Solver (Basic to Moderate) ---
    try:
        expr = (
            user_input_lower.replace("plus", "+")
            .replace("minus", "-")
            .replace("times", "*")
            .replace("into", "*")
            .replace("multiplied by", "*")
            .replace("divide", "/")
            .replace("divided by", "/")
            .replace("square root of", "math.sqrt")
            .replace("power of", "**")
            .replace("^", "**")
        )

        # Support for functions like sin, cos, log, etc.
        math_context = {
            "math": math,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e
        }

        if any(op in expr for op in ["+", "-", "*", "/", "**", "sqrt", "sin", "cos", "tan", "log"]):
            result = eval(expr, {"__builtins__": None}, math_context)
            return f"The answer is {result}"
    except Exception:
        pass

    # --- Fallback ---
    return "I can help you with math (basic to moderate), IT-related questions, and info about animals, birds, and food! Try asking: 'What is Python?', 'sin(30)', or 'Tell me about lions'."

# --- Routes ---
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
