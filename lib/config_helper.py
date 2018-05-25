import argparse
import os
import yaml
import datetime
from collections import OrderedDict


class ConfigHelper(object):
    def __init__(self):
        config = self.read_yml('configs')
        self.halo_key = config["halo"]["api_key"]
        self.halo_secret = config["halo"]["api_secret_key"]
        self.filename = self.report_name(config)
        self.csv_columns = self.construct_dict(config, 'csv_columns')

    def report_name(self, config):
        now = datetime.datetime.now()
        return "%s-%s" % (str(now), config["filename"])

    def construct_dict(self, config, key):
        d = OrderedDict()
        for col in config[key]:
            for k, v in col.items():
                d[k] = v
        return d

    def argparse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--group_id",
                            required=True,
                            help="server group id")
        parser.add_argument("--descendants",
                            required=False,
                            default=True,
                            help="including servers from children server groups or not ")
        return parser.parse_args()

    @classmethod
    def read_yml(self, f):
        yml_path = os.path.join(os.path.dirname(__file__), "../configs/%s.yml" % f)
        return yaml.load(file(yml_path, 'r'))
