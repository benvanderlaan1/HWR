import os
import numpy
import torch
import argparse

from PIL import Image

from transformers import TrOCRProcessor
from transformers import VisionEncoderDecoderModel
from pathlib import Path
import gdown

parser = argparse.ArgumentParser()
parser.add_argument("input_folder")

args = parser.parse_args()

NAMING = "_characters.txt"  # ""


MODEL_DIR = Path("Model")
MODEL_FILE = MODEL_DIR / "pytorch_model.bin"
INPUT_DIR = args.input_folder
RESULT_DIR = Path("result")

# a file
if not MODEL_FILE.exists():
    url = "https://drive.google.com/file/d/1KJ3dGUlk5nFFY8BQQz8r-8k0BCzpvFDq/view?usp=drive_link"
    gdown.download(url, str(MODEL_FILE), quiet=False, fuzzy=True)

if not RESULT_DIR.exists():
    RESULT_DIR.mkdir()

model = VisionEncoderDecoderModel.from_pretrained(str(MODEL_DIR))
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")

for file in os.listdir(INPUT_DIR):
    if file.endswith(".png") or file.endswith(".jpg"):
        image = Image.open(os.path.join(INPUT_DIR, file))
        pixel_values = processor(image, return_tensors="pt").pixel_values
        generated = model.generate(pixel_values)

        generated_text = processor.batch_decode(generated, skip_special_tokens=True)[0]

        with open(RESULT_DIR / (file.split(".")[0] + NAMING), "w+") as f:
            f.write(generated_text)
