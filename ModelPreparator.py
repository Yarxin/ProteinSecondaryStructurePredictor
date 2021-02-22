from TextParser import letter_to_num, _aminoacids_dict, _secondary_structure_dict
from numpy import array
from keras.utils import to_categorical


class ModelPreparator:

    @staticmethod
    def PrepareIntSequence(model_list):
        for item in model_list:
            free_field = True
            item.int_sequence, item.is_valid = letter_to_num(item.sequence, _aminoacids_dict)
            item.secondary_structure_labeled, free_field = letter_to_num(item.secondary_structure, _secondary_structure_dict)

        return model_list

    @staticmethod
    def MakeIntsAgain(X_set, Y_set):
        free_field = True
        x, free_field = letter_to_num(X_set, _aminoacids_dict)
        y, free_field = letter_to_num(Y_set, _secondary_structure_dict)

        return x, y

    @staticmethod
    def GetOneHotEncoding(x, y):
        data_x = array(x)
        data_y = array(y)

        X_set = to_categorical(data_x)
        Y_set = to_categorical(data_y)

        return X_set, Y_set

    @staticmethod
    def RemoveInvalidSequences(model_list):
        for item in model_list:
            if item.int_sequence == -1:
                model_list.remove(item)

        return model_list
