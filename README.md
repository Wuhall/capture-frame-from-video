# capture-frame-from-video

本项目用于从视频中按时间范围和帧率提取图片帧，并支持将图片批量重命名为 UUID。

## 项目结构

- `extract_frames_with_time_range.py`  
  从视频文件中按指定时间范围和帧率提取图片帧，支持设置输出质量，并将帧图片重命名为 UUID。

- `rename_file.py`  
  批量将指定文件夹下的图片文件重命名为 32 位 UUID，支持多种图片格式。

## 使用方法

1. **提取视频帧**
   ```sh
   python extract_frames_with_time_range.py
   ```

2. **批量重命名图片**
    ```sh
    python rename_file.py
    ```