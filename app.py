from flask import Flask, render_template, request, redirect, url_for
import json
import random

app = Flask(__name__)

# Load participants and drawn data
with open("data.json", "r") as file:
    data = json.load(file)

participants = data["participants"]
drawn = data["drawn"]

@app.route("/")
def index():
    # Ensure the main menu loads participants and their drawn status
    return render_template(
        "index.html",
        participants=[
            {"name": name, "drawn": name in drawn} for name in participants
        ],
    )

@app.route("/draw", methods=["POST"])
def draw():
    current_user = request.form.get("name")

    if not current_user or current_user in drawn:
        # Redirect to the main menu if no user is selected or already drawn
        return redirect(url_for("index"))

    # Find participants who are eligible to be drawn
    available_participants = [
        name for name in participants if name != current_user and name not in drawn.values()
    ]

    if not available_participants:
        # Redirect if no participants are available
        return redirect(url_for("index"))

    # Randomly select an available participant
    selected = random.choice(available_participants)

    # Record the draw
    drawn[current_user] = selected
    with open("data.json", "w") as file:
        json.dump({"participants": participants, "drawn": drawn}, file)

    # Show the draw result page
    return render_template("draw.html", current_user=current_user, selected=selected)

@app.route("/reset", methods=["POST"])
def reset():
    global drawn
    # Reset the drawn data
    drawn = {}
    with open("data.json", "w") as file:
        json.dump({"participants": participants, "drawn": drawn}, file)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
