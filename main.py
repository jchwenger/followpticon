import json
import pathlib
import zipfile
import argparse


def main(args):
    with zipfile.ZipFile(args.file, "r") as zip_ref:
        zip_ref.extractall(".")

    d = pathlib.Path("connections/followers_and_following/")
    d_fers = pathlib.Path("followers_1.json")
    d_fing = pathlib.Path("following.json")

    with (d / d_fers).open() as i:
        followers_data = json.load(i)
    with (d / d_fing).open() as i:
        following_data = json.load(i)

    followers = set([f["string_list_data"][0]["value"] for f in followers_data])
    following = set(
        [
            f["string_list_data"][0]["value"]
            for f in following_data["relationships_following"]
        ]
    )

    print(f"They follow you, you don't follow them:")
    print()

    for f in followers - following:
        print(f"{f}")

    print("-" * 40)
    print()

    print(f"You follow them, they don't follow you:")
    print()

    for f in following - followers:
        print(f"{f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""See who you follow and doesn't follow you back, and vice versa, on Instagram."""
    )

    parser.add_argument(
        "file",
        type=str,
        help="""Zip file containing Instagram following/follower information (to be requested in your setttings and downloaded manually.""",
    )

    args = parser.parse_args()

    main(args)
