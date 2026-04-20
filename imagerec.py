import numpy as np
from PIL import Image, ImageOps
import ai_edge_litert.interpreter as tflite
# Load model once
interpreter = tflite.Interpreter(model_path="Models/model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

class_labels = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

def is_valid_mri(image_array):
    # MRI scans are typically grayscale.
    # We check if the difference between R, G, and B channels is very low.
    if len(image_array.shape) == 3 and image_array.shape[2] == 3:
        r_g_diff = np.mean(np.abs(image_array[:, :, 0] - image_array[:, :, 1]))
        r_b_diff = np.mean(np.abs(image_array[:, :, 0] - image_array[:, :, 2]))
        
        # If mean channel difference is > 5.0, it's likely a color image (like a selfie)
        if r_g_diff > 5.0 or r_b_diff > 5.0:
            return False
    return True

def imagerecognise(uploadedfile):
    image = Image.open(uploadedfile).convert("RGB")
    
    # Store original data for validation before normalization
    orig_array = np.asarray(image).astype(np.float32)
    is_valid = is_valid_mri(orig_array)
    
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    image_array = np.asarray(image).astype(np.float32)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    interpreter.set_tensor(input_details[0]['index'], image_array)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    print(f"Raw Output Data: {output_data}")

    index = np.argmax(output_data)
    confidence = float(output_data[0][index])

    return class_labels[index], confidence, output_data[0], is_valid