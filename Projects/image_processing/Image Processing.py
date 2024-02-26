import os
import glob
import shutil
import pandas as pd
import numpy as np
import cv2
import matplotlib.pylab as plt

# Input directory
input_directory = r'C:\Users\Howar\Desktop\gitguud\Photo_processing\Input_image'

# Output directory
output_directory = r'C:\Users\Howar\Desktop\gitguud\Photo_processing\output_image'

# Create the image pattern
image_pattern = f'{input_directory}\\IMG_*.JPG'

# Use glob to get a list of file paths matching the pattern
image_paths = glob.glob(image_pattern)

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Process each image
    # image_paths[:1] for 1 picture processing
for image_path in image_paths[:1]:
    # Extract the file name from the path
    file_name = os.path.basename(image_path)

    # Create the output path
    output_path = os.path.join(output_directory, file_name)

    # Read the image using matplotlib
    img_mpl = plt.imread(image_path)
    img_cv2 = cv2.imread(image_path)
    # print(img_mpl)
    # print(img_cv2)
    # print(type(img_mpl))
    # print(type(img_cv2))
    # print(img_mpl.shape)
    # print(img_cv2.shape)
    # print(img_mpl.flatten())
    # print(img_cv2.flatten())
    # pd.Series(img_mpl.flatten()).plot(kind='hist', bins=50, title='Distribution of Pixel Values')


    # display image
    # fig, ax = plt.subplots(figsize=(10, 10))
    # ax.imshow(img_cv2_rgb)
    # ax.axis('off')


    # display RGB channels of imgage
    # fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    # axs[0].imshow(img_mpl[:, :, 0], cmap='Reds')
    # axs[1].imshow(img_mpl[:, :, 1], cmap='Greens')
    # axs[2].imshow(img_mpl[:, :, 2], cmap='Blues')
    # axs[0].axis('off')
    # axs[1].axis('off')
    # axs[2].axis('off')
    # axs[0].set_title('Red Channel')
    # axs[1].set_title('Green Channel')
    # axs[2].set_title('Blue Channel')





    # cv2 image handling
    # fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    # axs[0].imshow(img_cv2)
    # axs[1].imshow(img_mpl)
    # axs[0].axis('off')
    # axs[1].axis('off')
    # axs[0].set_title('CV2 Image')
    # axs[1].set_title('MPL Image')



    # **** image manipulation ****
    img = cv2.imread(image_path)


    # Converts cv2 to RGB
    img_cv2_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)

    # GreyScale
    # img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # fig, ax = plt.subplots(figsize=(20, 20))
    # ax.imshow(img_grey, cmap='grey')
    # ax.set_title('Grey Image')

    # Resize
    # print(img_cv2_rgb.shape)
    # img_resized = cv2.resize(img_cv2_rgb, (400, 260))
    # fig, axs = plt.subplots(1, 2, figsize=(20, 20))
    # axs[0].imshow(img_cv2_rgb)
    # axs[0].set_title('Original Image')
    # axs[1].imshow(img_resized, cmap='gray')
    # axs[1].set_title('Grey Image Resized')
    #
    # print(img_resized.shape)

    # Sharpen Image
    kernal_sharpening = np.array([[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]])

    sharpened = cv2.filter2D(img_cv2_rgb, -1, kernal_sharpening)



    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(sharpened)
    ax.axis('off')
    ax.set_title('Sharpened Image')


    plt.show()
    plt.pause(0.2)

    # Save the image to the output directory
    plt.imsave(output_path, sharpened)


    plt.close('all')

    cv2.destroyAllWindows()

print(f'Images copied to: {output_directory}')
