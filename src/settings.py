from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
OPERATION_PATH = Path.joinpath(ROOT_PATH, 'data', 'data_1.json')

print(ROOT_PATH)