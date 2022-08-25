# create file that has the location of training/test images, classes and backup file

full_path_to_images = 'training_10000_images'
# Defining counter for classes
c = 0

with open(full_path_to_images + '/' + 'classes.names', 'w') as names, \
     open(full_path_to_images + '/' + 'classes.txt', 'r') as txt:

    # Going through all lines in txt file and writing them into names file
    for line in txt:
        names.write(line)  # Copying all info from file txt to names

        # Increasing counter
        c += 1


with open(full_path_to_images + '/' + 'labelled_data.data', 'w') as data:
    # Number of classes
    data.write('classes = ' + str(c) + '\n')

    # Location of the train.txt file
    data.write('train = ' + full_path_to_images + '/' + 'train.txt' + '\n')

    # Location of the test.txt file
    data.write('valid = ' + full_path_to_images + '/' + 'test.txt' + '\n')

    # Location of the classes.names file
    data.write('names = ' + full_path_to_images + '/' + 'classes.names' + '\n')

    # Location where to save weights
    data.write('backup = backup')