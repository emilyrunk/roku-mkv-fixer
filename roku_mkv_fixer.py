
import os
from os import listdir
from os.path import isfile, join
import subprocess


# Get the current working directory's absolute path
def get_abs_path():
    cwd = os.getcwd()
    return cwd


# Get a list of all file names within the current working directory
def get_file_names_in_pwd(cwd):
    all_files = []
    for filen in os.listdir(cwd):
        if os.path.isfile(filen):
            all_files.append(filen)
    return all_files


def filter_mkv_files(all_files):
    mkv_list = []
    for name in all_files:
        if name.endswith("mkv"):
            mkv_list.append(name)
    return mkv_list


def convert_mkv(cwd, file_name):
    simple_file_name = file_name[:-4]
    ff_mpeg_command = 'ffmpeg -i {0}/{1}.mkv -c:v copy -strict experimental -c:a aac -ac 2 -ab 256K {0}/{1}.mp4'.format(
        cwd, simple_file_name)
    print("going to run command..", ff_mpeg_command)
    subprocess.call(ff_mpeg_command, shell=True)
    src_name = cwd + '/' + file_name
    dest_name = '{0}/{1}.{2}'.format(cwd, simple_file_name, 'mkv.done')
    os.rename(src_name, dest_name)


def convert_all_mkvs(cwd, mkv_file_names):
    for fn in mkv_file_names:
        convert_mkv(cwd, fn)


def main():
    # Step 0: Determine the absolute path of the present working directory
    abs_path = get_abs_path()

    # Step 1: get all file names in the present working directory
    all_files = get_file_names_in_pwd(abs_path)

    # Step 2: filter out MKV file names so you are left with MKV file names
    mkv_list = filter_mkv_files(all_files)

    # Step 3: for each MKV, run ffmpeg and rename files to mkv.done
    convert_all_mkvs(abs_path, mkv_list)


if __name__ == "__main__":
    main()
else:
    print "not running as main"