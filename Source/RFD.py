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