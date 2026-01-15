from meshtastic.mesh_pb2 import NodeInfo


import base64

encoded = (
    "CJLhqs0DEiUKCSEzOWFhYjA5MhIFVU5LXzEaBFVOSzEiBgAAAAAAAUIBAUgA"
)

# Base64 URL-safe decode (handle missing padding)
padding = "=" * (-len(encoded) % 4)
raw = base64.urlsafe_b64decode(encoded + padding)

node = NodeInfo()
node.ParseFromString(raw)

print(node)

'''
num: 2997301856
user {
  id: "!b2a73260"
  long_name: "DG-Qlass-CL-8"
  short_name: "DG18"
  macaddr: "\234\023\236\240\247P"
  hw_model: HELTEC_V4
  role: CLIENT_MUTE
  public_key: "\301\2031\"\001\235\307\333W\276\374\233\231\373\345\217_7\260\217R\357\306i\200\260m\005\303\310\274\006"
  is_unmessagable: false
}

num: 2997301856
user {
  id: "!b2a73260"
  long_name: "DG-Qlass-CL-8"
  short_name: "DG18"
  macaddr: "\200\361\262\2472`"
  hw_model: HELTEC_V4
  role: CLIENT_MUTE
  public_key: "\254\250i\010\315\217;\332.\273\327Fynp\372xm\270s1\265\275\214\346\245\330t\326e\260x"
  is_unmessagable: false
}
'''