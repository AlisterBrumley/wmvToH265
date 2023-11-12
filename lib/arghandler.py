import argparse
import sys
import re
import __main__
from pathlib import Path


def arg_parsing():
    arg_parse = argparse.ArgumentParser(
        description=(
            "Requires FFMPEG!\n"
            + "Iterates through a folder and converts all wmv files to h265 codec, contained in .mp4\n"
            + "To abort a conversion, use SIGINT (usually Ctrl+C)"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    # arguments
    arg_parse.add_argument(
        "-c",
        "--crf",
        metavar="int[0, 51]",
        type=int,
        help=("set crf value (default: 25)\nvalid values are between 0-51"),
        default=25,
        choices=range(0, 52),
    )
    arg_parse.add_argument(
        "-d",
        "--directory",
        metavar="/directory/str",
        type=str,
        help="directory containing wmv files (default: $PWD)",
        default=Path.cwd(),
    )
    arg_parse.add_argument(
        "-l",
        "--local",
        action="store_true",
        help=(
            "copy and convert files on local disk, then copy back when done.\n"
            + "decreases constant small writes on remote drives (external USB, NAS etc)"
        ),
    )
    arg_parse.add_argument(
        "-o",
        "--overwrite",
        action="store_true",
        help="automatically overwrite existing files",
    )
    arg_parse.add_argument(
        "-p",
        "--preset",
        metavar="speed",
        type=str,
        default="medium",
        choices={
            "ultrafast",
            "superfast",
            "veryfast",
            "faster",
            "fast",
            "medium",
            "slow",
            "slower",
            "veryslow",
        },
        help=(
            "set preset value (default: medium)\n"
            + "valid presets: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower and veryslow"
        ),
    )
    arg_parse.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="include subfolders when finding .wmv files",
    )
    arg_parse.add_argument(
        "-s", "--skip", action="store_true", help="automatically skip existing files"
    )
    arg_parse.add_argument(
        "-t",
        "--test",
        metavar="length, starttime",
        type=str,
        nargs="*",
        help="iterate through files and create test conversions,"
        + " default length is one minute, starting at the start of the file\n"
        + "format is 'HH:MM:SS'"
        + " eg. '00:05:00' for 5 minute clip, and '01:02:03' if you want clips starting at 1h2m3s",
    )
    arg_parse.add_argument(
        "-y", "--yes", action="store_true", help="Automatic yes to confirmation prompt"
    )
    arg_parse.add_argument("-L", "--log", action="store_true", help="log ffmpeg output")
    arg_parse.add_argument(
        "-P",
        "--progress",
        action="store_true",
        help="re-enable progress output which is disabled by -Q/R/S",
    )
    arg_parse.add_argument(
        "-Q",
        "--quiet",
        action="store_true",
        help="silence ffmpeg output except errors/warnings/overwrites",
    )
    arg_parse.add_argument(
        "-R",
        "--reallyquiet",
        action="store_true",
        help="silence all prompts and ffmpeg output except errors/warnings/overwrites (equivalent to -qy)",
    )
    arg_parse.add_argument(
        "-S",
        "--silent",
        action="store_true",
        help="silence all output, including warnings/errors and automatically skip exisiting files",
    )

    # parsing above arguments
    args = arg_parse.parse_args()

    return args


# dealing with test mode
def test_validation(test_arg_list):
    # set vars to test against
    re_timeformat = re.compile(r"\d\d:[0-5]\d:[0-5]\d")
    len_test = len(test_arg_list)
    script_name = Path(__main__.__file__).name

    # return default if set with no options
    if test_arg_list == []:
        return ["00:01:00", "00:00:00"]
    # error if incorrect number of timestamps
    elif len_test != 2:
        print("test requires length + time in HH:MM:SS and cannot lead other arguments")
        print("Usage:")
        print(script_name + " -yst")
        print(script_name + " -t 00:05:00 01:02:03")
        print(script_name + " --test 00:05:00 01:02:03")
        sys.exit(1)
    # making sure args match correct format
    elif not all((re_timeformat.fullmatch(entries) for entries in test_arg_list)):
        print("incorrect timestamps for test")
        print("test requires length + time in HH:MM:SS and cannot lead other arguments")
        print("Usage:")
        print(script_name + " -yst")
        print(script_name + " -t 00:05:00 01:02:03")
        print(script_name + " --test 00:05:00 01:02:03")
        sys.exit(1)
    # return if all other options met
    else:
        return test_arg_list
