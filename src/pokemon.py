import os
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM
import requests
from pathlib import Path

from src.helper import load_input_images, write_output_caption, download_model_from_url


checkpoint = "microsoft/git-base"
# weights_path = "https://drive.google.com/drive/folders/1xHdbMPG207CquIrKRkU4YiI_j7dGe2C-?usp=sharing"
weights_path = "model/hub/BERT-pokemon-gen2.ckpt"


def predict():
    # Download model from URL
    # model_path = download_model_from_url(weights_path)

    processor = AutoProcessor.from_pretrained(checkpoint)
    model = AutoModelForCausalLM.from_pretrained(weights_path, local_files_only=True)

    device = "cuda" if torch.cuda.is_available() else "cpu"

    img_paths = load_input_images(prefix="pokemon")

    for img_path in img_paths:
        image = Image.open(img_path)

        inputs = processor(images=image, return_tensors="pt").to(device)
        generated_ids = model.generate(pixel_values=inputs.pixel_values, max_length=50)
        generated_caption = processor.batch_decode(
            generated_ids, skip_special_tokens=True
        )[0]

        directory, filename = os.path.split(img_path)
        write_output_caption(generated_caption, filename)


if __name__ == "__main__":
    predict()
