import imgaug.augmenters as iaa

augmentations = iaa.Sequential([
    iaa.Resize(
        {"shorter-side": (320, 960), "longer-side": "keep-aspect-ratio"},
        interpolation="linear"
    ),
    iaa.Fliplr(0.5),
    iaa.Flipud(0.5),
    iaa.Sometimes(0.5, iaa.Rot90(keep_size=False)),
    iaa.Sometimes(0.25, iaa.GaussianBlur(sigma=(0.0, 1.0))),
    iaa.Sometimes(0.25, iaa.AverageBlur(k=(1, 5))),
    iaa.Sometimes(0.25, iaa.MedianBlur(k=(1, 5))),

    iaa.Sometimes(0.33, iaa.LinearContrast((0.5, 1.5))),
    iaa.Sometimes(0.33, iaa.Multiply((0.5, 1.5))),

    iaa.Sometimes(0.25, iaa.Affine(
        scale=(0.8, 1.25))),

    iaa.Sometimes(0.5, iaa.Affine(
        scale={"x": (0.9, 1.1), "y": (0.9, 1.1)},
        rotate=(0, 30))),

    iaa.CropToFixedSize(width=1024, height=1024)
])
