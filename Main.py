import sys
from audio import Audio
from FrequencyAnalysis import FrequencyAnalysis
from WriteFrequency import WriteFrequency

import scipy
import scipy.fftpack
import numpy as np

import matplotlib.pyplot as plt

class Main():
	def __init__(self):
		# carrega áudio
		audio = Audio(sys.argv[1])
		audio.load_wav()

		# inicializa variáveis
		y = audio.signal
		T = audio.T_sampling
		x = audio.time_vector

		 # tamanho da janela de corte em ms
		t = float(sys.argv[2])

		time = 0.
		n_samplings = int(t / T)

		left = 0
		right = n_samplings
		frequencys = []
		while time <= audio.secs:
			# o número de amostras por janela é o tempo em segundos da janela dividido pelo período de amostragem

			try:
				FA = FrequencyAnalysis(signal=y[left:right], time_vector=x[left:right], period=T)
			except:
				FA = FrequencyAnalysis(signal=y[left:], time_vector=x[left:], period=T)

			# faz a transformada de fourier do sinal y
			FA.fft()

			# plota domínio da frequência
			#FA.plot()

			max_freq = FA.max_frequency()
			frequencys.append(max_freq)

			print("Frequency: {} Hz".format(max_freq))

			time += t
			left = right
			right += n_samplings

		WriteFrequency(frequencys)

		


if __name__ == '__main__':
	main = Main()
