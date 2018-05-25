import lib
import logging
import sys

class LocalAccountReport(object):
    def __init__(self):
        self.config = lib.ConfigHelper()
        self.server = lib.ServerController()
        self.dict = lib.DictController(self.config)
        self.csv_writer = lib.CsvWriter(self.config)
        self.csv_columns = self.config.csv_columns

    def get_servers(self, args):
        return self.server.list_servers_under_group(args)

    def run(self, servers):
        for server in servers:
            accounts = self.server.list_local_accounts(server["id"])
            for account in accounts:
                data = self.dict.build_dict(account, server["id"])
                self.csv_writer.write(self.csv_columns.values(), data)
def main():
    sys.stdout.write("start retreiving server information")
    report = LocalAccountReport()

    args = report.config.argparse()

    servers = report.get_servers(args)

    report.run(servers)
    sys.stdout.write("finish writing out report")

if __name__ == "__main__":
    sys.stdout = lib.Logger(logging.info)
    sys.stderr = lib.Logger(logging.warning)
    main()
