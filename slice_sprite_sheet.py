from PIL import Image
import os
import sys

def slice_sprite_sheet(file_path, frames_horizontal, frames_vertical):
    # Открываем исходное изображение
    sprite_sheet = Image.open(file_path)
    sprite_width, sprite_height = sprite_sheet.size
    
    # Вычисляем размеры одного кадра
    frame_width = sprite_width // frames_horizontal
    frame_height = sprite_height // frames_vertical
    
    # Получаем имя файла и расширение
    file_name, file_extension = os.path.splitext(file_path)
    base_name = os.path.basename(file_name)
    
    # Создаем папку с именем исходного файла
    output_folder = base_name
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Общее количество кадров
    total_frames = frames_horizontal * frames_vertical
    
    # Определяем формат номера файла с ведущими нулями
    number_format = "{:0" + str(len(str(total_frames))) + "d}"
    
    # Нарезаем кадры и сохраняем их
    frame_number = 1
    for vertical_frame in range(frames_vertical):
        for horizontal_frame in range(frames_horizontal):
            left = horizontal_frame * frame_width
            top = vertical_frame * frame_height
            right = left + frame_width
            bottom = top + frame_height
            frame = sprite_sheet.crop((left, top, right, bottom))
            frame.save(os.path.join(output_folder, f"{base_name}_{number_format.format(frame_number)}{file_extension}"))
            frame_number += 1

# Пример использования
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python slice_sprite_sheet.py <file_path> <frames_horizontal> <frames_vertical>")
    else:
        slice_sprite_sheet(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
