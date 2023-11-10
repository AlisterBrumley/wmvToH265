# setting command
def cmd_set(args, input_path, conv_file):
    ffmpeg_command = [
        "ffmpeg",
        "-i",
        str(input_path),
        "-c:v",
        "libx265",
        "-tag:v",
        "hvc1",
        "-crf",
        args.crf,
        "-preset",
        args.preset,
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-f",
        "mp4",
        str(conv_file),
        "-y",
        "-nostdin",
    ]

    # adding optional args for ffmpeg
    if args.silent:
        ffmpeg_command.insert(5, "-x265-params")
        ffmpeg_command.insert(6, "log-level=none")
        ffmpeg_command.append("-nostats")
        ffmpeg_command.append("-loglevel")
        ffmpeg_command.append("quiet")
    elif args.quiet:
        ffmpeg_command.insert(5, "-x265-params")
        ffmpeg_command.insert(6, "log-level=none")
        ffmpeg_command.append("-nostats")
        ffmpeg_command.append("-loglevel")
        ffmpeg_command.append("warning")
    if args.progress:
        ffmpeg_command.append("-stats")

    return ffmpeg_command


# setting command for test mode
def test_set(args, input_path, conv_file):
    # set vars for readability
    clip_length = args.test[0]
    start_time = args.test[1]

    # create command
    ffmpeg_command = [
        "ffmpeg",
        "-ss",
        start_time,
        "-i",
        str(input_path),
        "-c:v",
        "libx265",
        "-tag:v",
        "hvc1",
        "-crf",
        args.crf,
        "-preset",
        args.preset,
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-f",
        "mp4",
        "-t",
        clip_length,
        str(conv_file),
        "-y",
        "-nostdin",
    ]

    # adding optional args for ffmpeg
    if args.silent:
        ffmpeg_command.insert(7, "-x265-params")
        ffmpeg_command.insert(8, "log-level=none")
        ffmpeg_command.append("-nostats")
        ffmpeg_command.append("-loglevel")
        ffmpeg_command.append("quiet")
    elif args.quiet:
        ffmpeg_command.insert(7, "-x265-params")
        ffmpeg_command.insert(8, "log-level=none")
        ffmpeg_command.append("-nostats")
        ffmpeg_command.append("-loglevel")
        ffmpeg_command.append("warning")
    if args.progress:
        ffmpeg_command.append("-stats")

    return ffmpeg_command
