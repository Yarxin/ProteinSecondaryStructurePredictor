from TextParser import read_record, letter_to_num, _aminoacids_dict, _secondary_structure_dict
from numpy import array, argmax
from keras.utils import to_categorical
import numpy as np


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

    @staticmethod
    def CreateX_Y_set(model_list):
        X_set = []
        Y_set = []

        X = np.array([])
        i = 0
        for item in model_list:
            X += item.hot_encoded_secondary_structure
            X_set.append(X)
            i += 1

        xset = np.asarray(X_set)
        print('nic')
        # return X_set, Y_set

