1. Work on the same library:
   1. by now you should be able to do something like this
      1. HEHEHAHA.data.convert_to_tfRecords(X_train, Y_train)
   2. Now using your library we should be able to do this:
      1. HEHEHAHA.transform(random_pad_crop(random_flip(cutout(rotate(x, 10), 8,8)), 4, 32)
      2. HEHEHAHA.showAndPlotImage(5, 5, misclassified/ParticularClass/Random/MisclassifiedClass)
   3. Use TensorFlow Profiler (https://www.tensorflow.org/tensorboard/r2/tensorboard_profiling_keras) and write a tutorial on a blog and share the link. Use CProfile, observe the results and write a readme on how to interpret the results in the same blog.