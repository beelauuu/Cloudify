import itertools
import random

rainbow_colors = [
    "#FF0000",
    "#FF7F00",
    "#FFFF00",
    "#00FF00",
    "#0000FF",
    "#4B0082",
    "#9400D3",
]
tree_colors = ["#dfd8c9", "#a5633c", "#5f6344", "#694b37", "#7a6935"]
summer_colors = ["#75CDD8", "#F0F2E7", "#FF8296", "#FFCA27", "#FFEC00"]
st_patricks_day_colors = ["#224D17", "#099441", "#60A830", "#9FDA40", "#D9DF1D"]
chinese_new_year_colors = [
    "#CC232A",
    "#F5AC27",
    "#FFD84B",
    "#F2888B",
    "#A3262A",
    "#CC9902",
]


def red_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "#F72119"


def orange_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return "#FF5733"


def yellow_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return "#FFF01F"


def green_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return "#39FF14"


def blue_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return "#1F51FF"


def violet_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return "#B026FF"


def pink_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return "#fe019a"


def white_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return "#FFFFFF"


def fall_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return random.choice(tree_colors)


def summer_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return random.choice(summer_colors)


def st_patricks_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return random.choice(st_patricks_day_colors)


def rainbow_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return random.choice(rainbow_colors)


def chinese_new_year_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return random.choice(chinese_new_year_colors)


def spotify_green_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return "#1DB954"


color_func_mapping = {
    "Spotify Green": spotify_green_color_func,
    "Red": red_color_func,
    "Orange": orange_color_func,
    "Yellow": yellow_color_func,
    "Green": green_color_func,
    "Blue": blue_color_func,
    "Purple": violet_color_func,
    "Pink": pink_color_func,
    "White": white_color_func,
    "St Patricks Mix": st_patricks_color_func,
    "Summer Mix": summer_color_func,
    "Fall Mix": fall_color_func,
    "Rainbow Mix": rainbow_color_func,
    "Chinese New Year Mix": chinese_new_year_color_func,
}