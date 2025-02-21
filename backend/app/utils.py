import base64

def encode_image(image):
    """Encode image to base64 string."""
    return base64.b64encode(image).decode("utf-8")