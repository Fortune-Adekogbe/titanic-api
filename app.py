import sys
import traceback
import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/predict', methods=['GET', 'POST'])  # Your API endpoint URL would consist /predict
def predict():
    if lr:
        try:
            json_ = request.get_json(force=True)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=['Age', 'Embarked_C', 'Embarked_Q', 'Embarked_S',
                                           'Embarked_nan', 'Sex_female', 'Sex_male', 'Sex_nan'], fill_value=0)
            status = {1: 'Alive', 0: "Dead"}
            prediction = [status[i] for i in list(lr.predict(query))]

            return jsonify(predictions=prediction)

        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return ('No model here to use')


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])  # This is for a command-line input
    except:
        port = 12345  # If you don't provide any port the port will be set to 12345

    lr = joblib.load("xgbrf_model.pkl")  # Load "model.pkl"
    print('Model loaded')
    model_columns = joblib.load("model_columns.pkl")  # Load "model_columns.pkl"
    print('Model columns loaded')

    app.run(port=port, debug=True)
