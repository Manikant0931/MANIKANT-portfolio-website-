from pathlib import Path

from PIL import Image


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEXTURE_PATHS = (
    PROJECT_ROOT / 'static/textures/monitor/layers/compressed/smudges.jpg',
    PROJECT_ROOT / 'public/textures/monitor/layers/compressed/smudges.jpg',
)


for texture_path in TEXTURE_PATHS:
    if not texture_path.exists():
        continue

    with Image.open(texture_path) as source:
        clean_texture = Image.new('RGB', source.size, (0, 0, 0))
        clean_texture.save(texture_path, format='JPEG', quality=95, optimize=True)