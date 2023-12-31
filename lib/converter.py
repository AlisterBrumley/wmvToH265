import sys
import os
import subprocess
from pathlib import Path
from datetime import datetime as dt
import lib.filehandlers as fh
import lib.cmdset as cs
from lib.userinputs import check_abort


# contains the main converter loop
def converter(args, video_dir, file_list, work_dir):
    # iterating through files in directory
    for wmv_file in file_list:
        # path for converted file
        output_path = Path(wmv_file).with_suffix(".mp4")

        # checking if file is an actual .wmv, skipping if so
        if not wmv_file.is_file():
            if not args.silent:
                print(str(wmv_file) + " is not a file; skipping")
            continue

        # checking overwrites
        try:
            fh.overwrite_check(output_path, args)
        # using the exception to skip to next
        except FileExistsError:
            continue

        # check if local mode and if so copy files
        # else set variables
        if args.local:
            input_path = fh.copy_local(work_dir, wmv_file)
            conv_file = Path(work_dir / wmv_file.name).with_suffix(".mp4")
        else:
            input_path = wmv_file
            conv_file = output_path

        # set temp file to write into
        temp_file = Path(conv_file).with_suffix(".mp4.part")

        # set command to be used for conversion
        if args.test:
            ffmpeg_command = cs.test_set(args, input_path, temp_file)
        else:
            ffmpeg_command = cs.cmd_set(args, input_path, temp_file)

        # pre-setting the shell environment vars
        enviroment_set = os.environ.copy()
        if args.log:
            timecode = dt.now().strftime("-%d%m%y-%H%M%S")
            log_file = Path(work_dir / (wmv_file.name + timecode + ".log"))
            enviroment_set["FFREPORT"] = "file=" + str(log_file)

        # conversion
        if not args.silent:
            try:
                subprocess.run(ffmpeg_command, check=True, env=enviroment_set)
            except KeyboardInterrupt:
                if not args.reallyquiet:
                    if check_abort(wmv_file.name):
                        sys.exit(0)
                else:
                    sys.exit(0)
            except subprocess.CalledProcessError as e:
                print("CalledProcessError Occurred on " + wmv_file.name)
                print(e)
                print("CONVERSION ABORTED, MOVING TO NEXT FILE")
                print("Ctrl+C or SIGINT TO ABORT")
            except Exception as e:
                print("UNEXPECTED EXCEPTION OCCURRED ON " + wmv_file.name)
                print(e)
                print("CONVERSION ABORTED, MOVING TO NEXT FILE")
                print("TO ABORT Ctrl+C or SIGINT")
        else:
            subprocess.run(ffmpeg_command)

        # renaming converted files
        temp_file.rename(conv_file)

        # copy converted file back if local true
        if args.local:
            fh.copy_back(conv_file, output_path)
            Path.unlink(conv_file)
            Path.unlink(input_path)
