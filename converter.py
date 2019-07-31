import imageio
import os

film = os.path.abspath("film.mp4")

def gif_converter(in_Path, target_Format):
    outputPath = os.path.splitext(in_Path)[0] + target_Format

    print(f"Converting {in_Path} \n to {outputPath}")

    reader = imageio.get_reader(in_Path)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps=fps)

    for frame in reader:
        writer.append_data(frame)
        print(f"Frame {frame}")
    
    print("Video converted!")
    writer.close()

gif_converter(film, ".gif")