from flask_api import status
from flask_restful import Resource, Api
from flask import Flask, make_response, request

from json import dumps, loads

import processing
from RFW import RFW
from RFD import RFD
from RFW_pb2 import ProtoBufRFW
from RFD_pb2 import ProtoBufRFD

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

        # Serialize RFD to JSON RFD
        json_rfd = dumps(rfd.json_serialize())

        # Send response
        response = make_response(json_rfd)
        response.headers['Content-type'] = 'application/json'
        return response

class ProtoBufResponseForData(Resource):
    def post(self):

        # Create ProtoBuf RFW & RFD
        pb_rfw = ProtoBufRFW()
        pb_rfd = ProtoBufRFD()

        # Create Object RFW & RFD
        rfw = RFW(0, 0, 0, 0, 0, 0)
        rfd = RFD(0, 0, 0)

        # Deserialize the ProtoBuf RFW
        pb_rfw.ParseFromString(request.data)
        rfw.protobuf_deserialize(pb_rfw)

        # Acces CSVs and fill RFD
        processing.process_rfw(rfw, rfd)

        # Serialize RFD to ProtoBuf RFD
        rfd.protobuf_serialize(pb_rfd)
        
        # Print Serialized ProtoBuf RFD before sending (for proof)
        print("RFW ID: ", pb_rfd.rfw_id)
        print("Last Batch ID: ", pb_rfd.last_batch_id)
        for k, v in pb_rfd.samples.items():
            print(k, v.batchSamples)

        # Send response
        response = make_response(pb_rfd.SerializeToString())
        response.headers['Content-type'] = 'application/x-protobuf'
        return response

# URL endpoints for JSON & ProtoBuf
api.add_resource(JSONResponseForData, '/json_rfd')
api.add_resource(ProtoBufResponseForData, '/protobuf_rfd')

if __name__ == '__main__':
    server.run(debug=True)
