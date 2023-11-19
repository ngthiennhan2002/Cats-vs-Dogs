from utils.lib import *

def visualization(accuracy, val_accuracy, loss, val_loss):
    epochs = range(len(accuracy))

    fig, axes = plt.subplots(2, 1, figsize=(6, 6))

    axes[0].plot(epochs, accuracy, 'r', label='Training accuracy')
    axes[0].plot(epochs, val_accuracy, 'b', label='Validation accuracy')
    axes[0].set_title('Train and validation accuracy')
    axes[0].legend()

    axes[1].plot(epochs, loss, 'r', label='Training loss')
    axes[1].plot(epochs, val_loss, 'b', label='Validation loss')
    axes[1].set_title('Train and validation loss')
    axes[1].legend()

    plt.tight_layout()
    plt.show()

