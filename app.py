from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

doctors = [
    {"id": 1, "name": "Антон Регеда", "position": "Невролог", "rating": 4.8, "experience": 5, "clinic": "Клиника доктора Пирогова"},
    {"id": 2, "name": "Ирина Смирнова", "position": "Терапевт", "rating": 4.9, "experience": 8, "clinic": "Городская клиника №5"},
    {"id": 3, "name": "Павел Козлов", "position": "Хирург", "rating": 4.7, "experience": 10, "clinic": "Медцентр «Альфа»"},
    {"id": 4, "name": "Мария Иванова", "position": "Педиатр", "rating": 4.6, "experience": 6, "clinic": "Детская больница №3"},
]

current_index = 0


@app.route("/")
def index():
    return render_template("index.html", doctor=doctors[current_index])


@app.route("/get_current_doctor")
def get_current_doctor():
    return jsonify(doctors[current_index])


@app.route("/action", methods=["POST"])
def handle_action():
    global current_index
    data = request.json
    action = data.get("action")

    if action in ["accept", "reject"]:
        current_index = (current_index + 1) % len(doctors)

    return jsonify({"status": "success", "new_doctor": doctors[current_index]})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

