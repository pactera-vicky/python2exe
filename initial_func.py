# encoding:utf-8
# @date:
# @editor: vicky
# @environment:
# @brief:


import logging
import cv2 as cv
import sys


def initial_logger():
    FORMAT = '%(asctime)s-%(levelname)s: %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    logger = logging.getLogger(__name__)
    return logger


def resize_image_type(im):
    """
    resize image to a size multiple of 32 which is required by the network
    args:
        img(array): array with shape [h, w, c]
    return(tuple):
        img, (ratio_h, ratio_w)
    """
    max_side_len = 960
    h, w, _ = im.shape

    resize_w = w
    resize_h = h

    # limit the max side
    if max(resize_h, resize_w) > max_side_len:
        if resize_h > resize_w:
            ratio = float(max_side_len) / resize_h
        else:
            ratio = float(max_side_len) / resize_w
    else:
        ratio = 1.
    resize_h = int(resize_h * ratio)
    resize_w = int(resize_w * ratio)
    if resize_h % 32 == 0:
        resize_h = resize_h
    elif resize_h // 32 <= 1:
        resize_h = 32
    else:
        resize_h = (resize_h // 32) * 32
    if resize_w % 32 == 0:
        resize_w = resize_w
    elif resize_w // 32 <= 1:
        resize_w = 32
    else:
        resize_w = (resize_w // 32) * 32
    try:
        if int(resize_w) <= 0 or int(resize_h) <= 0:
            return None, (None, None)
        im = cv.resize(im, (int(resize_w), int(resize_h)))
    except:
        print(im.shape, resize_w, resize_h)
        sys.exit(0)
    ratio_h = resize_h / float(h)
    ratio_w = resize_w / float(w)
    return im, (ratio_h, ratio_w)

