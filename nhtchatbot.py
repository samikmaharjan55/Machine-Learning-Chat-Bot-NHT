from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def nht():
    return render_template('Home.html')


@app.route('/chat', methods=['POST'])
def chat():
    ch = request.get_data('messageText')
    abc = str(ch)
    print(abc)
    if "hi" in abc:
        return jsonify({"answer": "Hello, How can I help you?"})
    elif "who are you" in abc:
        return jsonify({"answer": "I am NHT chatbot."})
    elif "hypertension" in abc:
        return jsonify({"answer": "Also known as high blood pressure, is a long term medical condition in which the blood pressure in the arteries is presistently elevated. How much is your bp?"})
    elif "Hypertension" in abc:
        return jsonify({"answer": "Also known as high blood pressure, is a long term medical condition in which the blood pressure in the arteries is presistently elevated. How much is your bp?"})
    elif "i think i have hypertension" in abc:
        return jsonify({"answer": "How much is your SBP and DBP? Ex: 140/90"})
    elif "140/90" in abc:
        return jsonify({"answer": "If you have SBP: 120-139 mmHg\n120-139"})
    else:
        with open('file.txt', 'a') as f:
            f.write(str(ch))
            f.write('\n')
            return jsonify({"answer": "Sorry, I didn't understand you"})


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
