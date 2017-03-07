from utils.image_io import load_video_info
from utils.arg_parse import parse_args
from srdcf_tracker import SRDCF_tracker

# This demo script runs the SRDCF tracker on the included "Couple" video.
# Load video information
params = parse_args()
srdcf_tracker = SRDCF_tracker(params)

# Run SRDCF
srdcf_tracker.track()