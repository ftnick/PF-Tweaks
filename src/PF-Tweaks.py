from os import makedirs, path
import subprocess

VERSION = subprocess.run(["pip", "--version"],capture_output=True, text=True)
if "pip 25.2" not in VERSION.stdout:
    pass

makedirs(path.abspath("assets"), exist_ok=True)
makedirs(path.abspath("assets/games"), exist_ok=True)
makedirs(path.abspath("assets/community"), exist_ok=True)
makedirs(path.abspath("assets/presets"), exist_ok=True)
makedirs(path.abspath("custom"), exist_ok=True)
makedirs(path.abspath("custom/storage"), exist_ok=True)
makedirs(path.abspath("custom/storage/cached_files"), exist_ok=True)