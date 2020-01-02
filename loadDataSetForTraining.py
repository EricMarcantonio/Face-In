from os import listdir

from PIL import Image
from keras.models import load_model
from mtcnn.mtcnn import MTCNN
from numpy import asarray, expand_dims

from matplotlib import pyplot

'''
Extracts a face from a single file.

TAKES: path to filename, including file name
RETURNS: a face as an NumPy array

'''


def extract_face(filename, required_size=(160, 160)):
    # load image from file
    image = Image.open(filename)
    # convert to RGB, if needed
    image = image.convert('RGB')
    # convert to array
    pixels = asarray(image)

    # create the detector, using default weights
    detector = MTCNN()
    # detect faces in the image
    results = detector.detect_faces(pixels)
    # extract the bounding box from the first face
    x1, y1, width, height = results[0]['box']
    # bug fix
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    # extract the face
    face = pixels[y1:y2, x1:x2]
    # resize pixels to the model size
    image = Image.fromarray(face)
    image = image.resize(required_size)
    face_array = asarray(image)




    return face_array


'''
Takes all files from an folder, and returns their faces

TAKES: a folder path
RETURNS: an array full of face arrays
'''


def load_faces(directory):
    faces = list()
    # enumerate files
    for filename in listdir(directory):
        # path
        path = directory + filename
        # get face
        face = extract_face(path)
        # store
        faces.append(face)
    return faces


'''
Gets the faces and names for each person.

TAKES: the parent directory to each person-folder RETURNS: 2 arrays; 1: an array full of the face embeddings of each 
folder (so to speak) 2. the folder names, which become labels later 
'''


def load_dataset(directory):
    X, y = list(), list()
    # enumerate folders, on per class
    for subdir in listdir(directory):
        # path
        path = directory + '/' + subdir + '/'
        # skip any files that might be in the dirc

        # load all faces in the subdirectory
        faces = load_faces(path)
        # create labels
        labels = [subdir for _ in range(len(faces))]
        # summarize progress
        print('>loaded %d examples for class: %s' % (len(faces), subdir))
        # store
        X.extend(faces)
        y.extend(labels)
    return asarray(X), asarray(y)


'''
Using the google facenet model, create the embeddings for each photo

TAKES: the facenet model, and a singlular face array. Run the load_directory first to get all the extracted face arrays
RETURNS: the face embedding for that model

'''


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


def returnForModelTraining(model = load_model("facenet_keras.h5"), PATH = "rawPictures"):
    trainX, trainy = load_dataset(PATH)

    newTrainX = []
    for eachFace in trainX:
        temp = get_embedding(model, eachFace)
        newTrainX.append(temp)
    return asarray(newTrainX), trainy

