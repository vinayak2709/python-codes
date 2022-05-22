import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--value", required=True, help="Path to the image")
args = vars(ap.parse_args())
print(args)
