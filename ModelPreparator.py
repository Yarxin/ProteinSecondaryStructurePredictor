from TextParser import read_record, letter_to_num, _aa_dict
from numpy import array, argmax
from keras.utils import to_categorical


class ModelPreparator:

    @staticmethod
    def PrepareIntSequence(model_list):
        for item in model_list:
            item.int_sequence, item.is_valid = letter_to_num(item.sequence, _aa_dict)
            print(item.id)
            print(item.sequence)
            print(item.int_sequence)
            print(item.secondary_structure)
            print(item.is_valid)
            sequence_len = len(item.sequence)
            print('Długośc łańcucha:' + str(sequence_len))

        return model_list

    @staticmethod
    def PrepareOneHotEncodedSequence(model_list):
        for item in model_list:
            if item.int_sequence != -1:
                data = array(item.int_sequence)
                print(data)
                item.hot_encoded_sequence = to_categorical(data)
                print(item.hot_encoded_sequence)

    @staticmethod
    def RemoveInvalidSequences(model_list):
        for item in model_list:
            if item.int_sequence == -1:
                model_list.remove(item)

        return model_list
