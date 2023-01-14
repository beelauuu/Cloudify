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
christmas_colors = ["#ff0000", "#ff7878", "#ffffff", "#74d680", "#378b29"]
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


def christmas_color_func(
    word, font_size, position, orientation, random_state=None, **kwargs
):
    return random.choice(christmas_colors)


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
