'''
Using the google facenet model, create the embeddings for each photo

TAKES: the facenet model, and a singlular face array. Run the load_directory first to get all the extracted face arrays
RETURNS: the face embedding for that model

'''

from keras.models import load_model
from keras.optimizers import Adam
from numpy import expand_dims

# Loading model

MODELK = load_model('facenet_keras.h5')
optimizer = Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
MODELK.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])


def get_embedding(face_pixels, model=MODELK):
    # scale pixel values
    face_pixels = face_pixels.astype('float32')
    # standardize pixel values across channels (global)
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    # transform face into one sample
    samples = expand_dims(face_pixels, axis=0)
    # make prediction to get embedding
    yhat = model.predict(samples)

    return yhat[0]
