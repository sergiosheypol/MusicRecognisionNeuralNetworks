from model import get_model
from dataset import get_dataset
from processing import read_folder

audio_files = '/Volumes/USB DISK/dataset'
dataset = 'dataset_0606'

#####################################################################
########################### PRE PROCESSING ##########################
#####################################################################

read_folder(audio_files, dataset)

#####################################################################
############################# TRAINING ##############################
#####################################################################

# Get values
x_train, x_test, y_train, y_test, input_shape = get_dataset(dataset)

# Get model
model = get_model(input_shape)

# Compile model. Categorical_crossentropy since Softmax
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=70,
          validation_data=(x_test, y_test),
          )

# Tests
score = model.evaluate(x_test, y_test, verbose=0)

model.save('model_0606.h5')

print('test loss:', score[0])
print('Accuracy: ', score[1])

# print(x_test[0:1].shape)

# print(model.predict(x_test[0:1]))
