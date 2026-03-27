import numpy as np
from PIL import Image, ImageOps
import tflite_runtime.interpreter as tflite

# Load model once
interpreter = tflite.Interpreter(model_path="Models/model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

class_labels = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

def imagerecognise(uploadedfile):
    image = Image.open(uploadedfile).convert("RGB")
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

    image_array = np.asarray(image).astype(np.float32)
    image_array = (image_array / 127.5) - 1
    image_array = np.expand_dims(image_array, axis=0)

    interpreter.set_tensor(input_details[0]['index'], image_array)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])

    index = np.argmax(output_data)
    confidence = float(output_data[0][index])

    return class_labels[index], confidence, output_data[0]