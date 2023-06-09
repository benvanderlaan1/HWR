import os
import numpy
import torch
import argparse

from PIL import Image

from transformers import TrOCRProcessor
from transformers import VisionEncoderDecoderModel

parser = argparse.ArgumentParser()
parser.add_argument('input_folder')

args = parser.parse_args()

MODEL_DIR = "Model"
INPUT_DIR = args.input_folder
RESULT_DIR = "result"

if not os.path.exists(RESULT_DIR):
    os.mkdir(RESULT_DIR)

model = VisionEncoderDecoderModel.from_pretrained(MODEL_DIR)
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")

for file in os.listdir(INPUT_DIR):
    if file.endswith(".png") or file.endswith(".jpg"):
        image = Image.open(os.path.join(INPUT_DIR, file))
        pixel_values = processor(image, return_tensors="pt").pixel_values
        generated = model.generate(pixel_values)

        generated_text = processor.batch_decode(generated, skip_special_tokens=True)[0]

        with open(RESULT_DIR + "/" + file.split(".")[0] + "_characters.txt", "w+") as f:
            f.write(generated_text)