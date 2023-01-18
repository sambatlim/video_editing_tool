from moviepy.editor import *
import os
import json

path_to_raw_video = "./rawVideo"
path_to_edited_video = "./editedVideo"
path_to_audio = "./audio"
path_to_logo = "./logo"

# load setting
with open('config.json', 'r') as f:
    config = json.load(f)
video_speed = config['speed']
video_color_effect = config['colorEffect']
video_flip = config['flip']
video_volume = config['audioVolume']


def get_video_file_in_directory():
    path = path_to_raw_video
    dir_list = os.listdir(path)
    return dir_list


def get_audio_path():
    path_audio = path_to_audio
    dir_list_audio = os.listdir(path_audio)
    return dir_list_audio[0]


def get_logo_path():
    path_logo = path_to_logo
    dir_list_logo = os.listdir(path_logo)
    return dir_list_logo[0]


def edit_video(video_name, audio_to_add_to_video, logo_to_add_to_video):
    video = path_to_raw_video+'/'+video_name
    clip = VideoFileClip(video)
    logo = path_to_logo+'/'+logo_to_add_to_video
    # edit speed video
    clip = clip.fx(vfx.speedx, video_speed)
    print("Edit speed complete.")
    # edit saturation video
    clip = clip.fx(vfx.colorx, video_color_effect)
    print("Edit color complete.")
    # flip video
    if video_flip == 1:
        clip.fx(vfx.mirror_x)
        print("flip video complete.")
    # add audio
    audio_clip = AudioFileClip(path_to_audio + '/' + audio_to_add_to_video).set_duration(clip.duration)
    clip = clip.set_audio(audio_clip)
    clip = clip.volumex(video_volume)
    print("Edit audio complete.")
    # add logo
    logo_image = (ImageClip(logo)
                  .set_duration(clip.duration)
                  .resize(height=50)
                  .set_pos(("right", "top")))
    print("add logo complete.")
    final_clip = CompositeVideoClip(
        [
            clip,
            logo_image
        ]
    )
    final_clip.write_videofile(path_to_edited_video+'/'+video_name)


if __name__ == '__main__':
    all_raw_video = get_video_file_in_directory()
    audio_to_add = get_audio_path()
    logo_to_add = get_logo_path()
    is_done = 0
    for video_path in all_raw_video:
        edit_video(video_path, audio_to_add, logo_to_add)
        is_done += 1
        print('Done: '+str(is_done)+'/'+str(len(all_raw_video)))



