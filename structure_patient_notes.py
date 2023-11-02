import os

# Global Vars
cache_dir = "cache/"
vector_db_path = "vector_db/"
data_path = "data/"

collection_name = "ih_docs"

embedding_model = "BAAI/bge-base-en-v1.5"
generative_model = "HuggingFaceH4/zephyr-7b-beta"

paths = [cache_dir, vector_db_path, data_path]
for path in paths:
    os.makedirs(path, exist_ok=True)

os.environ["TRANSFORMERS_CACHE"] = cache_dir


# PUT CODE HERE

from datasets import load_dataset

dataset = load_dataset("medical_dialog", "en")












# END CODE


import os

def remove_directory(path):
    if os.path.exists(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.remove(file_path)
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.rmdir(dir_path)
        os.rmdir(path)

for path in paths:
    remove_directory(path)