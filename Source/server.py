from flask_api import status
from flask_restful import Resource, Api
from flask import Flask, make_response, request

from json import dumps, loads

from RFW import RFW
from RFD import RFD

# Setup Flask server
server = Flask(__name__)
api = Api(server)

class JSONResponseForData(Resource):
    def post(self):
        return 

class ProtoBufResponseForData(Resource):
    def post(self):
        return

# URL endpoints for JSON & ProtoBuf
api.add_resource(JSONResponseForData, '/json_rfd')
api.add_resource(ProtoBufResponseForData, '/protobuf_rfd')

if __name__ == '__main__':
    server.run()
