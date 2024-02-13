import os
import nibabel as nib
import numpy as np
from skimage.transform import resize


def crop_and_resize(input_folder, output_folder, target_size=(288, 288)):
    max_depth = 79  # Maximum depth

    for file in os.listdir(input_folder):
        if file.endswith('.nii.gz'):
            img = nib.load(os.path.join(input_folder, file))
            print("Data type of the loaded image data:", img.shape)
            data = img.get_data()
            cropped_slices = []

            # Check if cropping or padding is needed
            if data.shape[0] < target_size[0] or data.shape[1] < target_size[1]:
                pad_x = max(0, (target_size[0] - data.shape[0]) // 2)
                pad_y = max(0, (target_size[1] - data.shape[1]) // 2)
                pad_width = (
                    (pad_x, target_size[0] - data.shape[0] - pad_x),
                    (pad_y, target_size[1] - data.shape[1] - pad_y),
                    (0, max_depth - data.shape[2])  # Pad the third dimension up to 79
                )
                padded_data = np.pad(data, pad_width, mode='constant', constant_values=0)
                resized_slices = []
                for depth_slice in range(padded_data.shape[2]):
                    slice_2d = padded_data[:, :, depth_slice]
                    resized_slice = resize(slice_2d, target_size, anti_aliasing=True)
                    normalized_slice = (resized_slice - np.min(resized_slice)) / (np.max(resized_slice) - np.min(resized_slice))
                    resized_slices.append(normalized_slice)
                cropped_image = np.stack(resized_slices, axis=-1)
            else:
                crop_x = (data.shape[0] - target_size[0]) // 2
                crop_y = (data.shape[1] - target_size[1]) // 2
                cropped_image = data[crop_x:crop_x + target_size[0], crop_y:crop_y + target_size[1], :min(target_size[0], data.shape[2])]

                # Pad the third dimension up to 79
                if cropped_image.shape[2] < max_depth:
                    pad_depth = max_depth - cropped_image.shape[2]
                    pad_width = ((0, 0), (0, 0), (0, pad_depth))
                    cropped_image = np.pad(cropped_image, pad_width, mode='constant', constant_values=0)

            # Expand last dimension by 1 just before saving
            cropped_image = np.expand_dims(cropped_image, axis=-1) if cropped_image.shape[2] == max_depth else cropped_image

            print("Processed image shape:", cropped_image.shape)

            nib.save(nib.Nifti1Image(cropped_image, img.affine), os.path.join(output_folder, file))


def crop_and_resize6(input_folder, output_folder, target_size=(288, 288)):
    max_depth = 79  # Maximum depth

    for file in os.listdir(input_folder):
        if file.endswith('.nii.gz'):
            img = nib.load(os.path.join(input_folder, file))
            print("Data type of the loaded image data:", img.shape)
            data = img.get_data()
            cropped_slices = []

            # Check if cropping or padding is needed
            if data.shape[0] < target_size[0] or data.shape[1] < target_size[1]:
                pad_x = max(0, (target_size[0] - data.shape[0]) // 2)
                pad_y = max(0, (target_size[1] - data.shape[1]) // 2)
                pad_width = (
                    (pad_x, target_size[0] - data.shape[0] - pad_x),
                    (pad_y, target_size[1] - data.shape[1] - pad_y),
                    (0, max_depth - data.shape[2])  # Pad the third dimension up to 79
                )
                padded_data = np.pad(data, pad_width, mode='constant', constant_values=0)
                resized_slices = []
                for depth_slice in range(padded_data.shape[2]):
                    slice_2d = padded_data[:, :, depth_slice]
                    resized_slice = resize(slice_2d, target_size, anti_aliasing=True)
                    normalized_slice = (resized_slice - np.min(resized_slice)) / (np.max(resized_slice) - np.min(resized_slice))
                    resized_slices.append(normalized_slice)
                cropped_image = np.stack(resized_slices, axis=-1)
            else:
                crop_x = (data.shape[0] - target_size[0]) // 2
                crop_y = (data.shape[1] - target_size[1]) // 2
                cropped_image = data[crop_x:crop_x + target_size[0], crop_y:crop_y + target_size[1], :min(target_size[0], data.shape[2])]

                # Pad the third dimension up to 79
                if cropped_image.shape[2] < max_depth:
                    pad_depth = max_depth - cropped_image.shape[2]
                    pad_width = ((0, 0), (0, 0), (0, pad_depth))
                    cropped_image = np.pad(cropped_image, pad_width, mode='constant', constant_values=0)
                
                # Expand last dimension by 1
                cropped_image = np.expand_dims(cropped_image, axis=-1)

            print("Processed image shape:", cropped_image.shape)
            
            nib.save(nib.Nifti1Image(cropped_image, img.affine), os.path.join(output_folder, file))

def crop_and_resize4(input_folder, output_folder, target_size=(288, 288)):
    max_depth = 79  # Maximum depth

    for file in os.listdir(input_folder):
        if file.endswith('.nii.gz'):
            img = nib.load(os.path.join(input_folder, file))
            print("Data type of the loaded image data:", img.shape)
            data = img.get_data()
            cropped_slices = []

            # Check if cropping or padding is needed
            if data.shape[0] < target_size[0] or data.shape[1] < target_size[1]:
                pad_x = max(0, (target_size[0] - data.shape[0]) // 2)
                pad_y = max(0, (target_size[1] - data.shape[1]) // 2)
                pad_width = (
                    (pad_x, target_size[0] - data.shape[0] - pad_x),
                    (pad_y, target_size[1] - data.shape[1] - pad_y),
                    (0, max_depth - data.shape[2])  # Pad the third dimension up to 79
                )
                padded_data = np.pad(data, pad_width, mode='constant', constant_values=0)
                resized_slices = []
                for depth_slice in range(padded_data.shape[2]):
                    slice_2d = padded_data[:, :, depth_slice]
                    resized_slice = resize(slice_2d, target_size, anti_aliasing=True)
                    normalized_slice = (resized_slice - np.min(resized_slice)) / (np.max(resized_slice) - np.min(resized_slice))
                    resized_slices.append(normalized_slice)
                cropped_image = np.stack(resized_slices, axis=-1)
            else:
                crop_x = (data.shape[0] - target_size[0]) // 2
                crop_y = (data.shape[1] - target_size[1]) // 2
                cropped_image = data[crop_x:crop_x + target_size[0], crop_y:crop_y + target_size[1], :min(target_size[0], data.shape[2])]

                # Pad the third dimension up to 79 and expand last dimension by 1
                if cropped_image.shape[2] < max_depth:
                    pad_depth = max_depth - cropped_image.shape[2]
                    pad_width = ((0, 0), (0, 0), (0, pad_depth))
                    cropped_image = np.pad(cropped_image, pad_width, mode='constant', constant_values=0)
                    cropped_image = np.expand_dims(cropped_image, axis=-1)

            print("Processed image shape:", cropped_image.shape)

            nib.save(nib.Nifti1Image(cropped_image, img.affine), os.path.join(output_folder, file))


def crop_and_resize3(input_folder, output_folder, target_size=(288, 288)):
    max_depth = 79  # Maximum depth

    for file in os.listdir(input_folder):
        if file.endswith('.nii.gz'):
            img = nib.load(os.path.join(input_folder, file))
            print("Data type of the loaded image data:", img.shape)
            data = img.get_data()
            cropped_slices = []

            # Check if cropping or padding is needed
            if data.shape[0] < target_size[0] or data.shape[1] < target_size[1]:
                pad_x = max(0, (target_size[0] - data.shape[0]) // 2)
                pad_y = max(0, (target_size[1] - data.shape[1]) // 2)
                pad_width = (
                    (pad_x, target_size[0] - data.shape[0] - pad_x),
                    (pad_y, target_size[1] - data.shape[1] - pad_y),
                    (0, max_depth - data.shape[2])  # Pad the third dimension up to 79
                )
                padded_data = np.pad(data, pad_width, mode='constant', constant_values=0)
                resized_slices = []
                for depth_slice in range(padded_data.shape[2]):
                    slice_2d = padded_data[:, :, depth_slice]
                    resized_slice = resize(slice_2d, target_size, anti_aliasing=True)
                    normalized_slice = (resized_slice - np.min(resized_slice)) / (np.max(resized_slice) - np.min(resized_slice))
                    resized_slices.append(normalized_slice)
                cropped_image = np.stack(resized_slices, axis=-1)
            else:
                crop_x = (data.shape[0] - target_size[0]) // 2
                crop_y = (data.shape[1] - target_size[1]) // 2
                cropped_image = data[crop_x:crop_x + target_size[0], crop_y:crop_y + target_size[1], :min(target_size[0], data.shape[2])]

                # Pad the third dimension up to 79
                if cropped_image.shape[2] < max_depth:
                    pad_depth = max_depth - cropped_image.shape[2]
                    pad_width = ((0, 0), (0, 0), (0, pad_depth))
                    cropped_image = np.pad(cropped_image, pad_width, mode='constant', constant_values=0)

            print("Processed image shape:", cropped_image.shape)
            
            nib.save(nib.Nifti1Image(cropped_image, img.affine), os.path.join(output_folder, file))



def crop_and_resize2(input_folder, output_folder, target_size=(288, 288)):
    for file in os.listdir(input_folder):
        if file.endswith('.nii.gz'):
            img = nib.load(os.path.join(input_folder, file))
            print(img.shape)
            data = img.get_data()
            cropped_slices = []
            
            crop_x = (data.shape[0] - target_size[0]) // 2
            crop_y = (data.shape[1] - target_size[1]) // 2
            
            for depth_slice in range(data.shape[2]):
                slice_2d = data[:, :, depth_slice]
                cropped_slice = slice_2d[crop_x:crop_x + target_size[0], crop_y:crop_y + target_size[1]]
                resized_slice = resize(cropped_slice, target_size, anti_aliasing=True)
                
                # Normalize pixel values to be between 0 and 1 for better visualization
                normalized_slice = (resized_slice - np.min(resized_slice)) / (np.max(resized_slice) - np.min(resized_slice))
                cropped_slices.append(normalized_slice)
            
            cropped_image = np.stack(cropped_slices, axis=-1)
            pad_width = ((0, 0), (0, 0), (0, 79 - cropped_image.shape[2]))

            cropped_image = np.pad(cropped_image, pad_width, mode='constant', constant_values=0)
            cropped_image = np.expand_dims(cropped_image,axis=-1)

            print(cropped_image.shape)
            nib.save(nib.Nifti1Image(cropped_image, img.affine), os.path.join(output_folder, file))

input_folder = "MGH2/"
output_folder = "data/"

crop_and_resize(input_folder, output_folder)
