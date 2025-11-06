# Turkish Flag and Olympic Rings Drawing

A Python visualization project that draws the Turkish Flag and Olympic Rings using Pygame, without relying on the turtle library.

## Features

- **Turkish Flag**: Accurate representation of the Turkish flag with proper proportions, including the crescent and star
- **Olympic Rings**: The five interlocking Olympic rings in their official colors

## Requirements

```
pygame
numpy
matplotlib
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Turkish-Flag-and-Olympic-Rings-Drawing.git
cd Turkish-Flag-and-Olympic-Rings-Drawing
```

2. Install the required dependencies:
```bash
pip install pygame numpy matplotlib
```

## Usage

### To display the Olympic Rings:
```bash
python olympicrings.py
```

### To display the Turkish Flag:
```bash
python turk_bayragi.py
```

Close the window or press the close button to exit the program.

## Screenshots

### Olympic Rings

![olimpiyathalkalari](https://user-images.githubusercontent.com/86886469/229761614-ccba1467-6d10-46b0-bf72-6bd15a91348d.png)

The five interlocking rings represent the five continents and are displayed in their official Olympic colors: blue, yellow, black, green, and red.

### Turkish Flag

![türkbayrağı](https://user-images.githubusercontent.com/86886469/229761691-a6352304-30ea-4d32-b18c-60a79ad05f79.png)

The Turkish flag features a white crescent moon and star on a red background, rendered with proper geometric proportions.

## Technical Details

- Built with Pygame for graphics rendering
- Uses mathematical calculations for accurate positioning
- Window size: 600x600 pixels (Turkish Flag), 600x500 pixels (Olympic Rings)
- All shapes are drawn using Pygame's circle and polygon primitives
