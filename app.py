from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Храним текущее имя врача
current_doctor_data = {
    "name": "Антон Регеда"
}

@app.route("/")
def index():
    return render_template("index.html", doctor_name=current_doctor_data["name"])

@app.route("/get_current_name")
def get_current_name():
    return jsonify({"current_name": current_doctor_data["name"]})

@app.route("/update_name", methods=["POST"])
def update_name():
    new_name = request.json.get("name", "").strip()
    if not new_name:
        return jsonify({"status": "error", "message": "Имя не может быть пустым"})
    current_doctor_data["name"] = new_name
    return jsonify({"status": "success", "new_name": new_name})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
