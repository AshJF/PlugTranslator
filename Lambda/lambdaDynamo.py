import json
import boto3

from flask_lambda import FlaskLambda
from flask import request

app = FlaskLambda(__name__)
ddb = boto3.resource("dynamodb")
table = ddb.Table('students')

@app.route('/students', methods = ['GET', 'POST'])
def put_or_list_students():
    if request.method == 'GET':
        students = table.scan()['Items']
        return (
            json.dumps(students),
            200,
            {'Content-Type': "application/json"}
        )
    else:
        table.put_item(Item = request.form.to_dict())
        return{
            json.dumps({"message": "student entry created"}),
            200,
            {'Content-Type': "application/json"}
        }