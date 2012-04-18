""":mod:`cpg_islands.finder` --- A CpG Island finder

This is based heavily on information and code from the following articles and
tutorials:

* `HMM and GHMM Tutorial <http://codecereal.blogspot.com/2011/05/hidden-markov-models.html>`_
* `BYU HMM Project <http://dna.cs.byu.edu/bio465/Labs/hmm.shtml>`_ and
  `GHMM Tutorial <http://dna.cs.byu.edu/bio465/Labs/hmmtut.shtml>`_
* `CpG Islands and HMM article <http://codecereal.blogspot.com/2011/06/cpg-islands-2.html>`_

"""

import ghmm

class CpGIslandFinder(object):
    """Locates CpG islands in DNA sequences."""
    def __init__(self):
        """Initialize the Hidden Markov Model."""
        # initialize the alphabet
        # self.alphabet = ['A', 'C', 'G', 'T']    
        self.alphabet = ghmm.DNA
        
        # transition matrix: rows and columns means origin and destiny states
        # state 0: normal (not a CpG island)
        # state 1: CpG island
        self.transition_probabilities = [
            # normal
            # |
            # |    island
            # |    |
            [0.9, 0.1], # normal
            [0.3, 0.7], # island
            ]

        # emission probabilities
        #               A    C    G    T
        emit_normal = [.25, .15, .25, .35]
        emit_island = [.25, .25, .25, .25]
        self.emissions_probabilities = [emit_normal, emit_island]
        
        # initial probabilities (assume uniform)
        self.initial_probabilities = [0.5] * 2

        # create the Hidden Markov Model
        self.hmm = ghmm.HMMFromMatrices(
            self.alphabet,
            ghmm.DiscreteDistribution(self.alphabet),
            self.transition_probabilities,
            self.emissions_probabilities,
            self.initial_probabilities
            )

    def __str__(self):
        return str(self.hmm)

    def learn(self, sequence):
        """Learn from another DNA sequence.

        :param sequence: the untagged DNA sequence
        :type sequence: :class:`str`
        """
        emission_sequence = ghmm.EmissionSequence(self.alphabet, list(sequence))
        self.hmm.baumWelch(emission_sequence)
