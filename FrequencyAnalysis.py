import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt

class FrequencyAnalysis():
	import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt

class FrequencyAnalysis():
	def __init__(self, signal, time_vector, period):
		self.signal = signal
		self.time_vector = time_vector
		self.period = period
		self.N = len(time_vector)

		self.yf = None
		self.xf = None

	def fft(self):
		"""
		Faz  a transformada de fourier e retorna o eixo x (frequência) pelo y (amplitude)
		"""
		Y = scipy.fftpack.fft(self.signal)
		X = np.linspace(0.0, 1.0/(2.0*self.period), self.N/2)

		self.yf = 2.0/self.N * np.abs(Y[:self.N//2])

		self.xf = X

	def plot(self):
		"""
		plota o sinal no domínio da frequência
		"""
		fig, ax = plt.subplots()
		ax.plot(self.xf, self.yf)
		plt.show()

	def max_frequency(self):
		"""
		retorna a frequência máxima do sinal
		"""

		return self.xf[np.argmax(self.yf)]

