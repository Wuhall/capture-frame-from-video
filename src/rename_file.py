import os
import uuid

def rename_images_to_uuid(folder_path, supported_extensions=('.jpg', '.jpeg', '.png', '.webp')):
    """
    将文件夹中的图片重命名为 32 位 UUID
    :param folder_path: 图片文件夹路径
    :param supported_extensions: 支持的图片扩展名（不区分大小写）
    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"文件夹不存在: {folder_path}")

    renamed_count = 0
    for filename in os.listdir(folder_path):
        # 检查文件扩展名是否在支持列表中
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in supported_extensions:
            # 生成 32 位 UUID 并保留原扩展名
            new_name = f"{uuid.uuid4().hex}{file_ext}"
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)

            # 重命名文件
            os.rename(old_path, new_path)
            renamed_count += 1
            print(f"Renamed: {filename} -> {new_name}")

    print(f"✅ 完成！共重命名 {renamed_count} 张图片。")

if __name__ == "__main__":
    # 示例调用：处理指定文件夹中的图片
    rename_images_to_uuid(
        folder_path="/Users/lucas/Downloads/output_frames",  # 替换为你的图片文件夹路径
        supported_extensions=(".jpg", ".png", ".jpeg", ".webp")  # 可自定义支持的格式
    )