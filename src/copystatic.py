import os, shutil

def copy_files_recursive(src, dst):
    if os.path.isdir(src):
        os.mkdir(dst)
        print(f"directory {dst} created")
        files = os.listdir(src)
        for file in files:
            new_src = os.path.join(src, file)
            new_dst = os.path.join(dst, file)
            copy_files_recursive(new_src, new_dst)

    elif os.path.isfile(src):
        shutil.copy(src, dst)
        print(f"file {src} copied to {dst}")

    else:
        print(f"invalid source: {src}")
