# get_image_paths.py
import os

def get_image_paths():
    # ディレクトリ取得するやつ

    DIR_NAME = os.path.dirname(__file__)+"/icons"
    EXT = '.png'
    image_list = []
    files = os.listdir(DIR_NAME)

    # ディレクトリ内のファイルを拡張子をチェックし、画像ファイルのパスをリストに追加
    for file in files:
        if file.endswith(EXT):
            image_list.append(os.path.join(DIR_NAME, file))
    print("--------------------------")
    return image_list

if __name__ == "__main__":
    get_image_paths()


