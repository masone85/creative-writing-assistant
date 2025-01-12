from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    genre = request.form.get("genre", "general")
    theme = request.form.get("theme", "adventure")
    character = request.form.get("character", "a curious hero")
    prompt = f"Write a creative story in the {genre} genre about {theme}, featuring {character}."

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7,
        )
        return {"outline": response.choices[0].text.strip()}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
