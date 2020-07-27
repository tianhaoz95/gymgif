import os
from PIL import Image


def generate_gif(frames=[], dir='./', filename='gym_game_play.gif'):
    animation_frames = []
    for f in frames:
        f_img = Image.fromarray(f)
        animation_frames.append(f_img)
    animation_frames[0].save(os.path.join(dir, filename), save_all=True, append_images=animation_frames[1:], loop=0)