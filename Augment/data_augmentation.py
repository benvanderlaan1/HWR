import os
import random
from PIL import Image
import torchvision.transforms as tf
from tqdm import tqdm

DATA_FOLDER = "Data"
DF_TO_LOAD = '/fixed_iam_lines_gt.txt'

def main():
    names = []
    text = []
    with open(DATA_FOLDER + DF_TO_LOAD) as f:
        lines = f.readlines()
        for line in lines:
            split = line.split("\t")
            #print(split)
            names.append(split[0])
            text.append(split[1][:-1])

    imgs = len(names)
    # Create augmented image and append info to dataframe
    for i in tqdm(range(imgs)):
        augmentImage(names[i], text[i], 0)
        names.append(names[i][:-4] + "augmented0.png")
        text.append(text[i])

        augmentImage(names[i], text[i], 1)
        names.append(names[i][:-4] + "augmented1.png")
        text.append(text[i])

        augmentImage(names[i], text[i], 2)
        names.append(names[i][:-4] + "augmented2.png")
        text.append(text[i])

    # Save newly created augmented data info
    with open("Data/augmented_data.txt", 'w+') as f:
        for name, tex in zip(names,text):
            f.write(name + "\t" + tex + "\n")


def Pad(image, top, bottom, left, right, color):
    width, height = image.size
    new_height = height + top + bottom
    new_width = width + left + right
    result = Image.new(image.mode, (new_width, new_height), color)
    result.paste(image, (right, top))
    return result

def augmentImage(name, text, idx):
    # Load the specified image
    img = Image.open(DATA_FOLDER + "/img/" + name)

    transforms = [tf.RandomPerspective(0.1, fill=255), 
                  tf.RandomRotation(degrees=(-4,4), fill=255), 
                  tf.RandomAffine(degrees=(0,0), shear=(10), fill=255),
                  tf.ElasticTransform(alpha=10.0, fill=255),
                  tf.GaussianBlur(kernel_size=(5,9), sigma=(0.1, 0.2))]

    nrTransforms = random.randint(1,5)
    img = Pad(img, 40, 40, 50, 50, 255)

    for i in range(nrTransforms):
        x = random.randint(0, len(transforms) - 1)
        transform = transforms[x]
        # Perform transform
        img = transform(img)
        del transforms[x]
        
    img.save(DATA_FOLDER + "/img/" + name[:-4] + "augmented" + str(idx) + ".png")

if __name__ == '__main__':
    main()