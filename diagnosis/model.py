# See README. Placeholder deterministic inference.
from PIL import Image
import os
LABELS = ['No DR','Mild','Moderate','Severe','Proliferative']
def run_inference_on_image(image_path: str):
    try:
        s = os.path.getsize(image_path)
        idx = (s // 1024) % len(LABELS)
        pred = LABELS[idx]
    except Exception:
        pred = LABELS[0]
    return {'prediction': pred, 'scores': {l: round(1.0/len(LABELS), 3) for l in LABELS}}
