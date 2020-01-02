
from loadTrainSaveModelEncoder import trainModel
from usingPreTrainedModel import getPrediction

trainModel()
predicted_name, prediction_percent = getPrediction("testConnor.JPG")

print("I think this picture is, " + str(predicted_name) + " and I am " + str(prediction_percent) + "% sure")
