# encoding:utf-8
# @date:
# @editor: vicky
# @environment:
# @brief:  传入参数为图片情况，打包为exe

import os, sys
import cv2 as cv
from initial_func import initial_logger, resize_image_type
root_parent = os.path.dirname(os.path.dirname(os.path.realpath(sys.executable)))
# __dir__ = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(__dir__)


logger = initial_logger()


def main():
    """读入.exe 同目录下的图片文件"""
    current_path = os.path.join(root_parent, "imgs_id")
    # current_path = os.path.join(path_parent, "imgs_id")
    output_path = os.path.join(root_parent, 'imgs_result')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    print("图片保存成功，请打开 {} 下查看 :".format(output_path))
    files = os.listdir(current_path)
    if files is None:
        logger.info("error the path:{} is empty".format(current_path))

    for num, file in enumerate(files):
        src0 = cv.imread(os.path.join(current_path, file), 1)
        src = src0.copy()
        img, (ratio_h, ratio_w) = resize_image_type(src)
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

        if img is None:
            logger.info("error in loading image:{}".format(file))
            continue
        """图片统一命名格式img_1.jpg"""
        img_name = "img_" + str(num) + '.jpg'
        save_file_path = os.path.join(output_path, img_name)
        cv.imwrite(save_file_path, img)


if __name__ == "__main__":
    main()




