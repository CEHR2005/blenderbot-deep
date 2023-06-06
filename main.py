from flask import Flask, request, jsonify
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

app = Flask(__name__)

model_name = 'facebook/blenderbot-400M-distill'
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)


@app.route('/ask', methods=['POST'])
def ask():
    question = request.json['question']
    inputs = tokenizer([question], return_tensors='pt')
    reply_ids = model.generate(**inputs)
    reply = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)
    return jsonify(reply)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
