from flask import Flask, render_template, request
import random, os, requests, json

app = Flask(__name__)

# Vocabulary data
# fetch from ChatGPT
API_KEY = os.environ.get("CHATGPT_API_KEY")

big_prompt = """
Please give me an SAT Hard 5000 vocabulary flashcard quiz with 4 choices like a multiple choice 
question where the first choice is always the correct answer but when shuffled 
so it acts as a flashcard revising system.  Give me at least 10 such problems.

Your output must conform to this format such that it can be parsed directly into a python dictionary by the json module.
Do not include any extra text or explanations.  Your replay must be only JSON that can be parsed into a dictionary directly with no cleaning:
vocab_data = {
        "Aberration": [
            "A departure from what is normal",
            "A type of music genre",
            "A scientific theory",
            "A type of flower"
        ]}

"""
API_URL = 'https://api.openai.com/v1/chat/completions'


def get_gpt_output(prompt):
    print("Getting ChatGPT output...")
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "gpt-4o-mini",  # or "gpt-4" if you have access
        "messages": [
            {"role": "system", "content": "You are a helpful English professor."},
            {"role": "user", "content": f"{prompt}"}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    vocab_data = {"ERROR": "No GPT Data Available"}
    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
        reply = reply.replace("```", '')
        reply = reply.replace("json", '')
        vocab_data = json.loads(reply)
    return vocab_data

vocab_data = get_gpt_output(big_prompt)
print(vocab_data)
@app.route("/")
def quiz():
    word, options = random.choice(list(vocab_data.items()))
    correct_answer = options[0]
    shuffled_options = options[:]
    random.shuffle(shuffled_options)

    return render_template("quiz.html", word=word, options=shuffled_options, correct=correct_answer)

@app.route("/result", methods=["POST"])
def result():
    selected = request.form.get("choice")
    correct = request.form.get("correct")

    if selected == correct:
        message = "Congrats! You got it right."
    else:
        message = f"Wrong! The correct answer was: {correct}"

    return render_template("result.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
