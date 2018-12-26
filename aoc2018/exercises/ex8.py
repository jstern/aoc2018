import os
from ..inputs import read_ints
from ..device import Device


if __name__ == "__main__":
    device = Device(read_ints("day8"))
    if os.environ.get("RECURSIVE") == "1":
        print(device.license_number_r())
    else:
        print(device.license_number())
