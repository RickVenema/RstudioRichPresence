from pypresence import Presence
import time
import sys

clientID = '493802983692435457'
RPC = Presence(clientID)

RPC.connect()
print(RPC.update(state="{}".format(sys.argv[1]), details="R Studio"))

