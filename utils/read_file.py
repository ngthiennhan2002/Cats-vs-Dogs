def read_history(file_name):
    with open(file_name, 'r') as file:
            lines = file.readlines()

    lines[0] = lines[0].replace('[', '').replace(']', '')
    lines[1] = lines[1].replace('[', '').replace(']', '')
    lines[2] = lines[2].replace('[', '').replace(']', '')
    lines[3] = lines[3].replace('[', '').replace(']', '')

    accuracy = [float(x) for x in lines[0].strip().split(',')]
    val_accuracy = [float(x) for x in lines[1].strip().split(',')]
    loss = [float(x) for x in lines[2].strip().split(',')]
    val_loss = [float(x) for x in lines[3].strip().split(',')]

    return accuracy, val_accuracy, loss, val_loss