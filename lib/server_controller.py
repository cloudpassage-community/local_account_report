import cloudpassage
from lib.api_session import ApiSession


class ServerController(ApiSession):
    def __init__(self):
        super(ServerController, self).__init__()
        self.api = cloudpassage.HttpHelper(self.session)
        self.srv_obj = cloudpassage.Server(self.session)

    def list_servers_under_group(self, args):
        url = '/v2/servers?group_id=%s&descendants=%s' % (args.group_id,
                                                          args.descendants)
        servers = self.api.get(url)
        return servers["servers"]

    def list_local_accounts(self, srv_id):
        return self.srv_obj.list_local_accounts(srv_id)