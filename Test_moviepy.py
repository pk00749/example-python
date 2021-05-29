from moviepy.video.io.VideoFileClip import VideoFileClip

# video = VideoFileClip('D:\\_Download\\pythonmeetup-cut.mp4')
# video = video.subclip(t_start='00:00:00.00', t_end='01:45:00.00')
# video.to_videofile('D:\\_Download\\pythonmeetup-cut_1.mp4', fps=60, remove_temp=True)


video = VideoFileClip('D:\\_Download\\pythonmeetup-cut.mp4')
video = video.subclip(t_start='01:45:00.01', t_end='03:30:06.00')
video.to_videofile('D:\\_Download\\pythonmeetup-cut_2.mp4', fps=60, remove_temp=True)