from netconf import nsmap_update, server, util
from users_cred import username, password
from netconf.client import NetconfSSHSession, connect_ssh
import time


MODEL_NS = "urn:my-urn:my-model"
nsmap_update({'pfx': MODEL_NS})
rpc_my_cool_rpc = "<my-cool-rpc>"


class MyServer (object):
    def __init__(self, user, pw):
        controller = server.SSHUserPassController(username=user, password=pw)
        self.server = server.NetconfSSHServer(server_ctl=controller, server_methods=self)

    def nc_append_capabilities(self, caps):
        util.subelm(caps, "capability").text = MODEL_NS

    def rpc_my_cool_rpc(self, session, rpc, *params):
        data = util.elm("data")
        data.append(util.leaf_elm("pfx:result", "RPC result string"))
        return data

server = MyServer(username, password)
print("Server is running")
time.sleep(100)

host = "127.0.0.1"
port = 830

session_ssh = connect_ssh(host, port, username, password)
session = NetconfSSHSession(host, port, username, password)
session.get()
session.close()
print("Servir was stopped")
