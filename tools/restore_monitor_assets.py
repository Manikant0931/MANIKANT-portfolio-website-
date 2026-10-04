from pathlib import Path

import numpy as np
from PIL import Image


PROJECT_ROOT = Path(__file__).resolve().parents[1]
COMPUTER_TEXTURES = (
    PROJECT_ROOT / 'static/models/Computer/baked_computer.jpg',
    PROJECT_ROOT / 'public/models/Computer/baked_computer.jpg',
)
SMUDGE_TEXTURES = (
    PROJECT_ROOT / 'static/textures/monitor/layers/compressed/smudges.jpg',
    PROJECT_ROOT / 'public/textures/monitor/layers/compressed/smudges.jpg',
)
CORRUPTED_LABEL = (1425, 2450, 2500, 3250)


def restore_label(texture_path: Path) -> None:
    with Image.open(texture_path) as source:
        image = np.asarray(source.convert('RGB'), dtype=np.float32).copy()

    left, top, right, bottom = CORRUPTED_LABEL
    left_edge = image[top:bottom, left - 1]
    image[top:bottom, left:right] = left_edge[:, None, :]

    Image.fromarray(np.clip(image, 0, 255).astype(np.uint8)).save(
        texture_path, quality=95, optimize=True
    )


def restore_smudges(texture_path: Path) -> None:
    source_path = texture_path.parents[1] / 'png/smudges.png'
    if not source_path.exists():
        return
    with Image.open(source_path) as source:
        source.convert('RGB').save(texture_path, quality=95, optimize=True)


for path in COMPUTER_TEXTURES:
    if path.exists():
        restore_label(path)

for path in SMUDGE_TEXTURES:
    if path.exists():
        restore_smudges(path)