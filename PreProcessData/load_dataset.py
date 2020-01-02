from os import listdir

from numpy import asarray

from PreProcessData.load_faces import load_faces

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
