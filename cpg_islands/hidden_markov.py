""":mod:`cpg_islands.hidden_markov` --- The actual model

For now, this is just a sample from a `ghmm tutorial`_.

.. _ghmm tutorial: http://codecereal.blogspot.com/2011/05/hidden-markov-models.html

"""

from __future__ import print_function, division
import sys
import ghmm
from header import header

RAW_ALPHABET = ['A', 'C', 'G', 'T']

# initialize the alphabet
alphabet = ghmm.Alphabet(RAW_ALPHABET)

# use uniform probabilities for transitions, emissions, and initial
# probabilities
transition_probabilities = [[1 / len(
            alphabet) for unused in xrange(
            len(alphabet))] for unused in xrange(len(alphabet))]
emissions_probabilities = transition_probabilities
initial_probabilities = [1 / len(alphabet) for unused in xrange(len(alphabet))]

# create the Hidden Markov Model
hmm = ghmm.HMMFromMatrices(
    alphabet,
    ghmm.DiscreteDistribution(alphabet),
    transition_probabilities,
    emissions_probabilities,
    initial_probabilities
    )

# print the initial model
print(header('Initial HMM'))
print(hmm)

# learn from an emission sequence
emission_sequence = ghmm.EmissionSequence(alphabet, list('ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACTGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGC'))
hmm.baumWelch(emission_sequence)

# print the revised model
print(header('Learned HMM'))
print(hmm)
