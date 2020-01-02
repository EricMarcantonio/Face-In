import time
from os import listdir
from matplotlib import pyplot
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from loadTrainSaveModelEncoder import trainModel
from usingPreTrainedModel import getPrediction



start_time = time.time()
trainModel()


for filename in listdir("test_pics"):

    predicted_name, prediction_percent, face_pixels = getPrediction(filename)


    pyplot.imshow(face_pixels)
    pyplot.title(predicted_name)
    pyplot.show()

    print("I think this picture is, " + str(predicted_name) + " and I am " + str(prediction_percent) + "% sure. It really was " + str(filename))
end_time = time.time()



print('Total time: ', end_time - start_time)
