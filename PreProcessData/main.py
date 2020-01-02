from numpy import asarray

from PreProcessData.get_embedding import get_embedding
from PreProcessData.load_dataset import load_dataset
from keras.models import load_model


def returnForModelTraining(model = load_model("facenet_keras.h5"), PATH = "rawPictures"):
    trainX, trainy = load_dataset(PATH)

    newTrainX = []
    for eachFace in trainX:
        temp = get_embedding(model, eachFace)
        newTrainX.append(temp)
    return asarray(newTrainX), trainy