# HWR

Download the trained model from:
drive
and place the file "pytorch_model.bin" int he folder "Model".

Use jpg's or png's as input images, place them all in a folder (use the "Input" folder or define your own later)

install the necessary python packages with the following command:
  `pip install -r requirements.txt`

Run the program with python as following:
  `python predict.py <Input directory>`

Or use the predefined input directory:
  `python predict.py Input`
  
The model output will be placed in the "Result" folder, where the output of each seperate image is placed into
a seperate .txt file that has a corresponding name. The inferred text will be placed as a line in this .txt file.
