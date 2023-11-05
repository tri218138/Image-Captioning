import os
import requests
from pathlib import Path


def download_model_from_url(url, model_save_path: str = "model/hub/"):
    Path(model_save_path).mkdir(parents=True, exist_ok=True)

    with open(model_save_path, "wb") as f:
        response = requests.get(url)
        f.write(response.content)


def load_input_images(img_path: str = "runs/input", prefix: str = "") -> list:
    if not os.path.exists(img_path):
        raise ValueError(f"Directory {img_path} does not exist.")

    image_files = [
        os.path.join(img_path, f)
        for f in os.listdir(img_path)
        if os.path.isfile(os.path.join(img_path, f)) and prefix in f
    ]
    return image_files


def write_output_caption(caption: str, file_name: str, path: str = "runs/output"):
    Path(path).mkdir(parents=True, exist_ok=True)
    name, _ = os.path.splitext(file_name)
    with open(os.path.join(path, name + ".txt"), "w") as f:
        f.write(caption)
