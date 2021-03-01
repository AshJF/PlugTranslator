import json
import boto3

from flask_lambda import FlaskLambda
from flask import request

app = FlaskLambda(__name__)

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("customer")

@app.route('/hello')
def index():
    data = {
        "message": "Hello, world!"
    }
    return (
        json.dumps(data),
        200,
        {"Content-Type": "application/json"}
    )

@app.route('/customers', methods = ['GET', 'POST'])
def put_or_list_customers():
    if request.method == 'GET':
        customers = table.scan()['Items'] 
        return (
            json.dumps(customers),
            200,
            {"Content-Type": "application/json"}
        )
    else:
        table.put_item(
            Item = request.form.to_dict()
        )
        return (
            json.dumps({"message": "Customer entry created"}),
            200,
            {"Content-Type": "application/json"}
        )

@app.route('/customers/<id>', methods = ['GET', 'PATCH', 'DELETE'])
def get_patch_delete_student(id):
    if request.method == 'GET':
        customer = table.get_item(Key = {'id': id})['Item']
        return (
            json.dumps(customer),
            200,
            {"Content-Type": "application/json"}
        )
    elif request.method == 'PATCH':
        attribute_updates = {
                key: {'Value': value, 'Action': 'PUT'} 
                for key, value in request.form.items()
            }
        table.update_item(Key = {'id': id}, AttributeUpdates = attribute_updates)
        return (
            json.dumps({"message": "Customer entry updated"}),
            200,
            {"Content-Type": "application/json"}
        )
    elif request.method == 'DELETE':
        table.delete_item(Key = {'id': id})
        return (
            json.dumps({"message": "Customer entry deleted"}),
            200,
            {"Content-Type": "application/json"}
        )