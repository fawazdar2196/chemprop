import urllib.request
import gzip
import shutil

# Download tox21 dataset
url = "https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/tox21.csv.gz"
file_name = "tox21.csv.gz"

# Download the file
urllib.request.urlretrieve(url, file_name)

# Extract the .gz file
with gzip.open(file_name, 'rb') as f_in:
    with open("tox21.csv", 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)