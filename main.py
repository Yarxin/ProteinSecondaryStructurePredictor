from TextParser import read_record, letter_to_num, _aa_dict
from JsonService import load_json
from keras.preprocessing.text import Tokenizer
from matplotlib import pyplot as plt
input_path = 'Sequences/TextRecords/casp7/testing'
json_path = 'Sequences/full_protein_dssp_annotations.json'

model_list = load_json(json_path)
ratio_list = []

for item in model_list:
    item.int_sequence, item.is_valid = letter_to_num(item.sequence, _aa_dict)
    print(item.id)
    print(item.sequence)
    print(item.int_sequence)
    print(item.secondary_structure)
    print(item.is_valid)
    sequence_len = len(item.sequence)
    secondary_len = len(item.secondary_structure)
    print('Długośc łańcucha:' + str(sequence_len))
