import os

base_dir = "train"
compare_dir = "val"

# Function to count the number of files in a directory
def count_files(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

for subdir in os.listdir(base_dir):
    base_subdir_path = os.path.join(base_dir, subdir)
    compare_subdir_path = os.path.join(compare_dir, subdir)
   
    # Count the number of files in the train and test directories
    train_files = count_files(base_subdir_path)
    test_files = count_files(compare_subdir_path)

    # Calculate the total number of files
    total_files = train_files + test_files

    # Calculate the percentages
    train_percentage = (train_files / total_files) * 100
    test_percentage = (test_files / total_files) * 100

    # Print the results
    print(f"Percentage of train files for {subdir}: {train_percentage:.2f}%")
    print(f"Percentage of validation files for {subdir}: {test_percentage:.2f}%")
