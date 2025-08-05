from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Vocabulary data
vocab_data = {
    "Aberration": [
        "A departure from what is normal",
        "A type of music genre",
        "A scientific theory",
        "A type of flower"
    ],
    "Belligerent": [
        "Hostile and aggressive",
        "Nice and pleasant",
        "A form of poetry",
        "A musical term"
    ],
    "Cacophony": [
        "A harsh, discordant mixture of sounds",
        "A cooking technique",
        "A type of sport",
        "A type of dance"
    ],
    "Debilitate": [
        "To weaken or hinder",
        "To encourage",
        "To decorate",
        "To educate"
    ],
    "Ebullient": [
        "Full of energy and enthusiasm",
        "Calm and reserved",
        "A type of writing style",
        "A musical instrument"
    ],
    "Facilitate": [
        "To make easier",
        "To complicate",
        "To ignore",
        "To destroy"
    ],
    "Garrulous": [
        "Excessively talkative",
        "Brief and to the point",
        "An expert in a field",
        "Shy and reserved"
    ],
    "Hapless": [
        "Unfortunate or unlucky",
        "Incredibly lucky",
        "Rhythmic and smooth",
        "Highly successful"
    ],
    "Impetuous": [
        "Acting quickly without thought",
        "Cautious and deliberate",
        "Calm and relaxed",
        "Thoughtful and considerate"
    ],
    "Juxtaposition": [
        "The act of placing two things side by side for comparison",
        "A type of artistic painting",
        "An emotional outburst",
        "A scientific discovery"
    ],
    "Kinetic": [
        "Related to motion",
        "Static and unchanging",
        "Calm and serene",
        "Confused and chaotic"
    ],
    "Lethargic": [
        "Feeling sluggish or lacking energy",
        "Highly energetic and lively",
        "Eager and motivated",
        "Focused and determined"
    ],
    "Mundane": [
        "Lacking interest or excitement; dull",
        "Extraordinary and exciting",
        "Bright and colorful",
        "Fascinating and captivating"
    ],
    "Nefarious": [
        "Wicked or criminal",
        "Heroic and admirable",
        "Generous and kind",
        "Joyful and happy"
    ],
    "Obfuscate": [
        "To confuse or make unclear",
        "To clarify and explain",
        "To inspire or motivate",
        "To entertain and amuse"
    ],
    "Pervasive": [
        "Spreading widely throughout an area or group",
        "Isolated and confined",
        "Localized and limited",
        "Temporary and fleeting"
    ],
    "Quintessential": [
        "The most perfect or typical example",
        "A rare and unusual occurrence",
        "An outdated concept",
        "A common misconception"
    ],
    "Ravenous": [
        "Extremely hungry",
        "Fully satisfied",
        "Indifferent and apathetic",
        "Calm and peaceful"
    ],
    "Sycophant": [
        "A person who flatters others for personal gain",
        "An independent thinker",
        "A critic of authority",
        "A fearless leader"
    ],
    "Trepidation": [
        "A feeling of fear or anxiety about something that may happen",
        "Confidence and bravery",
        "Indifference to the future",
        "Excitement about new opportunities"
    ],
    "Ubiquitous": [
        "Present everywhere at once",
        "Rare and hard to find",
        "Occasionally seen",
        "Limited to specific places"
    ],
    "Verbose": [
        "Using more words than are needed; wordy",
        "Concise and to the point",
        "Clear and simple",
        "Confusing and unclear"
    ],
    "Zealous": [
        "Having or showing devotion or enthusiasm",
        "Indifferent and apathetic",
        "Fearful and hesitant",
        "Mildly interested"
    ]
}

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
