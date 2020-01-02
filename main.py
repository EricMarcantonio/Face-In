import os
import time
from matplotlib import pyplot

# Reducing verbosity level 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from loadTrainSaveModelEncoder import trainModel
from usingPreTrainedModel import getPrediction


def testImage():
    for filename in os.listdir("test_pics"):
        predicted_name, prediction_percent, face_pixels = getPrediction(filename)

        pyplot.imshow(face_pixels)
        pyplot.title(str(predicted_name + " " + str(round(prediction_percent, 2))))
        pyplot.show()

        print("I think this picture is, %s and I am %f %% sure. It really was %s" % (predicted_name, prediction_percent, filename)) 


def menu():
    print("=== FACEIT ===")
    print("MENU")
    print("1. Train")
    print("2. Test")
    print("3. Exit")
    
    while True:
        userInput = input(": ")
        if userInput == "1":
            start_time = time.time()
            trainModel()
            end_time = time.time()
            print('Total training time: ', end_time - start_time)
        elif userInput == "2":
            start_time = time.time()
            testImage()
            end_time = time.time()
            print('Total testing time: ', end_time - start_time)
        elif userInput == "3":
            exit(0)
        else:
            print("=== INVALID INPUT ===")
            trainModel()
            testImage()

# Priyanka Chopra
# Shahrukh Khan

if __name__ == "__main__":
    menu()
