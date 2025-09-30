from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# --- Chatbot logic ---
def chatbot_response(user_input):
    user_input_lower = user_input.lower()

    # --- Greetings ---
    if "hello" in user_input_lower or "hi" in user_input_lower:
        return "Hello! I am Freddy 🤖. I can answer math questions and tell you about food and cuisines. Ask me something!"
    elif "your name" in user_input_lower:
        return "I am Freddy, your smart chatbot assistant."
    elif "bye" in user_input_lower:
        return "Goodbye! Have a wonderful day!"

    # --- AI Knowledge ---
    elif "what is ai" in user_input_lower or "ai" in user_input_lower:
        return "AI (Artificial Intelligence) is the simulation of human intelligence by machines."
    elif "machine learning" in user_input_lower:
        return "Machine Learning is a subset of AI that enables machines to learn from data without explicit programming."
    elif "deep learning" in user_input_lower:
        return "Deep Learning is a branch of machine learning using neural networks with many layers to model complex patterns."
    elif "nlp" in user_input_lower or "natural language processing" in user_input_lower:
        return "NLP (Natural Language Processing) helps machines understand and process human language."

    # --- Food & Cuisine Knowledge ---
    elif "pizza" in user_input_lower:
        return "Pizza is an Italian dish made with a flatbread base, tomato sauce, cheese, and various toppings."
    elif "sushi" in user_input_lower:
        return "Sushi is a Japanese dish made with vinegared rice, seafood, and vegetables."
    elif "biryani" in user_input_lower:
        return "Biryani is a popular South Asian dish made with rice, spices, and meat or vegetables."
    elif "pasta" in user_input_lower:
        return "Pasta is a staple of Italian cuisine, typically served with sauces like tomato, pesto, or Alfredo."
    elif "taco" in user_input_lower:
        return "Tacos are a traditional Mexican dish made with tortillas filled with meat, beans, cheese, and vegetables."
    elif "cuisine" in user_input_lower:
        return "Different cuisines include Italian (pasta, pizza), Indian (biryani, curry), Japanese (sushi, ramen), and Mexican (tacos, burritos). Which one interests you?"

    # --- Complex Math Solver ---
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
        )
        if any(op in expr for op in ["+", "-", "*", "/", "**", "sqrt"]):
            result = eval(expr, {"__builtins__": None, "math": math})
            return f"The answer is {result}"
    except Exception:
        pass

    # --- Fallback ---
    return "I can help with complex math, AI basics, and information about food & cuisines. Try asking me something like 'What is AI?', 'square root of 144', or 'Tell me about sushi'."


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
