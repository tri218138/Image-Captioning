import argparse
from src.download_model import download_model


def main():
    # Download trained model
    download_model()

    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "--mode", type=str, help="Select mode (pokemon/flickr8k)", default="pokemon"
    )

    args = parser.parse_args()

    if args.mode == "pokemon":
        from src.pokemon import predict

        predict()
    elif args.mode == "flickr8k":
        from src.flickr8k import predict

        predict()
    else:
        print("Invalid mode. Please select 'pokemon' or 'flickr8k'.")


if __name__ == "__main__":
    main()
