import json
import glob
import pathlib
import zipfile


def main():
    zip_fnames = glob.glob("*.zip")
    zip_fnames

    for fn in zip_fnames:
        with zipfile.ZipFile(fn, "r") as zip_ref:
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
    main()
