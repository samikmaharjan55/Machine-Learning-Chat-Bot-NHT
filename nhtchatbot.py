from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def nht():
    return render_template('Home.html')


@app.route('/chat', methods=['POST'])
def chat():
    ch = request.get_data('messageText')
    abc = ch.decode('UTF-8')
    ab = abc.replace('messageText=', '')
    a = ab.replace('+', ' ')
    print(a)
    if "hi" in a:
        return jsonify({"answer": "Hello, this is NHT chatbot. Are you feeling good?"})
    elif "Hi" in a:
        return jsonify({"answer": "Hello, this is NHT chatbot. Are you feeling good?"})
    elif "hello" in a:
        return jsonify({"answer": "Hello, this is NHT chatbot. Are you feeling good?"})
    elif "Hello" in a:
        return jsonify({"answer": "Hello, this is NHT chatbot. Are you feeling good?"})
    elif "yes" in a:
        return jsonify({"answer": "Good to know! Always remember me if you need assistance."})
    elif "no" in a:
        return jsonify({"answer": "Do you have any symptoms?"})
    elif "No" in a:
        return jsonify({"answer": "How much is your SBP and DBP? Ex: 120/80 mmHg"})
    elif "headache" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "chest pain" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "shortness of breath" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "diziness" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "vision problem" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "confusion and fatigue" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "irregular heartbeat" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "sweating" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "blood spot in eyes" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "blood in urine" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "pounding in chest neck and ears" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "chest pain" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "severe" in a:
        return jsonify({"answer": "How much is your SBP and DBP? Ex: 120/80 mmHg"})
    elif "normal" in a:
        return jsonify({"answer": "How much is your SBP and DBP? Ex: 120/80 mmHg"})
    elif "120 80" in a:
        return jsonify({"answer": "You have a normal bp."})
    elif "140 90" in a:
        return jsonify({"answer": "You have Hypertension Stage I."})
    elif "160 100" in a:
        return jsonify({"answer": "You have Hypertension Stage II."})
    else:
        with open('file.txt', 'a') as f:
            f.write(a)
            f.write('\n')
            return jsonify({"answer": "Sorry, I didn't understand you"})


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
