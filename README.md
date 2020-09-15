# Titanic survivors prediction API

To use, run the following:

```bash
curl -s -XPOST 'https://life-boat.herokuapp.com/predict' -d '{"Age":3,"Sex":"male","Embarked":"S"}' -H 'accept-content: application/json'
```

Alternatively a simple python script:

```python
import requests
import json
url = 'https://life-boat.herokuapp.com/predict'
data = {"Age":3,"Sex":"male","Embarked":"S"}
response = requests.post(url, json.dumps(data))
print(response.json())
```

# Acknowlegements
 - **Article**: [Towards Data Science: Create an API to Deploy Machine Learning Models using Flask](https://towardsdatascience.com/create-an-api-to-deploy-machine-learning-models-using-flask-and-heroku-67a011800c50)
 - **Author**: [Elizabeth Ter Sahakyan](https://towardsdatascience.com/@liztersahakyan)
