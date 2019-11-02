import pandas as pd

from RFW import RFW
from RFD import RFD

def process_rfw(rfw, rfd):

    df = pd.DataFrame()
    dataset_path = ""

    # Determine which dataset to access
    if rfw.bm_type == "DVD Test":
        dataset_path = "../Datasets/DVD-testing.csv"
    elif rfw.bm_type == "DVD Train":
        dataset_path = "../Datasets/DVD-training.csv"
    elif rfw.bm_type == "NDBench Test":
        dataset_path == "../Datasets/NDBench-testing.csv"
    elif rfw.bm_type == "NDBench Train":
        dataset_path == "../Datasets/NDBench-testing.csv"
    else:
        print("Error: Unrecognized Benchmark Type")

    # Open CSV in a pandas dataframe
    df = pd.read_csv(dataset_path)

    # Obtain requested samples
    samples = {}
    col_values = df[rfw.wl_metric].tolist()
    for i in range(rfw.batch_size):
        batch_name = "Batch " + str(rfw.batch_id + i)
        batch_id = rfw.batch_id + i
        batch_start = rfw.batch_unit * (batch_id - 1)
        batch_end = (rfw.batch_unit * batch_id)
        samples[batch_name] = col_values[batch_start : batch_end]

    # Update RFD
    rfd.rfw_id = rfw.id
    rfd.last_batch_id = rfw.batch_id + rfw.batch_size - 1
    rfd.samples = samples