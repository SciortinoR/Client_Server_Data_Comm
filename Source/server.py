from flask_api import status
from flask_restful import Resource, Api
from flask import Flask, make_response, request

from json import dumps, loads

import processing
from RFW import RFW
from RFD import RFD

# Setup Flask server
server = Flask(__name__)
api = Api(server)

class JSONResponseForData(Resource):
    def post(self):
        
        # Create RFW & RFD
        rfw = RFW(0, 0, 0, 0, 0, 0)
        rfd = RFD(0, 0, 0)

        # Deserialize the RFW
        rfw.json_deserialize(loads(request.data))

        # Access CSVs and fill RFD
        processing.process_rfw(rfw, rfd)

        # Serialize RFD
        json_rfd = dumps(rfd.json_serialize())

        # Send response
        response = make_response(json_rfd)
        response.headers['Content-type'] = 'application/json'

        return response

class ProtoBufResponseForData(Resource):
    def post(self):
        return

# URL endpoints for JSON & ProtoBuf
api.add_resource(JSONResponseForData, '/json_rfd')
api.add_resource(ProtoBufResponseForData, '/protobuf_rfd')

if __name__ == '__main__':
    server.run(debug=True)
