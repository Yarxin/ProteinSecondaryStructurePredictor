from JsonService import load_json
from ModelPreparator import ModelPreparator
from matplotlib import pyplot as plt
import model
import dataProcessor
json_path = 'Sequences/protein2.json'

model_list = load_json(json_path)

ratio_list = []
print('Wczytano dane')

model_list = ModelPreparator.PrepareIntSequence(model_list)
print('Przetłumaczono literki na cyferki')

model_list = ModelPreparator.RemoveInvalidSequences(model_list)
print('Usunięto wadliwe sekwencje')

X_set_string, Y_set_string = dataProcessor.PrepareData(model_list)
X_set_int, Y_set_int = ModelPreparator.MakeIntsAgain(X_set_string, Y_set_string)

X_set_encoded, Y_set_encoded = ModelPreparator.GetOneHotEncoding(X_set_int, Y_set_int)
print('Przygotowano zbiory danych')

X_train, X_test, X_val = dataProcessor.SplitDataX(X_set_encoded)
Y_train, Y_test, Y_val = dataProcessor.SplitDataY(Y_set_encoded)

X_train_r = dataProcessor.ReshapeDataX(X_train)
X_test_r = dataProcessor.ReshapeDataX(X_test)
X_val_r = dataProcessor.ReshapeDataX(X_val)

net = model.CNN_model()

history = None

history = net.fit(X_train_r, Y_train, epochs=model.nn_epochs, batch_size=model.batch_dim, shuffle=True,
                        validation_data=(X_val_r, Y_val))

scores = net.evaluate(X_test_r, Y_test)
print("Loss: " + str(scores[0]) + ", Accuracy: " + str(scores[1]) + ", MAE: " + str(scores[2]))

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, model.nn_epochs + 1)

plt.plot(epochs, acc, label='Dokładność trenowania')
plt.plot(epochs, val_acc, label='Dokładność walidacji')
plt.title('Dokładność trenowania i walidacji')
plt.legend()

plt.figure()

plt.plot(epochs, loss, label='Strata trenowania')
plt.plot(epochs, val_loss, label='Strata walidacji')
plt.title('Strata trenowania i walidacji')
plt.legend()

plt.show()