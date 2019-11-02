import sys
import RFW_pb2

# Prompts user for RFW info
def prompt_for_RFW(pb_rfw):

    pb_rfw.id = int(input("Enter the RFW ID: "))
    pb_rfw.bm_type = input("Enter Benchmark Type (with quotes \"\"): ")
    pb_rfw.wl_metric = input("Enter Workload Metric (with quotes \"\"): ")
    pb_rfw.batch_unit = int(input("Enter Batch Unit: "))
    pb_rfw.batch_id = int(input("Enter Batch ID: "))
    pb_rfw.batch_size = int(input("Enter Batch Size: "))

if __name__ == '__main__':

    # Makes a binary RFW based on user input
    if len(sys.argv) != 2:
        print ("Usage example:", "python make_binary_protofile.py", "protofile.pb (name of protofile to be created)" )
        sys.exit(-1)

    # Create ProoBuf RFW
    pb_rfw = RFW_pb2.ProtoBufRFW()

    # Read the existing RFW if exists
    try:
        with open(sys.argv[1], "rb") as f:
            pb_rfw.ParseFromString(f.read())
    except IOError:
        print(sys.argv[1] + ": File does not exist or could not open file.  Creating a new one.")

    # Prompt user for RFW info
    prompt_for_RFW(pb_rfw)

    # Write the new binary RFW to disk
    with open(sys.argv[1], "wb") as f:
        f.write(pb_rfw.SerializeToString())
        f.close()

        
