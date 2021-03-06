from tensorflow.keras.models import load_model

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense

classifier = Sequential()
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Flatten())
classifier.add(Dense(units = 1, activation = 'sigmoid'))
classifier.compile(optimizer='adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1. / 255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1. / 255)
training_set = train_datagen.flow_from_directory('training_set', target_size = (64, 64), batch_size = 8, class_mode = 'binary')
test_set = test_datagen.flow_from_directory('test_set', target_size = (64, 64), batch_size = 8, class_mode = 'binary')
classifier.fit_generator(training_set, steps_per_epoch  = 24, epochs = 2, validation_data = test_set, validation_steps = 1000)
classifier.save('my_model.h5')