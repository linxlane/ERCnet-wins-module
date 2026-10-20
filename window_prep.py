# --- imports ---
import argparse
from pathlib import Path
import shutil

# --- argparse ---
parser = argparse.ArgumentParser()
parser.add_argument('--goi', '-g', required=False, help='Full path to tsv file which provides genes of interets for windows analysis. End with /')
parser.add_argument('--job_name', '-j', required=True, help='Job name of standard ERCnet run. This flag string must match job name exactly.')
args = parser.parse_args()

# Make new windows analysis out directory
Path('OUT_' + args.job_name + '_windows').mkdir()

# --- Copy Directories and Files ---
#shutil.copytree(source_dir, destination_dir)
