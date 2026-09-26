from Device import Device

plc = Device(ip="1", mac="00:00:00:00:00:01", name="plc_Siemens")

plc.receive_packet()
plc.receive_packet()

print(plc.get_info())
