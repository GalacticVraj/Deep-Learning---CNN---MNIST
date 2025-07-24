from flask import Flask, render_template, request, jsonify
from PIL import Image, ImageOps
import numpy as np
import base64, io
import tensorflow as tf

# Load the model
model = tf.keras.models.load_model("model.h5")

# Setup Flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        image_data = data["image"].split(",")[1]
        image = Image.open(io.BytesIO(base64.b64decode(image_data))).convert("L")
        
        # Invert (white on black)
        image = ImageOps.invert(image)

        # Resize to 28x28 (but better to center it first)
        image = image.resize((28, 28))

        # Convert to numpy array
        image = np.array(image)

        # Apply a threshold to clean up fuzzy pixels
        image = np.where(image > 50, 255, 0).astype(np.uint8)

        # Normalize
        image = image / 255.0

        # Reshape for model
        image = image.reshape(1, 28, 28, 1)

        prediction = model.predict(image)
        digit = int(np.argmax(prediction))
        print("Predicted:", digit)
        return jsonify({"digit": digit})
    except Exception as e:
        print("Prediction error:", e)
        return jsonify({"digit": "Error"}), 500



# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         print("POST /predict received")  # Debug print

#         data = request.get_json()
#         image_data = data["image"].split(",")[1]
#         image = Image.open(io.BytesIO(base64.b64decode(image_data))).convert("L")
#         image = ImageOps.invert(image).resize((28, 28))
#         image = np.array(image) / 255.0
#         image = image.reshape(1, 28, 28, 1)

#         prediction = model.predict(image)
#         digit = int(np.argmax(prediction))
#         print("Predicted:", digit)
#         return jsonify({"digit": digit})
#     except Exception as e:
#         print("Prediction error:", e)
#         return jsonify({"digit": "Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
