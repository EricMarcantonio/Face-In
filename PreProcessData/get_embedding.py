'''
Using the google facenet model, create the embeddings for each photo

TAKES: the facenet model, and a singlular face array. Run the load_directory first to get all the extracted face arrays
RETURNS: the face embedding for that model

'''
from numpy import expand_dims


def get_embedding(model, face_pixels):
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
