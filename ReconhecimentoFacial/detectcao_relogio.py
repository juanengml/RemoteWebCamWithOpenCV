import dlib 
opcoes = dlib.simple_object_detector_training_options()
opcoes.add_left_right_image_flips = True
opcoes.C = 5

dlib.train_simple_object_detector("./treinamento_relogio.xml","./recursos/detector_relogios.svm",opcoes)

