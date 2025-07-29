import os
import uuid
import subprocess

def extract_frames(
    input_video,
    output_dir,
    fps=1,
    start_time=None,
    end_time=None,
    quality=2,
):
    os.makedirs(output_dir, exist_ok=True)
    temp_dir = os.path.join(output_dir, "temp_frames")
    os.makedirs(temp_dir, exist_ok=True)

    # FFmpeg 直接输出帧到临时文件
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_video,
        "-vf", f"fps={fps}",
        "-qscale:v", str(quality),
    ]
    if start_time:
        ffmpeg_cmd.extend(["-ss", start_time])
    if end_time:
        ffmpeg_cmd.extend(["-to", end_time])
    ffmpeg_cmd.extend([os.path.join(temp_dir, "frame_%04d.jpg")])

    subprocess.run(ffmpeg_cmd, check=True)

    # 重命名为 UUID
    frame_count = 0
    for filename in os.listdir(temp_dir):
        if filename.endswith(".jpg"):
            new_name = f"{uuid.uuid4().hex}.jpg"
            os.rename(
                os.path.join(temp_dir, filename),
                os.path.join(output_dir, new_name)
            )
            frame_count += 1

    # 清理临时目录
    os.rmdir(temp_dir)
    print(f"✅ 成功提取 {frame_count} 帧到 {output_dir}")

if __name__ == "__main__":
    extract_frames(
        input_video="/Users/lucas/Downloads/06-03-16-0.mp4",
        output_dir="/Users/lucas/Downloads/output_frames",
        fps=1/10, # 每10秒一帧
        start_time="00:02:00",
        end_time="00:17:00",
        quality=2,
    )