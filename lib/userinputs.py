import sys


# checks amount of .wmv files and ask if they wish to continue
def confirmer(file_list):
    len_file_list = str(len(file_list))
    print(len_file_list + " files found")
    print(
        "WARNING: converting a large amount of files and/or long videos"
        + " can take several hours/days and makes heavy use of your cpu!"
    )
    confirm = input("do you wish to continue? [y/n] ").lower().strip()

    # reasks 3 times if incorrect input, otherwise proceeds
    for cnt in range(4):
        if confirm == "y" or confirm == "yes":
            break
        elif confirm == "n" or confirm == "no":
            print("exiting...")
            sys.exit(0)
        else:
            if cnt == 3:
                print("repeated invalid responses: exiting...")
                sys.exit(1)
            confirm = input("respond with 'y' or 'n': ").lower().strip()


# if user keyboard interrupts(ctrl+c), checks if they want to abort all
def check_abort(interrupted_file):
    print("USER ABORTED CONVERSION ON - " + interrupted_file)
    confirm = input("do you wish to abort all? [y/n] ").lower().strip()

    # evalute or reasks 3 times if incorrect input
    for cnt in range(4):
        if confirm == "y" or confirm == "yes":
            print("exiting...")
            return True
        elif confirm == "n" or confirm == "no":
            break
        else:
            if cnt == 3:
                print("repeated invalid responses: exiting...")
                sys.exit(1)
            confirm = input("respond with 'y' or 'n': ").lower().strip()


# to run when output file already exists
def overwrite_conf(output_path):
    print(output_path + " already exists")
    confirm = input("do you wish to overwrite, skip or abort? [o/s/a] ").lower().strip()

    # evalute or reasks 3 times if incorrect input
    for cnt in range(4):
        if confirm == "o" or confirm == "overwrite":
            return
        elif confirm == "s" or confirm == "skip":
            raise FileExistsError
        elif confirm == "a" or confirm == "abort":
            print("exiting...")
            sys.exit(0)
        else:
            if cnt == 3:
                print("repeated invalid responses: exiting...")
                sys.exit(1)
            confirm = input("respond with 'o', 's' or 'a': ").lower().strip()
