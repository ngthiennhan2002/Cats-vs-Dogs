from utils.lib import *

DATA_DIR = './PetImages'

def remove_invalid_images(dir):
    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        try:
            img = Image.open(file_path)
        except IOError:
            os.remove(file_path)


def preprocessing():
    CAT_DIR = r'C:\Users\ASUS\Desktop\Luyện tập AI - ML - DL\Tensorflow\Cats vs Dogs Classification\PetImages\Cat\\'
    DOG_DIR = r'C:\Users\ASUS\Desktop\Luyện tập AI - ML - DL\Tensorflow\Cats vs Dogs Classification\PetImages\\Dog\\'
    remove_invalid_images(CAT_DIR)
    remove_invalid_images(DOG_DIR)

    datagen = ImageDataGenerator(
        rescale=1./225,
        # rotation_range=40,
        # width_shift_range=0.2,
        # height_shift_range=0.2,
        # shear_range=0.2,
        # zoom_range=0.2,
        # horizontal_flip=True,
        # fill_mode='nearest',
        validation_split=0.2
    )

    train_generator = datagen.flow_from_directory(
        DATA_DIR,
        target_size=(150, 150),
        batch_size=64,
        class_mode='binary',
        subset='training'
    )

    validation_generator = datagen.flow_from_directory(
        DATA_DIR,
        target_size=(150, 150),
        batch_size=64,
        class_mode='binary',
        subset='validation'
    )

    return train_generator, validation_generator