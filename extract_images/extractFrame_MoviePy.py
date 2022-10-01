# -------------------------
# Author : Pythoslabs
# About : This gets all the frames at 1 second intervals and writes into a folder using MoviePy
# Date Created : 5 May  2019
# Input :  Movie file name
# Output : Folder where the images have to be written


from moviepy.editor import VideoFileClip, concatenate_videoclips

def extractFiles(input_video_path,output_folder):
    base_video_file = VideoFileClip(input_video_path)
    for t_sec in  range(0,int(base_video_file.duration)):
        base_video_file.save_frame(".//%s//frame_%d.jpg" %(output_folder,t_sec), t=t_sec)
        print("extracting ..frame#%d" %(t_sec))
        
        

folder_frames_extract = r"..\output\\"
folder_input_video =  r"..\\input\\"
video_clip  = "00.mp4"

base_file= folder_input_video + video_clip

# == Debug ==
print("folder_frames_extract=" + folder_frames_extract)
print("base_file = " + base_file)


extractFiles(base_file,folder_frames_extract)
