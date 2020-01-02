import os
import pickle
import time
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder,  Normalizer
from PreProcessData.main import returnForModelTraining


def trainModel():
    if os.path.exists("./out_encoder"):
        os.remove("./out_encoder")
    if os.path.exists("./trained_model"):
        os.remove("./trained_model")
    '''
    Read and preprocess data for training
    '''
    start_time = time.time()
    trainX, trainy = returnForModelTraining()
    end_time = time.time()
    print("Loaded all classes in %s" % str(end_time - start_time))

    '''
    Normalize input vectors
    '''
    in_encoder = Normalizer(norm="l2")
    trainX = in_encoder.transform(trainX)

    '''
    Label encode targets
    '''
    # label encode targets
    out_encoder = LabelEncoder()
    out_encoder.fit(trainy)

    '''
    Save the encoder
    '''
    with open("out_encoder", "wb") as f:
        pickle.dump(out_encoder, f)

    '''
    Fix the labeling
    '''
    trainy = out_encoder.transform(trainy)

    '''Create a blank model for recognition'''
    model = SVC(kernel='linear', probability=True)
    start_time = time.time()

    '''Fit the model'''
    model.fit(trainX, trainy)
    end_time = time.time()
    print("Trained Model in %s" % str(end_time - start_time))

    '''Save the new model'''
    with open("trained_model", "wb") as f:
        pickle.dump(model, f)
