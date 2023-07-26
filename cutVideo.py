from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import json

path_to_raw_video = "./rawVideo"
path_to_edited_video = "./editedVideo"

# load setting
with open('cutVideoConfig.json', 'r') as f:
    config = json.load(f)
video_duration_to_edit = config['videoDurationInSecond']


def get_video_file_in_directory():
    path = path_to_raw_video
    dir_list = os.listdir(path)
    if len(dir_list) == 0:
        print("no video to edit. please, add video to rawVideo directory.")
    return dir_list


def edit_video(video_name):
    video = path_to_raw_video + '/' + video_name
    clip = VideoFileClip(video)
    video_duration = clip.duration
    number_of_subclip = int(video_duration/video_duration_to_edit) +1
    video_version = 0
    end_time = 0
    for i in range(number_of_subclip):
        video_version += 1
        start_time = end_time
        end_time = start_time + video_duration_to_edit
        new_name = "./outputSubVideo/"+str(video_version)+'_'+video_name
        print(start_time,end_time)
        ffmpeg_extract_subclip(video, start_time, end_time, targetname=new_name)


if __name__ == '__main__':
    all_raw_video = get_video_file_in_directory()
    is_done = 0
    for video_path in all_raw_video:
        edit_video(video_path)
        is_done += 1
        print('Done: ' + str(is_done) + '/' + str(len(all_raw_video)))
