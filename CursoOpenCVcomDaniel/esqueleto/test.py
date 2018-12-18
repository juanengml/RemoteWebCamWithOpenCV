from skimage.morphology import skeletonize
ske = (skeletonize("01.jpg"//255) * 255).astype(np.uint8)
print ske
