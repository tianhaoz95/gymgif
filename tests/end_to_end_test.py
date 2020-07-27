import os
import gym
from gymgif import generate_gif


def get_asset_dir():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    asset_dir = os.path.join(test_dir, '../assets')
    return asset_dir


def test_generate_gif_from_recording():
    env = gym.make('MountainCar-v0')
    done = False
    env.reset()
    frames = []
    while not done:
        frames.append(env.render(mode='rgb_array'))
        action = env.action_space.sample()
        _, _, done, _ = env.step(action)
    generate_gif(frames, get_asset_dir(), 'render_from_recording.gif')
    env.close()
