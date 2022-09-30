import os
import glob
import random
from flask import Flask, request, jsonify, send_file
from scripts.txt2img import Input, main

app = Flask(__name__)


@app.route("/text-to-image", methods=['POST'])
def make_predict():
    json = request.get_json()
    prompt = json['Prompt']
    seed = random.randint(100000000, 999999999)
    params = Input(prompt, 12, "outputs/txt2img-samples", 25, 1, seed)
    main(params)
    list_of_files = glob.glob('outputs/txt2img-samples/samples/*.png')
    latest_file = max(list_of_files, key=os.path.getctime)
    return send_file(path_or_file=latest_file,
                     download_name=f"{prompt}.png",
                     mimetype="image/png")


app.run(host='localhost', port=14100, debug=True)