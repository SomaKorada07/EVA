1. Vanilla network - Total params: **9,484**; val_acc: **0.9898**; epoch: 25th; Batch Size: 32

   from keras.layers import Activation

   model = Sequential()

   model.add(Convolution2D(8, 3, input_shape=(28,28,1), use_bias=False)) # RF - 3X3, O/P - 26x26
   model.add(Activation('relu'))

   model.add(Convolution2D(14, 3, use_bias=False)) # RF - 5X5, O/P - 24x24
   model.add(Activation('relu'))

   model.add(Convolution2D(16, 3, use_bias=False)) # RF - 7X7, O/P - 22x22
   model.add(Activation('relu'))

   model.add(Convolution2D(8, 1, use_bias=False))
   model.add(MaxPooling2D(pool_size = (2, 2), strides=None, padding='valid', data_format=None)) # RF - 14X14, O/P - 11x11

   model.add(Convolution2D(8, 3, use_bias=False)) # RF - 16X16, O/P - 9X9
   model.add(Activation('relu'))

   model.add(Convolution2D(14, 3, use_bias=False)) # RF - 16X16, O/P - 7X7
   model.add(Activation('relu'))

   model.add(Convolution2D(16, 3, use_bias=False)) # RF - 18X18, O/P - 5X5
   model.add(Activation('relu'))

   model.add(Convolution2D(10, 1, use_bias=False))
   model.add(Activation('relu'))

   model.add(Convolution2D(10, 5, use_bias=False)) # RF - 20X20, O/P - 5X5

   model.add(Flatten())
   model.add(Activation('softmax'))

2. Adding Dropout and Increasing Batch Size - Total params: **9,484**; val_acc: **0.9917**; epoch: 17th; Batch Size: 128

   from keras.layers import Activation

   model = Sequential()

   model.add(Convolution2D(8, 3, input_shape=(28,28,1), use_bias=False)) # RF - 3X3, O/P - 26x26
   model.add(Activation('relu'))

   model.add(Convolution2D(14, 3, use_bias=False)) # RF - 5X5, O/P - 24x24
   model.add(Dropout(0.125))
   model.add(Activation('relu'))

   model.add(Convolution2D(16, 3, use_bias=False)) # RF - 7X7, O/P - 22x22
   model.add(Dropout(0.125))
   model.add(Activation('relu'))

   model.add(Convolution2D(8, 1, use_bias=False))
   model.add(MaxPooling2D(pool_size = (2, 2), strides=None, padding='valid', data_format=None)) # RF - 14X14, O/P - 11x11

   model.add(Convolution2D(8, 3, use_bias=False)) # RF - 16X16, O/P - 9X9
   model.add(Dropout(0.125))
   model.add(Activation('relu'))

   model.add(Convolution2D(14, 3, use_bias=False)) # RF - 16X16, O/P - 7X7
   model.add(Dropout(0.125))
   model.add(Activation('relu'))

   model.add(Convolution2D(16, 3, use_bias=False)) # RF - 18X18, O/P - 5X5
   model.add(Dropout(0.125))
   model.add(Activation('relu'))

   model.add(Convolution2D(10, 1, use_bias=False))
   model.add(Activation('relu'))

   model.add(Convolution2D(10, 5, use_bias=False)) # RF - 20X20, O/P - 5X5

   model.add(Flatten())
   model.add(Activation('softmax'))

3. Adding BatchNormalization - Total params: **9,724**; val_acc: **0.9918**; epoch: 25th; Batch Size: 128

   from keras.layers import Activation

   model = Sequential()

   model.add(Convolution2D(8, 3, input_shape=(28,28,1), use_bias=False)) # RF - 3X3, O/P - 26x26
   model.add(BatchNormalization())
   model.add(Activation('relu'))

   model.add(BatchNormalization())
   model.add(Convolution2D(14, 3, use_bias=False)) # RF - 5X5, O/P - 24x24
   model.add(Dropout(0.125))
   model.add(Activation('relu'))

   model.add(BatchNormalization())
   model.add(Convolution2D(16, 3, use_bias=False)) # RF - 7X7, O/P - 22x22
   model.add(Dropout(0.125))
   model.add(Activation('relu'))

   model.add(Convolution2D(8, 1, use_bias=False))
   model.add(MaxPooling2D(pool_size = (2, 2), strides=None, padding='valid', data_format=None)) # RF - 14X14, O/P - 11x11

   model.add(BatchNormalization())
   model.add(Convolution2D(8, 3, use_bias=False)) # RF - 16X16, O/P - 9X9
   model.add(Dropout(0.125))
   model.add(Activation('relu'))

   model.add(BatchNormalization())
   model.add(Convolution2D(14, 3, use_bias=False)) # RF - 16X16, O/P - 7X7
   model.add(Dropout(0.125))
   model.add(Activation('relu'))

   model.add(BatchNormalization())
   model.add(Convolution2D(16, 3, use_bias=False)) # RF - 18X18, O/P - 5X5
   model.add(Dropout(0.125))
   model.add(Activation('relu'))

   model.add(Convolution2D(10, 1, use_bias=False))
   model.add(Activation('relu'))

   model.add(Convolution2D(10, 5, use_bias=False)) # RF - 20X20, O/P - 5X5

   model.add(Flatten())
   model.add(Activation('softmax'))

4. Adding LR Scheduler and changing Dropout position (moved to before BN) - Total params: **9,724**; val_acc: **0.9940**; epoch: 25th; Batch Size: 128

   from keras.layers import Activation

   model = Sequential()

   model.add(Convolution2D(8, 3, input_shape=(28,28,1), use_bias=False)) # RF - 3X3, O/P - 26x26
   model.add(BatchNormalization())
   model.add(Activation('relu'))

   model.add(Dropout(0.125))
   model.add(BatchNormalization())
   model.add(Convolution2D(14, 3, use_bias=False)) # RF - 5X5, O/P - 24x24
   model.add(Activation('relu'))

   model.add(Dropout(0.125))
   model.add(BatchNormalization())
   model.add(Convolution2D(16, 3, use_bias=False)) # RF - 7X7, O/P - 22x22
   model.add(Activation('relu'))

   model.add(Convolution2D(8, 1, use_bias=False))
   model.add(Activation('relu'))
   model.add(MaxPooling2D(pool_size = (2, 2), strides=None, padding='valid', data_format=None)) # RF - 14X14, O/P - 11x11

   model.add(BatchNormalization())
   model.add(Convolution2D(8, 3, use_bias=False)) # RF - 16X16, O/P - 9X9
   model.add(Activation('relu'))

   model.add(Dropout(0.125))
   model.add(BatchNormalization())
   model.add(Convolution2D(14, 3, use_bias=False)) # RF - 18X18, O/P - 7X7
   model.add(Activation('relu'))

   model.add(Dropout(0.125))
   model.add(BatchNormalization())
   model.add(Convolution2D(16, 3, use_bias=False)) # RF - 20X20, O/P - 5X5
   model.add(Activation('relu'))

   model.add(Convolution2D(10, 1, use_bias=False))
   model.add(Activation('relu'))
   model.add(Convolution2D(10, 5, use_bias=False)) # RF - 20X20, O/P - 5X5

   model.add(Flatten())
   model.add(Activation('softmax'))

5. Final - Total params: **8,068**; val_acc: **0.9941**; epoch: 40th; Batch Size: 128

   from keras.layers import Activation

   model = Sequential()

   model.add(Convolution2D(8, 3, input_shape=(28,28,1), use_bias=False)) # RF - 3X3, O/P - 26x26
   model.add(BatchNormalization())
   model.add(Activation('relu'))

   model.add(Dropout(0.125))
   model.add(BatchNormalization())
   model.add(Convolution2D(10, 3, use_bias=False)) # RF - 5X5, O/P - 24x24
   model.add(Activation('relu'))

   model.add(Dropout(0.125))
   model.add(BatchNormalization())
   model.add(Convolution2D(16, 3, use_bias=False)) # RF - 7X7, O/P - 22x22
   model.add(Activation('relu'))

   model.add(Convolution2D(8, 1, use_bias=False))
   model.add(MaxPooling2D(pool_size = (2, 2), strides=None, padding='valid', data_format=None)) # RF - 14X14, O/P - 11x11

   model.add(Dropout(0.125))
   model.add(BatchNormalization())
   model.add(Convolution2D(8, 3, use_bias=False)) # RF - 16X16, O/P - 9X9
   model.add(Activation('relu'))

   model.add(BatchNormalization())
   model.add(Convolution2D(10, 3, use_bias=False)) # RF - 18X18, O/P - 7X7
   model.add(Activation('relu'))

   model.add(Dropout(0.125))
   model.add(BatchNormalization())
   model.add(Convolution2D(16, 3, use_bias=False)) # RF - 20X20, O/P - 5X5
   model.add(Activation('relu'))

   model.add(BatchNormalization())
   model.add(Convolution2D(10, 1, use_bias=False)) # RF - 20X20, O/P - 5X5
   model.add(Activation('relu'))

   model.add(Dropout(0.125))
   model.add(BatchNormalization())
   model.add(Convolution2D(10, 5, use_bias=False)) # RF - 20X20, O/P - 5X5

   model.add(Flatten())
   model.add(Activation('softmax'))