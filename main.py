from utils.lib import *
from utils.visualization import *
from utils.read_file import *

def main():
    accuracy, val_accuracy, loss, val_loss = read_history('history.txt')

    visualization(accuracy, val_accuracy, loss, val_loss)

main()