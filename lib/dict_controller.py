

class DictController(object):
	def __init__(self, config):
		self.col = config.csv_columns

	def build_dict(self, acct_data,server_id ):
		data = {
			self.col["server_id"] : server_id,
			self.col["username"]  : acct_data["username"],
			self.col["uid"]       : acct_data["uid"],
			self.col["gid"]: acct_data["gid"],
			self.col["admin"]: acct_data["admin"],
			self.col["comment"]: acct_data["comment"],
			self.col["home"]: acct_data["home"],
			self.col["shell"]: acct_data["shell"],
			self.col["last_login_at"]: acct_data["last_login_at"],
			self.col["active"]: acct_data["active"],
			self.col["last_login_from"]: acct_data["last_login_from"],
			self.col["expires"]: acct_data["expires"],
			self.col["password_locked"]: acct_data["password_locked"],
			self.col["password_locked_with"]: acct_data["password_locked_with"],
			self.col["password_expires"]: acct_data["password_expires"],
			self.col["password_expired"]: acct_data["password_expired"]
		}
		return data
