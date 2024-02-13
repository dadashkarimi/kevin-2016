for import nibabel as nib
import numpy as np

def convert_mgz_to_nii(input_path, output_path):
    img = nib.load(input_path)
    data = img.get_data()
    #expanded_data = np.expand_dims(data, axis=-1)  # Expand the last dimension with size 1
    #new_img = nib.Nifti1Image(expanded_data, img.affine)
    nib.save(img, output_path)

def convert_all_mgz_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".mgz"):
                mgz_path = os.path.join(root, file)

                # Get the relative path from input_folder to the mgz file
                relative_path = os.path.relpath(root, input_folder)

                # Extract parent folder names
                parent_folders = os.path.normpath(relative_path).split(os.path.sep)
                parent_folders = [folder for folder in parent_folders if folder]  # Remove empty elements

                # Construct the output filename with parent folder names and extension only
                output_file = "_".join(parent_folders[-2:]) + ".nii.gz"
                output_path = os.path.join(output_folder, output_file)
                convert_mgz_to_nii(mgz_path, output_path)

if __name__ == "__main__":
    #input_folder = "mgh_70"
    #output_folder = "MGH2"

    convert_all_mgz_in_folder(input_folder, output_folder)
