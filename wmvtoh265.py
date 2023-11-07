import sys
from pathlib import Path
import lib.arghandler as ah
import lib.filehandlers as fh
from lib.converter import converter
from lib.userinputs import confirmer


def __main__():
    # dealing with arguments
    args = ah.arg_parsing()
    args.crf = str(args.crf)

    # input validation for test
    # if --test was flagged with no arguments it returns list with defaults
    if args.test is not None:
        args.test = ah.test_validation(args.test)

    # args that include others set here
    if args.silent:
        args.reallyquiet = True
        args.skip = True
    if args.reallyquiet:
        args.quiet = True
        args.yes = True

    # set inital vars
    video_dir = Path(args.directory)

    if args.recursive:
        file_list = list(video_dir.rglob("*.wmv"))
    else:
        file_list = list(video_dir.glob("*.wmv"))

    # checking if any wmv files in folder
    if not file_list:
        print("no files detected!")
        sys.exit(1)

    # check number of files and comfirm with user if they want to proceed
    if not args.yes:
        confirmer(file_list)

    # create work_dir directory for logs and local mode
    work_dir = fh.mk_workdir(args)

    # check permissions
    fh.prmsn_check(video_dir)
    if args.log or args.local:
        fh.prmsn_check(work_dir)

    # iterate through files and convert
    converter(args, video_dir, file_list, work_dir)


if __name__ == "__main__":
    __main__()
