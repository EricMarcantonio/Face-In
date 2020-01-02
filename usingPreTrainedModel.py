import pickle

from keras.models import load_model
from keras.optimizers import Adam
from numpy import expand_dims

# Loading model
from PreProcessData.extract_face import extract_face
from PreProcessData.get_embedding import get_embedding




def getPrediction(filename):
    # Holds model

    with open("trained_model", "rb") as f:
        model = pickle.load(f)

    # Load the encoder
    with open("out_encoder", "rb") as f:
        out_encoder = pickle.load(f)

    oneEmb = get_embedding(extract_face("test_pics/" + filename))

    samples = expand_dims(oneEmb, axis=0)
    yhat_class = model.predict(samples)
    yhat_prob = model.predict_proba(samples)

    class_index = yhat_class[0]
    class_prob = yhat_prob[0, class_index] * 100

    predict_names = out_encoder.inverse_transform(yhat_class)

    return predict_names[0], round(class_prob, 5)
