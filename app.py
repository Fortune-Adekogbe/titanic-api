import traceback
import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)
lr = joblib.load("xgbrf_model.pkl")  # Load "model.pkl"
model_columns = joblib.load("model_columns.pkl")  # Load "model_columns.pkl"

@app.route('/predict', methods=['POST'])  # Your API endpoint URL would consist /predict
def predict():
    if lr:
        try:
            json_ = request.get_json(force=True)
            json_.update((x, [y] if type(y) != list else y) for x, y in json_.items())
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=['Age', 'Embarked_C', 'Embarked_Q', 'Embarked_S',
                                           'Embarked_nan', 'Sex_female', 'Sex_male', 'Sex_nan'], fill_value=0)
            status = {1: 'Alive', 0: "Dead"}
            prediction = [status[i] for i in list(lr.predict(query))]

            return jsonify(predictions=prediction)

        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        return ('No model here to use')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
