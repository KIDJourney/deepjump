import os.path
from subprocess import call

from skimage import io as imageio


def get_screen_shoot(image_name='tmp.png', download_path="./images/"):
    try:
        os.makedirs('images')
    except:
        pass
    download_path = os.path.join(download_path, image_name)
    call(['adb', 'shell', 'screencap', '-p', os.path.join('/sdcard/', image_name)])
    call(['adb', 'pull', '/sdcard/tmp.png', download_path])
    return imageio.imread(download_path)


def click_screen(x, y, t):
    x, y, t = str(x), str(y), str(t)
    call(['adb', 'swipe', x, y, x, y, t])
