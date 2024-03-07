import os 

rootdir = os.getcwd() 

print (rootdir)

def get_uploaded_images():
    uploads = []
    for subdir, dirs, files in os.walk(rootdir + '/uploads/'): 
        for file in files:
            uploads.append(os.path.join(subdir, file))      
    return uploads