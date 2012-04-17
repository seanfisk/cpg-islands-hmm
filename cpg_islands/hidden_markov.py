""":mod:`cpg_islands.hidden_markov` --- The actual model

For now, this is just a sample from a `ghmm tutorial`_.

.. _ghmm tutorial: http://codecereal.blogspot.com/2011/05/hidden-markov-models.html

"""

from __future__ import print_function
import ghmm
from header import header

# setting 0 for Heads and 1 for Tails as our Alphabet 
sigma = ghmm.IntegerRange(0, 2)

# transition matrix: rows and columns means origin and destiny states
transitions_probabilities = [
    [0.9, 0.1], # 0: fair state
    [0.1, 0.9], # 1: biased state
]

# emission matrix: rows and columns means states and symbols respectively
emissions_probabilities = [
    [0.5, 0.5], # 0: fair state emissions probabilities
    [0.75, 0.25], # 1: biased state emissions probabilities
]

# probability of initial states
pi = [0.5, 0.5] # equal probabilities for 0 and 1

hmm = ghmm.HMMFromMatrices(
    sigma,
    # you can model HMMs with others emission probability distributions
    ghmm.DiscreteDistribution(sigma),    
    transitions_probabilities,
    emissions_probabilities,
    pi
)

print(header('Hidden Markov Model'))
print(hmm)
print()

tosses = [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0,
          1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1]

# not as pythonic is could be :-/
sequence = ghmm.EmissionSequence(sigma, tosses)

viterbi_path, _ = hmm.viterbi(sequence)

print(header('Viterbi Path'))
print(viterbi_path)
print()

states_probabilities = hmm.posterior(sequence)

print(header('State Probabilities'))
print(states_probabilities)
