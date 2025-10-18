from PIL import Image
import os


def convert_images(input_folder, output_folder, target_width, target_format):
    img_formats = ('.png', '.jpg', '.jpeg', '.gif', '.webp')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_list = os.listdir(input_folder)
    print('file_list:', file_list)
    img_files = [file for file in file_list if file.endswith(img_formats)]
    print('img_files:', img_files)

    for file in img_files:
        file_path = os.path.join(input_folder, file)
        print('file_path', file_path)

        with Image.open(file_path) as img:
            image_name, _ = os.path.splitext(file)
            print('image_name', image_name)

            new_image_name = f'{image_name}.{target_format.lower()}'
            output_path = os.path.join(output_folder, new_image_name)

            aspect_ratio = img.width / img.height
            height = int(target_width / aspect_ratio)
            image_formatted = img.resize((target_width, height))
            image_formatted.save(output_path, target_format, quality=80)

if __name__ == '__main__':
    convert_images('./images', './images/converted', 980, 'webp')
