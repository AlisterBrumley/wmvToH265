# wmvToH265

### Python script that iterates through files and uses ffmpeg to convert wmv files to H265
Basically a wrapper around an ffmpeg call, with some useful options and safety checks.

### How to use
#### Basic use
1. open a terminal or command prompt
2. navigate to video directory using `cd`
3. `python path/to/wmvtoh265.py` or `python3 path/to/wmvtoh265.py`

It will warn you it might take a while and prompt to make sure you want to continue. If you do, it will work through the wmv files and convert them in place.

#### Running from a different directory
This is an alternate way, and probably the easier way to do it. Using `-d` you can specify a directory to iterate over:
1. open a terminal or commmand prompt
2. navigate to where this script is located using `cd`
3. `python wmvtoh265.py -d path/where/wmvs/live` or `python3 wmvtoh265.py -d path/where/wmvs/live`

#### Running locally from servers, other PC's or external drive
You might want to run it from a different computer than where the videos are stored, or on a local SSD instead of a USB hard disk etc. The argument `-l` or `--local` will copy the `.wmv` files to a folder in your home folder (located at `~/.h265convert`), write out the conversion there, copy the `.mp4` back when it's finished, and delete the local files. The same steps as above apply.

#### Other options
There's several other options, including logging, recursive over subfolders and changes to output quality which I won't list here. Access all arguments by running `python3 wmvtoh265.py -h`