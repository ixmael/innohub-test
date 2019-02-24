from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import datetime
from flask_httpauth import HTTPBasicAuth

db_connect = create_engine('sqlite:///restapy.sqlite')
app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "SuperSecretPwd"
}
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class Messages(Resource):
    #@auth.login_required
    def get(self):
        if request.args.get('last_item') == 'true':
            query_text = "select * from messages order by id desc limit 1"
        else:
            query_text = "select * from messages"

        conn = db_connect.connect() # connect to database
        query = conn.execute(query_text) # This line performs query and returns json result
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
    
    #@auth.login_required
    def post(self):
        message = request.json['content']
        today = datetime.date.today().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        conn = db_connect.connect() # connect to database
        query = conn.execute("insert into messages values(null,'{0}','{1}','{2}')".format(message, today, today))
        return {'status':'success'}


api.add_resource(Messages, '/mensajes') # Route_1

if __name__ == '__main__':
     app.run(port='5002')
