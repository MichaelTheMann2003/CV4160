import subprocess
import os

def extract_frames(video_path, output_folder, frame_interval):    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # FFmpeg command to extract frames
    command = [
        'ffmpeg', '-i', video_path,
        '-vf', f'fps=1/{frame_interval}',
        os.path.join(output_folder, 'frame_%04d.jpg')
    ]
    
    # Run the command
    subprocess.run(command, check=True)
    print(f"Frames extracted to '{output_folder}'")

# Example usage
video_path = 'guitar1.mp4'              # Path to your video file
output_folder = 'output_frames'          # Folder to save extracted frames
frame_interval = 30                    # Interval in seconds

extract_frames(video_path, output_folder, frame_interval)
