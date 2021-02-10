from JsonService import load_json
from ModelPreparator import ModelPreparator
input_path = 'Sequences/TextRecords/casp7/testing'
json_path = 'Sequences/full_protein_dssp_annotations.json'

model_list = load_json(json_path)
ratio_list = []

model_list = ModelPreparator.PrepareIntSequence(model_list)
model_list = ModelPreparator.RemoveInvalidSequences(model_list)

model_list = ModelPreparator.PrepareOneHotEncodedSequence(model_list)
