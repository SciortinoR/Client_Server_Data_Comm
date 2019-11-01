class RFW:
    def __init__(self, id, bm_type, wl_metric, batch_unit, bacth_id, bacth_size):
        self.id = id
        self.bm_type = bm_type
        self.wl_metric = wl_metric
        self.batch_unit = batch_unit
        self.batch_id = bacth_id
        self.batch_size = bacth_size

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
