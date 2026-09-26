

class NetworkNode:
    def __init__(self, ip: str, mac: str):
        self.ip = ip
        self.mac = mac
        self.lable = ip
        # self.vendor = self

    def _detect_vendor(self):
        if self.mac.startswith("00:1A:2B"):
            return "Cisco"
        return "Generic ICS"

    def set_label(self, new_label: str):
        self.lable = new_label

