# Legend:
# G – 3_10 helix
# H – α-helix
# I – π-helix
# E – β-sheet
# B – β-bridge
# T – helix turn
# S – bend (high curvature)
# L – coil (none of the above)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv1D, BatchNormalization, Flatten, LSTM
from keras import optimizers

do_summary = True

LR = 0.0009
# LR = 0.0000003
drop_out = 0.38
batch_dim = 64
nn_epochs = 70
window_size = 17

loss = 'categorical_crossentropy'

def CNN_model():
    m = Sequential()
    m.add(Conv1D(128, 5, padding='same', activation='relu', input_shape=(window_size, 21)))
    m.add(BatchNormalization())
    m.add(Dropout(drop_out))
    m.add(Conv1D(128, 3, padding='same', activation='relu'))
    m.add(BatchNormalization())
    m.add(Dropout(drop_out))
    m.add(Conv1D(64, 3, padding='same', activation='relu'))
    m.add(BatchNormalization())
    m.add(Dropout(drop_out))
    m.add(Flatten())
    m.add(Dense(128, activation='relu'))
    m.add(Dense(32, activation='relu'))
    m.add(Dense(8, activation='softmax'))
    opt = optimizers.Adam(lr=LR)
    m.compile(optimizer=opt,
              loss=loss,
              metrics=['accuracy', 'mae'])
    if do_summary:
        print("\nHyper Parameters\n")
        print("Learning Rate: " + str(LR))
        print("Drop out: " + str(drop_out))
        print("Batch dim: " + str(batch_dim))
        print("Number of epochs: " + str(nn_epochs))
        print("\nLoss: " + loss + "\n")

        m.summary()

    return m
