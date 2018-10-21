#author : Nashrullah

"""
    Display the image with seperating color by red or green or blue channel.
    t = 2 --> Red channel
    t = 1 --> Green channel
    t = 0 --> Blue channel
"""
def seperateColor(img, t):
    for i in range(3):
        if i == t:
            continue
        img[:,:,i] = 0
    return img
