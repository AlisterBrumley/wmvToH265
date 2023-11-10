import os
import sys
import shutil
from pathlib import Path
from lib.userinputs import overwrite_conf


# check permissions before conversion
def prmsn_check(directory):
    if not os.access(directory, os.W_OK):
        print("User doesn't have write permissions for " + directory)
        print("Try run with 'sudo' or change permissions")
        sys.exit(1)
    elif not os.access(directory, os.R_OK):
        print("User doesn't have read permissions for " + directory)
        print("Try run with 'sudo' or change permissions")
        sys.exit(1)


# prompt user for overwrite
def overwrite_check(output_path, args):
    if output_path.is_file():
        if args.overwrite:
            return
        if args.skip:
            raise FileExistsError
        else:
            output_path = str(output_path)
            return overwrite_conf(output_path)


# copy to work dir on local disk
def copy_local(work_dir, wmv_file):
    # set local Path and copy
    copy_dest = Path(work_dir / wmv_file.name)
    shutil.copy2(wmv_file, copy_dest)

    # return copied Path
    return copy_dest


# copy to original dir on original disk
def copy_back(conv_file, output_path):
    # TODO copyback logs if exist?
    # set path and copy
    shutil.copy2(conv_file, output_path)


# create work dir
def mk_workdir(args):
    work_dir = Path(Path.home() / ".h265convert")
    # creating local mode workdir, unused if not local
    if args.log or args.local:
        os.makedirs(work_dir, exist_ok=True)
    return work_dir


# CURRENTLY NOT USED
# REMOVE OR ADD CHECK FOR LOGS
# remove the working dir for local mode
# def rm_workdir(work_dir):
    # shutil.rmtree(work_dir)
