import json
from dataModel import dataModel


def load_json(file_path):
    model_list = []
    with open(file_path) as json_file:
        file = json.load(json_file)
    for element in file:
        model = dataModel()
        obj = file[element]
        for string in obj:
            model.id = element
            if string == 'Sequence':
                model.sequence = obj[string]
            elif string == 'DSSP':
                model.secondary_structure = obj[string]
        model_list.append(model)
    return model_list
