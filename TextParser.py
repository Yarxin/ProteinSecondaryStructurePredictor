import re
import numpy as np

# Constants
NUM_DIMENSIONS = 3

# Functions for conversion from Mathematica protein files to TFRecords
_aminoacids_dict = {'A': '0', 'C': '1', 'D': '2', 'E': '3', 'F': '4', 'G': '5', 'H': '6', 'I': '7', 'K': '8', 'L': '9',
            'M': '10', 'N': '11', 'P': '12', 'Q': '13', 'R': '14', 'S': '15', 'T': '16', 'V': '17', 'W': '18',
            'Y': '19', 'X': '20'}

_secondary_structure_dict = {'G': '0', 'H': '1', 'I': '2', 'E': '3', 'B': '4', 'T': '5', 'S': '6', 'L': '7'}

_dssp_dict = {'L': '0', 'H': '1', 'B': '2', 'E': '3', 'G': '4', 'I': '5', 'T': '6', 'S': '7'}
_mask_dict = {'-': '0', '+': '1'}

A = np.random.uniform(0.001, 1, 21)
C = np.random.uniform(0.001, 1, 21)
D = np.random.uniform(0.001, 1, 21)
E = np.random.uniform(0.001, 1, 21)
F = np.random.uniform(0.001, 1, 21)
G = np.random.uniform(0.001, 1, 21)
H = np.random.uniform(0.001, 1, 21)
I = np.random.uniform(0.001, 1, 21)
K = np.random.uniform(0.001, 1, 21)
L = np.random.uniform(0.001, 1, 21)
M = np.random.uniform(0.001, 1, 21)
N = np.random.uniform(0.001, 1, 21)
P = np.random.uniform(0.001, 1, 21)
Q = np.random.uniform(0.001, 1, 21)
R = np.random.uniform(0.001, 1, 21)
S = np.random.uniform(0.001, 1, 21)
T = np.random.uniform(0.001, 1, 21)
V = np.random.uniform(0.001, 1, 21)
W = np.random.uniform(0.001, 1, 21)
Y = np.random.uniform(0.001, 1, 21)
X = np.random.uniform(0.001, 1, 21)


class switch(object):
    """Switch statement for Python, based on recipe from Python Cookbook."""

    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        # raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5
            self.fall = True
            return True
        else:
            return False


def letter_to_num(string, dict_):
    """ Convert string of letters to list of ints """
    try:
        patt = re.compile('[' + ''.join(dict_.keys()) + ']')
        num_string = patt.sub(lambda m: dict_[m.group(0)] + ' ', string)
        num = [int(i) for i in num_string.split()]
        return num, True
    except:
        # print('Error')
        return -1, False


def read_record(file_, num_evo_entries):
    """ Read a Mathematica protein record from file and convert into dict. """

    dict_ = {}

    while True:
        next_line = file_.readline()
        for case in switch(next_line):
            if case('[ID]' + '\n'):
                id_ = file_.readline()[:-1]
                dict_.update({'id': id_})
            elif case('[PRIMARY]' + '\n'):
                primary = letter_to_num(file_.readline()[:-1], _aminoacids_dict)
                dict_.update({'primary': primary})
            elif case('[EVOLUTIONARY]' + '\n'):
                evolutionary = []
                for residue in range(num_evo_entries): evolutionary.append(
                    [float(step) for step in file_.readline().split()])
                dict_.update({'evolutionary': evolutionary})
            elif case('[SECONDARY]' + '\n'):
                secondary = letter_to_num(file_.readline()[:-1], _dssp_dict)
                dict_.update({'secondary': secondary})
            elif case('[TERTIARY]' + '\n'):
                tertiary = []
                for axis in range(NUM_DIMENSIONS): tertiary.append([float(coord) for coord in file_.readline().split()])
                dict_.update({'tertiary': tertiary})
            elif case('[MASK]' + '\n'):
                mask = letter_to_num(file_.readline()[:-1], _mask_dict)
                dict_.update({'mask': mask})
            elif case('\n'):
                return dict_
            elif case(''):
                return None


def ToAminoInternalCode(string):
    amino_list = []
    for char in string:
        if char == 'A':
            amino_list.append(A)
        if char == 'C':
            amino_list.append(C)
        if char == 'D':
            amino_list.append(D)
        if char == 'E':
            amino_list.append(E)
        if char == 'F':
            amino_list.append(F)
        if char == 'G':
            amino_list.append(G)
        if char == 'H':
            amino_list.append(H)
        if char == 'I':
            amino_list.append(I)
        if char == 'K':
            amino_list.append(K)
        if char == 'L':
            amino_list.append(L)
        if char == 'M':
            amino_list.append(M)
        if char == 'N':
            amino_list.append(N)
        if char == 'P':
            amino_list.append(P)
        if char == 'Q':
            amino_list.append(Q)
        if char == 'R':
            amino_list.append(R)
        if char == 'S':
            amino_list.append(S)
        if char == 'T':
            amino_list.append(T)
        if char == 'V':
            amino_list.append(V)
        if char == 'W':
            amino_list.append(W)
        if char == 'Y':
            amino_list.append(Y)
        if char == 'X':
            amino_list.append(X)
    X_set = np.asarray(amino_list)
    return X_set
