import os
import shutil


def get_dest_dir(): # prompt user for destination directory and save to file
    if os.path.isfile("dest_dir.txt"):  # check if dest_dir.txt exists, set dest_dir to contents of file
        with open("dest_dir.txt", "r") as file:
            dest_dir = file.read().strip()
        user_input = input(f"\nCurrent destination directory is {dest_dir}. Press Enter to use, or input new directory:\n")
        if user_input:  # if user input is not empty, set dest_dir to user input and save to dest_dir.txt
            dest_dir = user_input
            with open("dest_dir.txt", "w") as file:
                file.write(dest_dir)
    else:
        dest_dir = input("\nEnter destination directory:\n")  # if dest_dir.txt does not exist, prompt user for dest_dir
        with open("dest_dir.txt", "w") as file:
            file.write(dest_dir)

    return dest_dir


def rename_files(book_dir, dest_dir):  # move and rename files
    new_book_dir = os.path.join(dest_dir, os.path.basename(book_dir))  # set correct folder name for new book directory
    shutil.copytree(book_dir, new_book_dir)  # copy book directory to destination directory

    file_count = 0  # used to count files and rename sequentially

    for dirpath, dirnames, filenames in sorted(os.walk(new_book_dir)):  # walk through new book directory and find files
        for file_name in sorted(filenames):
            file_count += 1  # increment file_count for sequential renaming
            file_extension = os.path.splitext(file_name)[1]  # get file extension for renaming
            new_file_name = f"{file_count:03d}{file_extension}"  # generate new file name
            file_path = os.path.join(dirpath, file_name)  # get full path of file to move
            new_file_path = os.path.join(new_book_dir, new_file_name)  # generate new file path
            os.rename(file_path, new_file_path)  # move and rename file
            print(f"Moved and renamed {file_name} to {new_file_name}")

    print("\nFinished moving and renaming files.\n")

    for dirpath, dirnames, filenames in os.walk(new_book_dir, topdown=False):  # walk through new dir and remove empty dirs
        if not os.listdir(dirpath):
            os.rmdir(dirpath)
            print(f"Removed empty directory: {dirpath}")

    print("\nFinished removing empty directories.")


def main():
    book_dir = input("Enter book directory:\n")
    dest_dir = get_dest_dir()
    print(f"Book directory: {book_dir}")
    print(f"Destination directory: {dest_dir}\n")
    rename_files(book_dir, dest_dir)
    print("\nAll done!")


if __name__ == "__main__":
    main()
