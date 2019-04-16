from flask import Flask, render_template, render_template_string, jsonify, request
import nltk
import numpy as np

from Sent_funcs import *

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/polarity',methods = ['POST', 'GET'] )


def get_sentiment():
    text = request.args.get('text')
    sent_instance  =  SentimentObject()
    text = sent_instance.clean_one_review(text)
    text = sent_instance.tokenize_text(text)
    global graph
    with graph.as_default():
        pred = np.round(model.predict(text))
    if pred[0][0]==1:
        pred = 'Negative'
    else:
        pred='Positive'

    return render_template("result.html",
                           result = pred)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=80)