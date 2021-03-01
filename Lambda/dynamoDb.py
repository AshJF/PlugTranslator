
import boto3

ddb = boto3.resource('dynamodb')

table = ddb.Table('students')

table.get_item(
    Key = {'id': '1'}
)

table.put_item(Item = {
    'id': '2',
    'name': 'Lee',
    'branch': 'DnA'
})

table.delete_item(
    Key = {'id': '2'}
)