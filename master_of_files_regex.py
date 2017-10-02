
"""Are you a file extension master? Let's find out by checking if Bill's files are images or audio files. Please use regex if available natively for your language.

You will create 2 string methods:

isAudio/is_audio, matching 1 or + uppercase/lowercase letter(s) (combination possible), with the extension .mp3, .flac, .alac, or .aac.
isImage/is_image, matching 1 or + uppercase/lowercase letter(s) (combination possible), with the extension .jpg, .jpeg, .png, .bmp, or .gif.
Note that this is not a generic image/audio files checker. It's meant to be a test for Bill's files only. Bill doesn't like punctuation. He doesn't like numbers, neither. Thus, his filenames are letter-only

Rules

It should return true or false, simply.
File extensions should consist of lowercase letters and numbers only.
File names should consist of letters only (uppercase, lowercase, or both)
Good luck!"""

import re



def is_audio(file_name):
    """
    >>> is_audio("NothingElseMatters.mp3")
    True

    >>> is_audio("NothingElseMatters.Mp3")
    False

    >>> is_audio("NothingElseMatters.flac")
    True

    >>> is_audio("NothingElseMatters.FLAC")
    False

    >>> is_audio(" Amon Tobin.alac")
    False

    """

    # audio_match = re.match(r"\w+\.mp3|\w+\.flac|\w+\.alac|\w+\.aac", file_name)
    # valid_name = re.match(r"\^[\W]*$", file_name)
    # if audio_match != None and valid_name == None:
    #     return True
    # else:
    #     return False

    return bool(re.match(r"^[a-zA-Z]+\.(mp3|flac|alac|aac)$", file_name))



def is_img(file_name):
    """
    >>> is_img("icon.bmp")
    True

    >>> is_img("icon2.jpg")
    False

    >>> is_img("animate bounce.GIF")
    False


    """
    return bool(re.match(r"[a-zA-Z]+\.(jpg|jpeg|png|bmp|gif)$", file_name))






