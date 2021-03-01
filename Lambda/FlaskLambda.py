import json

from flask_lambda import FlaskLambda



app = FlaskLambda(__name__)

@app.route('/hello')
def index():
    data = {

    }
    return (
        json.dumps(data),
        200,
        {'Content-Type': "application/json"}
    )