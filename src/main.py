import os
from src import ChatHandler, settings
import time

def main():
    folder_path = settings.folder_path
    for filename in os.listdir(folder_path):
        if not filename.endswith(settings.valid_extensions):
            continue

        file_path = os.path.join(folder_path, filename)
        ch = ChatHandler()(file_path)

        print(f"========={filename}============")
        ch.summary()

if __name__ == '__main__':
    main()
