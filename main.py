# Authors: Robert Layton <robertlayton@gmail.com>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Mathieu Blondel <mathieu@mblondel.org>
#
# License: BSD 3 clause

import numpy as np
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from PIL import Image
import io
from fastapi import FastAPI,File
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

def get_image_from_bytes(binary_image: bytes) -> Image:
    """Convert image from bytes to PIL RGB format
    
    Args:
        binary_image (bytes): The binary representation of the image
    
    Returns:
        PIL.Image: The image in PIL RGB format
    """
    input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")
    return input_image

@app.post('/predict')
def predict(file: bytes = File(...)):
    n_colors = 64
    img = get_image_from_bytes(file)
    china = np.array(img, dtype=np.float64) / 255
    w, h, d = original_shape = tuple(china.shape)
    assert d == 3
    image_array = np.reshape(china, (w * h, d))
    image_array_sample = shuffle(image_array, random_state=0, n_samples=1_000)
    kmeans = KMeans(n_clusters=n_colors, n_init="auto", random_state=0).fit(
        image_array_sample
    )
    return_centers = {}
    cluster_centers = kmeans.cluster_centers_*255
    for i in range(len(kmeans.cluster_centers_)):
        return_centers[i] = cluster_centers[i].tolist()
    return return_centers


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8009)
