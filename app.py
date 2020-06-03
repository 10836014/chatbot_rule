from flask import Flask, request
import Chatbot.chatbot as Chatbot
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':
        data = json.loads(request.get_data().decode('utf-8'))
        print("get POST request data: ", data)

        question = data["question"]

        chatter = Chatbot.Chatbot(w2v_model_path='model/word2vec.model')

        ans = {
            'answer': chatter.waiting_loop(question)
        }

        return ans

    elif request.method == 'GET':
        return 'GET OK!'

if __name__ == '__main__':
    app.run()