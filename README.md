# Sprite Sheet Slicer

This Python script slices a sprite sheet into individual frames and saves them as separate image files. Each frame is named with leading zeros based on the total number of frames, and the frames are saved in a subdirectory named after the original file.

## Features

- Automatically slices a sprite sheet into individual frames.
- Names frames with leading zeros for better file organization.
- Saves frames in a subdirectory named after the original sprite sheet file.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Install the Pillow library if you haven't already:

    ```sh
    pip install Pillow
    ```

2. Download or clone this repository.

## Usage

1. Place your sprite sheet image file in the same directory as the script.

2. Run the script with the following command:

    ```sh
    python slice_sprite_sheet.py <file_path> <frames_horizontal> <frames_vertical>
    ```

    - `<file_path>`: Path to the sprite sheet image file.
    - `<frames_horizontal>`: Number of frames horizontally.
    - `<frames_vertical>`: Number of frames vertically.

### Example

To slice a sprite sheet named `down.png` into a 4x4 grid:

```sh
python slice_sprite_sheet.py down.png 4 4
