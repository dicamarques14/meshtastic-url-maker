import base64
from meshtastic.mesh_pb2 import NodeInfo
from meshtastic.mesh_pb2 import User
from meshtastic.mesh_pb2 import HardwareModel
from meshtastic.config_pb2 import Config

node = NodeInfo()
node_id = "!deadcafe"
long_name = "LongName"
short_name = "STNM"
hex_mac = "000000000001"
model: HardwareModel = HardwareModel.UNSET
role: Config.DeviceConfig.Role = Config.DeviceConfig.Role.CLIENT
base64_p_key = "AQ=="
is_unmessagable=False


# REQUIRED
node.num = 967487634
node.user.CopyFrom(User(
    id=node_id,
    long_name=long_name,
    short_name=short_name,
    macaddr=bytes.fromhex(hex_mac),
    hw_model=model,
    role=role,
    public_key=base64.decodebytes(base64_p_key.encode("ascii")),
    is_unmessagable=is_unmessagable)
)

# Serialize protobuf
raw = node.SerializeToString()

# Base64 URL-safe encode (NO padding)
encoded = base64.urlsafe_b64encode(raw).decode().rstrip("=")


url = f"https://meshtastic.org/v/#{encoded}"
print(url)
