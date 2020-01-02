import pickle
from os import listdir

from keras.models import load_model
from numpy import expand_dims
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
from loadDataSetForTraining import returnForModelTraining, extract_face, get_embedding


# Holds model
model = None
# Loading model
with open("trained_model", "rb") as f:
    model = pickle.load(f) 

out_encoder = None
with open("out_encoder", "rb") as f:
    out_encoder = pickle.load(f)

for filename in listdir("test_pics"):
    print(filename)

    oneEmb = get_embedding(load_model('facenet_keras.h5', compile=False), extract_face("test_pics/" + filename))

    samples = expand_dims(oneEmb, axis=0)
    yhat_class = model.predict(samples)
    yhat_prob = model.predict_proba(samples)

    class_index = yhat_class[0]
    class_prob = yhat_prob[0, class_index] * 100

    predict_names = out_encoder.inverse_transform(yhat_class)

    print(predict_names[0])
    print(class_prob)
