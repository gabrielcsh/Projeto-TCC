import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import numpy as np
from matplotlib import pyplot as plt

class Audio():
	def __init__(self, filename):
		self.filename = filename
		self.n_samplings = None # número total de amostras
		self.secs = None # duração do áudio
		self.F_sampling = None # frequência de amostragem
		self.T_sampling = None # período de amostragem
		self.signal = None # sinal amostrado
		self.time_vector = None # array com os instantes de tempo (eixo x)

	def mp3_to_wav(self):
		# TO DO

		# seria bom ver se dá pra convertar mp3 em wav, tem muitos áudios mp3 bons e uns wav bem bosta
		pass


	def load_wav(self):
		self.F_sampling, signal = wavfile.read(self.filename)

		self.signal = np.mean(signal, axis=1) # faz a média dos canais se o áudio for estéreo

		self.n_samplings = self.signal.shape[0] 

		self.secs = self.n_samplings/float(self.F_sampling)

		self.T_sampling = 1.0/self.F_sampling

		self.time_vector = scipy.arange(0, self.secs, self.T_sampling)

	def plot_time_domain(self):
		plt.xlabel('Time')
		plt.ylabel('Amplitude')
		plt.plot(self.time_vector, self.signal, "g")
		plt.show()
