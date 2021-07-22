class Job:
	def __init__(self, job_requester):
		self.job_name = ""
		self.batch_id = ""
		self.requester = job_requester
	def request(self, job_name, batch_id):
		self.job_name = job_name
		self.batch_id = batch_id
		return self.job_name, self.batch_id
