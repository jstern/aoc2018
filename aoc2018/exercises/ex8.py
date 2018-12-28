from ..inputs import read_ints
from ..device import Device


if __name__ == "__main__":
    device = Device(read_ints("day8"))
    print(device.license_number())
    print(device.license_value())
