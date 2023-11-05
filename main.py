import argparse


def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--mode", type=str, help="Select mode (pokemon/flickr8k)")

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
