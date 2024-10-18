from flask import Flask, request, jsonify, render_template
import tensorflow_hub as hub
import joblib

# template_dir = os.path.abspath('./client/templates/')
# static_dir = os.path.abspath('./client/static/')
# app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

# extra_dirs = [static_dir]
# app.config['EXTRA_DIRS'] = extra_dirs

app = Flask(__name__)

embedder = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
tagger = joblib.load("log_reg.joblib")
tags_list = joblib.load("tags_list.pkl")



@app.route('/suggest', methods=['POST'])
def predict():
    # Parsing du JSON
    input_data = request.get_json()
    question = input_data['question']

    # Conversion de la question en embedding
    question_embedding = embedder([question]).numpy()

    # Suggestions des tags
    tag_probabilities = tagger.predict(question_embedding)
    tag_predictions = (tag_probabilities > 0.5).astype(int)
    
    # Récupération des tags prédits
    predicted_tags = [tags_list[i] for i in range(len(tags_list)) if tag_predictions[0][i] == 1]

    # Réponse en JSON
    response = jsonify({"tags": predicted_tags})
    return response

@app.route('/test')
def index():
    return render_template('tagger.html')


if __name__ == "__main__":
    app.run(port=5001, debug=True)