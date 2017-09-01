import numpy as np
import random
from math import sqrt, pi, exp

def gaussian_prob(obs, mu, sig):
    num = (obs - mu)**2
    denum = 2*sig**2
    norm = 1 / sqrt(2*pi*sig**2)
    return norm * exp(-num/denum)

class GNB(object):

	def __init__(self):
		self.possible_labels = ['left', 'keep', 'right']

	def train(self, data, labels):
		"""
		Trains the classifier with N data points and labels.

		INPUTS
		data - array of N observations
		  - Each observation is a tuple with 4 values: s, d,
		    s_dot and d_dot.
		  - Example : [
			  	[3.5, 0.1, 5.9, -0.02],
			  	[8.0, -0.3, 3.0, 2.2],
			  	...
		  	]

		labels - array of N labels
		  - Each label is one of "left", "keep", or "right".
		"""
		X = data
		Y = labels
		num_vars = 4

		totals_by_label = {
		    "left" : [],
		    "keep" : [],
		    "right": [],
		}

		for label in self.possible_labels:
			for i in range(num_vars):
			    totals_by_label[label].append([])

		for x, label in zip(X,Y):

			# process the raw s,d,s_dot,d_dot snapshot if desired.
			# x = self.process_vars(x)
			# print len(x)
			# add this data into the appropriate place in the
			# totals_by_label data structure.
			for i,val in enumerate(x):
				totals_by_label[label][i].append(val)

	    # Get the mean and standard deviation for each of the arrays
        # we've built up. These will be used as our priors in GNB
        means = []
        stds = []
        for i in self.possible_labels:
            means.append([])
            stds.append([])
            for arr in totals_by_label[i]:
                mean = np.mean(arr)
                std = np.std(arr)
                means[-1].append(mean)
                stds[-1].append(std)

		print means
        self._means = means
        self._stds = stds

	def predict(self, observation):
		"""
		Once trained, this method is called and expected to return
		a predicted behavior for the given observation.

		INPUTS

		observation - a 4 tuple with s, d, s_dot, d_dot.
		  - Example: [3.5, 0.1, 8.5, -0.2]

		OUTPUT

		A label representing the best guess of the classifier. Can
		be one of "left", "keep" or "right".
		"""
		# TODO - complete this
		return self.possible_labels[2]
