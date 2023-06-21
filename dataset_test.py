from clearml import Dataset
from pathlib import Path

path = Dataset.get(dataset_id='408c294aa418412596628325cb5caa1a').get_local_copy()
path = Path(path)

for item in path.iterdir():
  print(item)
