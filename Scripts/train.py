from fastai.vision.all import *

# Define paths
path = Path('Pneumonologos/XRays')
train_path = path/'Train'
val_path = path/'Val'

# Create data loaders
dls = ImageDataLoaders.from_folder(path, train='Train', valid='Val',
                                   test='Test',
                                   item_tfms=Resize(460),
                                   batch_tfms=aug_transforms())

# Create learner
learn = cnn_learner(dls, resnet34, metrics=[accuracy, RocAucBinary()])

# Train the model
learn.fine_tune(4)

# Save the trained model
learn.export('Pneumonologos/Models/pneumonia_classifier.pkl')
