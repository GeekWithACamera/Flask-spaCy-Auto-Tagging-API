from flask import Flask, request, jsonify
import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_md")

app = Flask(__name__)

# Auto-tagging function
def generate_tags(text):
    doc = nlp(text)
    tags = list(set(ent.text for ent in doc.ents))  # Extract unique named entities
    return tags

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    tags = generate_tags(text)
    return jsonify({"tags": tags})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
