from os import listdir

from loadTrainSaveModelEncoder import trainModel


from usingPreTrainedModel import getPrediction

trainModel()


for filename in listdir("test_pics"):

    predicted_name, prediction_percent = getPrediction(filename)

    print("I think this picture is, " + str(predicted_name) + " and I am " + str(prediction_percent) + "% sure. It really was " + str(filename))
