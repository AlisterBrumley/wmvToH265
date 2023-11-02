# setting command
def cmd_set(args, input_path, conv_file, video_dir):
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
        str(conv_file),
        "-y",
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
