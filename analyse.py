import os

base_dir = "train"

# Function to count the number of files in a directory
def count_files(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

for subdir in os.listdir(base_dir):
    base_subdir_path = os.path.join(base_dir, subdir)

    train_files = count_files(base_subdir_path)

    # Print the results
    print(f"Number of train files for {subdir}: {train_files}")
