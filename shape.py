import numpy as np
from PIL import Image
from collections import Counter
from wordcloud import WordCloud

#Spotify Shape
def generate_spotify_word_cloud(color, artist_names):
    #Open up the shape and replace the transparent background with white.
    spotify_mask = np.array(Image.open("static/img/spotifyTransparent.png"))
    spotify_mask[spotify_mask == 0] = 255

    #Create the wordcloud with all the details
    wordcloud = WordCloud(
    font_path = "static/font/KeepOnTruckin-Aq32.ttf", 
    background_color=None,
    width=1500,
    height=1500,
    mode = "RGBA", 
    mask=spotify_mask,)
    word_could_dict = Counter(artist_names)
    wordcloud.generate_from_frequencies(word_could_dict)
    wordcloud.recolor(color_func = color)

    #Save it as a file
    wordcloud.to_file('static/img/wordcloud.png')

#Star Shape
def generate_star_word_cloud(color, artist_names):
    star_mask = np.array(Image.open("static/img/starTransparent.png"))
    star_mask[star_mask == 0] = 255
    wordcloud = WordCloud(
    font_path = "static/font/KeepOnTruckin-Aq32.ttf", 
    background_color=None,
    width=1500,
    height=1500,
    mode = "RGBA", 
    mask=star_mask,)
    word_could_dict = Counter(artist_names)
    wordcloud.generate_from_frequencies(word_could_dict)
    wordcloud.recolor(color_func = color)
    wordcloud.to_file('static/img/wordcloud.png')

#Heart Shape
def generate_heart_word_cloud(color, artist_names):
    heart_mask = np.array(Image.open("static/img/heartTransparent.png"))
    heart_mask[heart_mask == 0] = 255
    wordcloud = WordCloud(
    font_path = "static/font/KeepOnTruckin-Aq32.ttf", 
    background_color=None, 
    width=1500,
    height=1500,
    mode = "RGBA", 
    mask=heart_mask,)
    word_could_dict = Counter(artist_names)
    wordcloud.generate_from_frequencies(word_could_dict)
    wordcloud.recolor(color_func = color)
    wordcloud.to_file('static/img/wordcloud.png')

#Moon Shape
def generate_moon_word_cloud(color, artist_names):
    moon_mask = np.array(Image.open("static/img/moonTransparent.png")) 
    moon_mask[moon_mask == 0] = 255
    wordcloud = WordCloud(
    font_path = "static/font/KeepOnTruckin-Aq32.ttf", 
    background_color=None, 
    width=1500,
    height=1500,
    mode = "RGBA", 
    mask=moon_mask,)
    word_could_dict = Counter(artist_names)
    wordcloud.generate_from_frequencies(word_could_dict)
    wordcloud.recolor(color_func = color)
    wordcloud.to_file('static/img/wordcloud.png')

#Tree Shape
def generate_tree_word_cloud(color, artist_names):
    tree_mask = np.array(Image.open("static/img/treeTransparent.png"))
    tree_mask[tree_mask == 0] = 255
    wordcloud = WordCloud(
    font_path= "static/font/KeepOnTruckin-Aq32.ttf", 
    background_color=None, 
    width=1500,
    height=1500,
    mode = "RGBA", 
    mask=tree_mask,)
    word_could_dict = Counter(artist_names)
    wordcloud.generate_from_frequencies(word_could_dict)
    wordcloud.recolor(color_func = color)
    wordcloud.to_file('static/img/wordcloud.png')

#Pacman Shape
def generate_pacman_word_cloud(color, artist_names):
    pacman_mask = np.array(Image.open("static/img/pacmanTransparent.png"))
    pacman_mask[pacman_mask == 0] = 255
    wordcloud = WordCloud(
    font_path = "static/font/KeepOnTruckin-Aq32.ttf", 
    background_color=None,
    width=1500,
    height=1500,
    mode = "RGBA", 
    mask=pacman_mask,)
    word_could_dict = Counter(artist_names)
    wordcloud.generate_from_frequencies(word_could_dict)
    wordcloud.recolor(color_func = color)
    wordcloud.to_file('static/img/wordcloud.png')

#Default
def generate_normal_word_cloud(color, artist_names):
    wordcloud = WordCloud(
    font_path = "static/font/KeepOnTruckin-Aq32.ttf", 
    background_color=None, 
    width=1500,
    height=1500,
    mode = "RGBA", 
    )
    word_could_dict = Counter(artist_names)
    wordcloud.generate_from_frequencies(word_could_dict)
    wordcloud.recolor(color_func = color)
    wordcloud.to_file('static/img/wordcloud.png')