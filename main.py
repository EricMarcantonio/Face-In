from keras.models import load_model
from numpy import expand_dims
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC

from loadDataSetForTraining import returnForModelTraining, extract_face, get_embedding

trainX, trainy = returnForModelTraining()

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
trainy = out_encoder.transform(trainy)

# fit model
model = SVC(kernel='linear', probability=True)
model.fit(trainX, trainy)

'''
Testing!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

oneEmb = get_embedding(load_model('facenet_keras.h5'), extract_face("test_pics/testConnor.JPG"))

samples = expand_dims(oneEmb, axis=0)
yhat_class = model.predict(samples)
yhat_prob = model.predict_proba(samples)

class_index = yhat_class[0]
class_prob = yhat_prob[0, class_index] * 100

predict_names = out_encoder.inverse_transform(yhat_class)

print(predict_names[0])
print(class_prob)
