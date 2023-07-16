# image-frier
A quick script to transform regular photos into oversaturated, oversharpened abstract images.

## prerequisites

The most recent version (as of this authoring) requires Python 3.10, so install that first.  
Next, install pillow via pip:

```
pip install Pillow
```

## installation

At this point, you can clone the repo and run frier.py directly.
The source image should be supplied as the first argument to the script:

```
git clone https://github.com/peacebaker/image-frier.git
python frier source.jpg

```

By default, the image (and all its iterations) will be saved to a subfolder of the current working directory named 
'felt cute'.  This location can be changed by altering the "NAME" constant in the script:

```
NAME = 'felt cute'
```