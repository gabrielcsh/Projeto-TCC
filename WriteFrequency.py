import csv

#numpy.savetxt('/tmp/arq_numpy.csv', data, delimiter=',', fmt='%s')
class WriteFrequency():
	def __init__(self, frequencias):
		self.frequencias = frequencias
		with open("frequencias.csv", 'w') as csvfile:
			count = 0
			fieldnames = ['frequencias']
			writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
			writer.writerow(self.frequencias)
