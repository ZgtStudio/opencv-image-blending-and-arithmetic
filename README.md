# OpenCV Image Blending and Arithmetic

This repository contains my third set of computer vision exercises under **Zgt Studio**.  
The goal is to explore **image blending** and **basic arithmetic operations** in OpenCV, including:  
simple addition, weighted addition, overlay effects and grayscale conversion.

---

## 1. Exercises

### 1.1 Weighted Image Addition

Folder: `OpenCV Weighted Image Addition/`

This example demonstrates weighted addition of two images using  
`cv2.addWeighted`.

**Script:**

- `weighted_addition.py`
  - reads two images (e.g., `Bison.jpg` and `Falcon.jpg`),
  - checks whether files are loaded correctly,
  - displays both original images,
  - blends them with weighted addition,
  - shows the result.

**Data:**

- `Bison.jpg` – sample image  
- `Falcon.jpg` – sample image

---

### 1.2 Image Overlay (Simple vs Weighted)

Folder: `OpenCV Image Blending Overlay/`

This example compares two different approaches:  
pixel-wise addition with `cv2.add` and weighted blending with `cv2.addWeighted`.

**Script:**

- `image_blending_overlay.py`
  - reads two images (e.g., `Horse.jpg` and `Swan.jpg`),
  - applies simple overlay with `cv2.add`,
  - applies weighted overlay with `cv2.addWeighted`,
  - displays both results for comparison.

**Data:**

- `Horse.jpg` – sample image  
- `Swan.jpg` – sample image

---

### 1.3 Grayscale and Arithmetic Operations

Folder: `OpenCV Grayscale and Arithmetic Operations/`

This example introduces grayscale conversion and basic arithmetic operations  
used frequently in preprocessing workflows.

**Script:**

- `grayscale_and_arithmetic.py`
  - reads a sample image,
  - converts the image to grayscale using `cv2.cvtColor`,
  - demonstrates basic arithmetic operations (e.g., add/subtract),
  - displays results.

**Data:**

- `<your_sample_image>.jpg` – sample image used for grayscale + arithmetic examples

---

## 2. Project structure

```text
opencv-image-blending-and-arithmetic/
├─ OpenCV Weighted Image Addition/
│  ├─ Bison.jpg
│  ├─ Falcon.jpg
│  └─ weighted_addition.py
├─ OpenCV Image Blending Overlay/
│  ├─ Horse.jpg
│  ├─ Swan.jpg
│  └─ image_blending_overlay.py
├─ OpenCV Grayscale and Arithmetic Operations/
│  ├─ <your_sample_image>.jpg
│  └─ grayscale_and_arithmetic.py
└─ README.md
