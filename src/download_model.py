import gdown, os

model_path_dict = {
    "BERT-pokemon-gen2.ckpt": "https://drive.google.com/file/d/1-21oR8vFDkip300rJHA9Ywq_0bhm5Xkd/view?usp=drive_link",
    "MicrosoftGit-flickr8k-gen1.ckpt": "https://drive.google.com/file/d/1-AkSC9Gj97c5X9ySGMFnu8PjaJwjFWpm/view?usp=drive_link",
}

model_root = "model/hub"
model_file_name = "pytorch_model.bin"


def download_model():
    for model in model_path_dict.keys():
        url = model_path_dict[model]
        file_id = url.split("/")[-2]

        download_link = f"https://drive.google.com/uc?/export=download&id={file_id}"
        model_path = f"{model_root}/{model}/{model_file_name}"

        if not os.path.exists(model_path):
            gdown.download(url=download_link, output=model_path, resume=True)
