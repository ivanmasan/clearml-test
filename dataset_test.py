from clearml import Dataset
from pathlib import Path
from time import time

t = time()
path = Dataset.get(dataset_id='d16b8d4a56074ed484d9c39babb0dc88').get_local_copy()
path = Path(path)
print(time() - t)

for item in path.iterdir():
  print(item)
