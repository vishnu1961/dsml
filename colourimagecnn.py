import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Generate synthetic color dataset
def generate_color_image(color, size=(32,32)):
    img = np.zeros((*size, 3), dtype=np.uint8)
    img[:,:] = color  # fill image with given RGB color
    return img

# Define color classes (RGB)
colors = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
    "yellow": [255, 255, 0],
    "cyan": [0, 255, 255],
    "magenta": [255, 0, 255]
}

# Create dataset
X = []
y = []
for idx, (name, rgb) in enumerate(colors.items()):
    for _ in range(500):  # 500 images per color
        noise = np.random.randint(-20, 20, (32,32,3))  # add slight noise
        img = np.clip(generate_color_image(rgb) + noise, 0, 255)
        X.append(img)
        y.append(idx)

X = np.array(X) / 255.0   # normalize
y = np.array(y)

# Split dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Build CNN
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(len(colors), activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train CNN
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))
# Function to predict color
def predict_color(image):
    img = tf.image.resize(image, (32,32)) / 255.0
    img = np.expand_dims(img, axis=0)  # add batch dimension
    pred = model.predict(img)
    class_idx = np.argmax(pred)
    return list(colors.keys())[class_idx]

# Example: predict a red image
test_img = generate_color_image([250, 10, 10])  # almost red
plt.imshow(test_img)
plt.axis("off")
plt.show()

print("Predicted color:", predict_color(test_img))
