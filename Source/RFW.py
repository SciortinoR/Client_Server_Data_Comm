class RFW:
    def __init__(self, id, bm_type, wl_metric, batch_unit, batch_id, batch_size):
        self.id = id
        self.bm_type = bm_type
        self.wl_metric = wl_metric
        self.batch_unit = batch_unit
        self.batch_id = batch_id
        self.batch_size = batch_size

    def json_serialize(self):
        return {
            'ID' : self.id,
            'Benchmark_Type' : self.bm_type,
            'Workload_Metric' : self.wl_metric,
            'Batch_Unit' : self.batch_unit,
            'Batch_ID' : self.batch_id,
            'Batch_Size' : self.batch_size
        }

    def json_deserialize(self, obj):
        self.id = obj['ID']
        self.bm_type = obj['Benchmark_Type']
        self.wl_metric = obj['Workload_Metric']
        self.batch_unit = obj['Batch_Unit']
        self.batch_id = obj['Batch_ID']
        self.batch_size = obj['Batch_Size']

    def protobuf_serialize(self, obj):
        obj.id = self.id
        obj.bm_type = self.bm_type
        obj.wl_metric = self.wl_metric
        obj.batch_unit = self.batch_unit
        obj.batch_id = self.batch_id
        obj.batch_size = self.batch_size

    def protobuf_deserialize(self, obj):
        self.id = obj.id           
        self.bm_type = obj.bm_type
        self.wl_metric = obj.wl_metric
        self.batch_unit = obj.batch_unit
        self.batch_id = obj.batch_id
        self.batch_size = obj.batch_size