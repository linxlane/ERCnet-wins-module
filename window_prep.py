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
windows_job_out_path = 'OUT_' + args.job_name + '_windows/'
shutil.rmtree(windows_job_out_path, ignore_errors=True)
Path(windows_job_out_path).mkdir()

# --- Copy Directories and Files ---
standard_job_path = 'OUT_' + args.job_name + '/'
shutil.copy(standard_job_path + 'Dropped_gene_log.csv', windows_job_out_path)
shutil.copy(standard_job_path + 'Run_data_counts_log.csv', windows_job_out_path)
shutil.copytree(standard_job_path + 'benchmark/', windows_job_out_path + 'benchmark/', dirs_exist_ok=True)
#shutil.copy(standard_job_path + 'benchmark/' + args.job_name + '_Phylogenomics_benchmark.tsv', windows_job_out_path)
shutil.copy(standard_job_path + 'Species_mapping.csv', windows_job_out_path)
shutil.copy(standard_job_path + 'Seq_counts_per_species.csv', windows_job_out_path)
shutil.copy(standard_job_path + 'Filtered_genefam_dataset.csv', windows_job_out_path)
shutil.copytree(standard_job_path + 'HOG_seqs/', windows_job_out_path + 'HOG_seqs/', dirs_exist_ok=True)
shutil.copytree(standard_job_path + 'Alns/', windows_job_out_path + 'Alns/', dirs_exist_ok=True)
shutil.copytree(standard_job_path + 'TAPER_Alns/', windows_job_out_path + 'TAPER_Alns/', dirs_exist_ok=True)
full_Gb_alns_path = windows_job_out_path + '/Gb_alns_full_length/'
Path(full_Gb_alns_path).mkdir()
shutil.copytree(standard_job_path + 'Gb_alns/', full_Gb_alns_path, dirs_exist_ok=True)
shutil.copytree(standard_job_path + 'Aln_pruning/', windows_job_out_path + 'Aln_pruning/', dirs_exist_ok=True)
