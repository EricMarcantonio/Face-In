import pickle

from keras.models import load_model
from keras.optimizers import Adam
from numpy import expand_dims

from loadDataSetForTraining import extract_face, get_embedding

# Holds model

# Loading model
with open("trained_model", "rb") as f:
    model = pickle.load(f)

# Load the encoder
with open("out_encoder", "rb") as f:
    out_encoder = pickle.load(f)


def getPrediction(filename):
    '''Compile and load the facenet embedding'''
    MODELK = load_model('facenet_keras.h5')
    optimizer = Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
    MODELK.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    oneEmb = get_embedding(MODELK, extract_face("test_pics/" + filename))

    samples = expand_dims(oneEmb, axis=0)
    yhat_class = model.predict(samples)
    yhat_prob = model.predict_proba(samples)

    class_index = yhat_class[0]
    class_prob = yhat_prob[0, class_index] * 100

    predict_names = out_encoder.inverse_transform(yhat_class)

    print(predict_names[0])
    print(round(class_prob, 5))
