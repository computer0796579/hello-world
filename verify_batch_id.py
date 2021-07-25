class Job:
	""" Verify batch id for a job."""
	def __init__(self, job_name, job_batch_id):
		self._job_name = job_name
		self._job_batch_id = job_batch_id

	def verify(self):
		"""Veryfy the batch id."""
		s = input("Batch ID: ")
		if self._job_batch_id == eval(s):
			print("GTG, thank you")
		else:
			print("Invalid batch id.")
