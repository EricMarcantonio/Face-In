import time
from os import listdir
from keras.models import load_model
from keras.optimizers import Adam
from numpy import expand_dims
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
from keras.optimizers import Adam
import tensorflow as tf

from loadDataSetForTraining import returnForModelTraining, extract_face, get_embedding

import pickle
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

print("SAVING ENCODER")
with open("out_encoder", "wb") as f:
    pickle.dump(out_encoder,f)
print("ENCODER SAVED")

trainy = out_encoder.transform(trainy)

# fit model
model = SVC(kernel='linear', probability=True)

start_time = time.time()
model.fit(trainX, trainy)
end_time = time.time()
print("Trained Model in %s" % str(end_time - start_time))

'''
Testing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
print("SAVING MODEL")
with open("trained_model", "wb") as f:
    pickle.dump(model, f)
print("MODEL SAVED")
MODELK = load_model('facenet_keras.h5')



optimizer = Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
MODELK.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])


for filename in listdir("test_pics"):
    print(filename)
    
    oneEmb = get_embedding(MODELK, extract_face("test_pics/" + filename))

    samples = expand_dims(oneEmb, axis=0)
    yhat_class = model.predict(samples)
    yhat_prob = model.predict_proba(samples)

    class_index = yhat_class[0]
    class_prob = yhat_prob[0, class_index] * 100

    predict_names = out_encoder.inverse_transform(yhat_class)

    print(predict_names[0])
    print(round(class_prob, 5))
