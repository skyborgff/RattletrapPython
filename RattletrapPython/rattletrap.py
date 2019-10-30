from pathlib import Path
import subprocess

rattletrap_path = Path(__file__).absolute().parent / 'rattletrap.exe'

def parse(replay: str, json: Path):
    process = subprocess.call([rattletrap_path, '-i', replay, '-o', str(json)])
    process.wait()

def generate(json: str, replay: Path):
    process = subprocess.call([rattletrap_path, '-i', json, '-o', str(replay)])
    process.wait()
