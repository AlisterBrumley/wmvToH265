import argparse
from pathlib import Path


def arg_parsing():
    arg_parse = argparse.ArgumentParser(
        description=(
            "Requires FFMPEG!\n"
            + "Iterates through a folder and converts all wmv files to h265 codec, contained in .mp4"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    # arguments
    arg_parse.add_argument(
        "-c",
        "--crf",
        metavar="int[0, 51]",
        type=int,
        help=("Set crf value (default: 25)\n" + "Valid values are between 0-51"),
        default=25,
        choices=range(0, 52),
    )
    arg_parse.add_argument(
        "-d",
        "--directory",
        metavar="/directory/str",
        type=str,
        help="Directory containing wmv files (default: $PWD)",
        default=Path.cwd(),
    )
    arg_parse.add_argument(
        "-l",
        "--local",
        action="store_true",
        help=(
            "Copy and convert files on local disk, then copy back when done.\n"
            + "Decreases constant small writes on remote drives (external USB, NAS etc)"
        ),
    )
    arg_parse.add_argument("-L", "--log", action="store_true", help="log ffmpeg output")
    arg_parse.add_argument(
        "-o",
        "--overwrite",
        action="store_true",
        help="Automatically overwrite existing files",
    )
    arg_parse.add_argument(
        "-p",
        "--preset",
        metavar="speed",
        type=str,
        help=(
            "Set preset value (default: medium)\n"
            + "Valid presets: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower and veryslow"
        ),
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
    )
    arg_parse.add_argument(
        "-P", "--progress", action="store_true", help="Enable progress output (disabled by -q/r/s options)"
    )
    arg_parse.add_argument(
        "-q", "--quiet", action="store_true", help="Silence ffmpeg output except errors/warnings/overwrites"
    )
    arg_parse.add_argument(
        "-r",
        "--reallyquiet",
        action="store_true",
        help="Silence all prompts and ffmpeg outputse except errors/warnings/overwrites (equivalent to -qy)",
    )
    arg_parse.add_argument(
        "-R", "--recursive", action="store_true", help="Include subfolders when finding .wmv files"
    )
    arg_parse.add_argument(
        "-s",
        "--silent",
        action="store_true",
        help="Silence all output, including warnings/errors and automatically skip exisiting files",
    )
    arg_parse.add_argument(
        "-S",
        "--skip",
        action="store_true",
        help="Automatically skip existing files"
    )
    arg_parse.add_argument("-y", "--yes", action="store_true", help="Automatic yes to confirmation prompt")

    # parsing above arguments
    args = arg_parse.parse_args()

    return args
