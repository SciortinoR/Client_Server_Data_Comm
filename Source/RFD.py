class RFD:
    def __init__(self, rfw_id, last_batch_id, samples):
        self.rfw_id = rfw_id
        self.last_batch_id = last_batch_id
        self.samples = samples

    def json_serialize(self):
        return {
            'RFW_ID' : self.rfw_id,
            'Last_Batch_ID' : self.last_batch_id,
            'Samples_Requested' : self.samples
        }

    def json_deserialize(self, obj):
        self.rfw_id = obj['RFW_ID']
        self.last_batch_id = obj['Last_Batch_ID']
        self.samples = obj['Samples_Requested']

    def protobuf_serialize(self, obj):
        obj.rfw_id = self.rfw_id
        obj.last_batch_id = self.last_batch_id
        for k, v in self.samples.items():
            obj.samples[k].batchSamples.extend(v)

    def protobuf_deserialize(self, obj):
        self.rfw_id = obj.rfw_id
        self.last_batch_id = obj.last_batch_id
        self.samples = obj.samples