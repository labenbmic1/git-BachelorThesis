import numpy
import numpy.linalg
import scipy.sparse

class TImodel():# (long range) transversal Ising model
	__counter = 0

	def __init__(self, L=2, coeff=[1, 1, 0], signs=[-1, -1, -1], alpha=1.5, s=[1, 3, 1], basis=3, PBC=False):
		TImodel.__counter += 1
		self._L = L
		self._parameters = 3 # fix (ordered (J, g, h))
		
		while len(self._s) < self._parameters:
			self._s.append(3)
		while len(self._s) > self._parameters:
			del self._s[-1]
			print(" deleted one s", self._s)