from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Chatbot logic with only if-else ---
def chatbot_response(user_input):
    user_input = user_input.lower()

    # --- Greetings ---
    if "hello" in user_input or "hi" in user_input:
        return "Hello! I can answer math questions and tell you about AI. Ask me something!"

    elif "your name" in user_input:
        return "I am your chatbot assistant."

    elif "bye" in user_input:
        return "Goodbye! Have a wonderful day!"

    # --- AI Knowledge ---
    elif "what is ai" in user_input or "ai" in user_input:
        return "AI (Artificial Intelligence) is the simulation of human intelligence by machines."
    elif "machine learning" in user_input:
        return "Machine Learning is a subset of AI that enables machines to learn from data without explicit programming."
    elif "deep learning" in user_input:
        return "Deep Learning is a branch of machine learning using neural networks with many layers to model complex patterns."
    elif "neural network" in user_input:
        return "A Neural Network is a system of algorithms inspired by the human brain that recognizes patterns."
    elif "natural language processing" in user_input or "nlp" in user_input:
        return "Natural Language Processing (NLP) is a field of AI that helps machines understand and process human language."

    # --- Basic Math ---
    elif "add" in user_input or "+" in user_input:
        parts = [int(s) for s in user_input.replace("+", " ").split() if s.isdigit()]
        if len(parts) == 2:
            return f"The answer is {parts[0] + parts[1]}"
        return "Please ask like: add 5 and 10"

    elif "subtract" in user_input or "-" in user_input:
        parts = [int(s) for s in user_input.replace("-", " ").split() if s.isdigit()]
        if len(parts) == 2:
            return f"The answer is {parts[0] - parts[1]}"
        return "Please ask like: subtract 10 and 5"

    elif "multiply" in user_input or "into" in user_input or "times" in user_input or "*" in user_input:
        parts = [int(s) for s in user_input.replace("*", " ").split() if s.isdigit()]
        if len(parts) == 2:
            return f"The answer is {parts[0] * parts[1]}"
        return "Please ask like: multiply 4 and 6"

    elif "divide" in user_input or "divided by" in user_input or "/" in user_input:
        parts = [int(s) for s in user_input.replace("/", " ").split() if s.isdigit()]
        if len(parts) == 2:
            if parts[1] == 0:
                return "Division by zero is not allowed."
            return f"The answer is {parts[0] / parts[1]}"
        return "Please ask like: divide 20 by 5"

    elif "square root" in user_input:
        for word in user_input.split():
            if word.isdigit():
                num = int(word)
                return f"The square root of {num} is {num**0.5}"
        return "Please ask like: square root of 25"

    elif "square" in user_input:
        for word in user_input.split():
            if word.isdigit():
                num = int(word)
                return f"The square of {num} is {num**2}"
        return "Please ask like: square of 7"

    # --- Fallback ---
    else:
        return "I can answer basic math (add, subtract, multiply, divide, square, square root) and basic AI concepts (AI, ML, Deep Learning, NLP). Try asking me!"
    

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
