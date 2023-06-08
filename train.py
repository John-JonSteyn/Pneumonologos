import sys
from fastai.vision.all import *

# Define paths
path = Path('./XRays')
train_path = path/'Train'
val_path = path/'Val'

# Verify folder structure
if not path.exists():
    print(f"ERROR: Path '{path}' does not exist.")
    sys.exit(1)
if not train_path.exists():
    print(f"ERROR: Training path '{train_path}' does not exist.")
    sys.exit(1)
if not val_path.exists():
    print(f"ERROR: Validation path '{val_path}' does not exist.")
    sys.exit(1)

# Create data loaders
dls = ImageDataLoaders.from_folder(path, train='Train', valid='Val',
                                   test='Test',
                                   item_tfms=Resize(460),
                                   batch_tfms=aug_transforms())

# Verify data loaders
if dls.train_ds is None:
    print("ERROR: Training dataset not loaded.")
    sys.exit(1)
if dls.valid_ds is None:
    print("ERROR: Validation dataset not loaded.")
    sys.exit(1)

# Create learner
learn = cnn_learner(dls, resnet34, metrics=[accuracy, RocAucBinary()])

# Train the model
learn.fine_tune(4)

# Save the trained model
learn.export('Pneumonologos/Models/pneumonia_classifier.pkl')
