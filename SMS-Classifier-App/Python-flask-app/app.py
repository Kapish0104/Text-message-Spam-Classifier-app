from flask import Flask, request, render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

def classifyMessage(message_text):
    nb_model = pickle.load(open('naive_bayes_model', 'rb'))
    vectorizer = pickle.load(open('vectorizer', 'rb'))
    message_list =[]
    message_list.append(message_text)
    message_vector = vectorizer.transform(message_list)
    prediction = nb_model.predict(message_vector)[0]
    print(prediction)
    if prediction == 0:
        return 'THE MESSAGE IS NOT A SPAM'
    else:
        return 'THE MESSAGE IS A SPAM'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        message = " "
        return render_template('index.html')
    if request.method == 'POST':
        message = request.form.get('msg')
        if message == None or message == "":
            prediction = "Message Field Blank"
        else:
            prediction = classifyMessage(message)
        return render_template('index.html', message= prediction)

if __name__ == '__main__':
    print("Welcome to my app")
    app.run(host='0.0.0.0', port=81)


