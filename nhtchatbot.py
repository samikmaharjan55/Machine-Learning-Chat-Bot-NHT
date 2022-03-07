from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def nht():
    return render_template('Home.html')


@app.route('/chat', methods=['POST'])
def chat():
    ch = request.form['messageText']
    print(ch)
    if "hi" in ch:
        return jsonify({"answer": "Hello"})
    elif "who are you" in ch:
        return jsonify({"answer": "I am NHT chatbot."})
    elif "hypertension" in ch:
        return jsonify({"answer": "Hypertension"})
    else:
        return jsonify({"answer": "Sorry I didn't understand u"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
