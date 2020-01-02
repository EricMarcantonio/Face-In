from os import listdir

from PreProcessData.extract_face import extract_face

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
