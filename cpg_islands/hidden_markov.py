""":mod:`cpg_islands.finder` --- A CpG Island finder

This is based heavily on information and code from the following articles and
tutorials:

* `HMM and GHMM Tutorial <http://codecereal.blogspot.com/2011/05/hidden-markov-models.html>`_
* `BYU HMM Project <http://dna.cs.byu.edu/bio465/Labs/hmm.shtml>`_ and
  `GHMM Tutorial <http://dna.cs.byu.edu/bio465/Labs/hmmtut.shtml>`_
* `CpG Islands and HMM article <http://codecereal.blogspot.com/2011/06/cpg-islands-2.html>`_

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
