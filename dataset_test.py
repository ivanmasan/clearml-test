from clearml import Dataset
from pathlib import Path

path = Dataset.get(dataset_id='02804c028b4a493e92649d4ea9e4cbda').get_local_copy()
path = Path(path)

for item in path.iterdir():
  print(item)
