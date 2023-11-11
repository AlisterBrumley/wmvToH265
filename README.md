# wmvToH265

### Python script that iterates through files and uses ffmpeg to convert wmv files to H265
Basically a wrapper around an ffmpeg call, with some useful options and safety checks.


### Default ffmpeg command

### How to use
#### Basic use
1. open a terminal or command prompt
2. navigate to video directory using `cd`
3. `python path/to/wmvtoh265.py`

It will warn you it might take a while and prompt to make sure you want to continue. If you do, it will work through the wmv files and convert them.

#### Running locally from servers, other PC's or external drive
You might want to run it from a different computer than where the videos are stored, or on an SSD instead of a USB hard disk etc. The argument `-l` or `--local` will copy the `.wmv` files to a folder in your home folder (located at `~/.h265convert`), write the conversion there, and then move it back when it's finished. This reduces constant I/O done during the conversion, but it doesn't make it any faster. Although if you have a slow server, using a PC with a faster CPU might.