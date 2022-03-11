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
        return jsonify({"answer": "Hello, this is NHT chatbot. How can I help you?"})
    elif "I have a headache" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "i have a headache" in a:
        return jsonify({"answer": "Severe or normal"})
    elif "Severe" in a:
        return jsonify({"answer": "What are the other symptoms that you have"})
    elif "severe" in a:
        return jsonify({"answer": "What are the other symptoms that you have"})
    elif "chest pain" in a:
        return jsonify({"answer": "For how long have you been suffering from it"})
    elif "one day ago" in a:
        return jsonify({"answer": "Have you been diagnosed with Hypertension before? Yes or No?"})
    elif "no" in a:
        return jsonify({"answer": "How much is your SBP and DBP? A.120/80mmHg \n B.120-129/<80 mmHg \n C.130-139/80-89mmHg \n D.>140/>80mmHg \n Choose A or B or C or D"})
    elif "yes" in a:
        return jsonify({"answer": "How much is your SBP and DBP? A.120/80mmHg \n B.120-129/<80 mmHg \n C.130-139/80-89mmHg \n D.>140/>80mmHg \n Choose A or B or C or D"})
    elif "140" in a:
        return jsonify({"answer": "If you have SBP: 120-139 mmHg\n120-139"})
    else:
        with open('file.txt', 'a') as f:
            f.write(a)
            f.write('\n')
            return jsonify({"answer": "Sorry, I didn't understand you"})


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
