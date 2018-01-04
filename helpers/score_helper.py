import skimage.color

from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

SCORE_AREA_R_START = 200
SCORE_AREA_R_END = 300

SCORE_AREA_C_START = 0
SCORE_AREA_C_END = 400


def get_score_area(game_image):
    return game_image[SCORE_AREA_R_START:SCORE_AREA_R_END, SCORE_AREA_C_START, SCORE_AREA_C_END]


def _get_score_object(score_area):
    gray_image = skimage.color.rgb2gray(score_area)
    thresh = threshold_otsu(gray_image)

    bw = closing(gray_image < thresh, square(3))
    cleared = clear_border(bw)
    label_image = label(cleared)

    number_regions = regionprops(label_image)

    regions = []
    for region in number_regions:
        r_min, c_min, r_max, y_max = region.bbox
        regions.append((r_min, c_min, r_max, y_max))
    regions = sorted(regions, key=lambda x: x[1])

    ret_number = []
    for r in regions:
        number_image = gray_image[r[0]:r[2], r[1]:r[3]]
        ret_number.append(number_image)

    return ret_number


def get_score_object(game_image):
    score_area = get_score_area(game_image)
    return _get_score_object(score_area)
