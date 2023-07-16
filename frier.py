import random
import os
import sys
from pathlib import Path

from PIL import Image, ImageEnhance

# art has names, right?
NAME = 'felt cute'

# do androids dream of refried memes?
# or do their nightmares drift 
# through seas of digital decay?
NIGHTmARES = 100
JpGqUALITY = 6
WEBpQuALITY = 66

# scaling factors
SATURATIONfACTOR = 1.6
SHARPNESSfACTOR = 1.2
CONTRASTfACTOR = 1.3

# find the supplied image name and current working directory
IMAGE = sys.argv[1]
CwD = Path.cwd()
OUTPUT = os.path.join(CwD, NAME)

def saturate(image):
    """Increase image saturation, per the predefined factor."""

    # convert image to hsl values
    hsl = image.convert("HSV")
    h, s, l = hsl.split()

    # adjust the saturation channel
    enhancer = ImageEnhance.Color(s)
    s = enhancer.enhance(SATURATIONfACTOR)

    # merge and convert back to RGB colorspace
    saturated = Image.merge("HSV", (h, s, l))
    return saturated.convert('RGB')

def sharpen(image):
    """Increase the image sharpness, per predefined factor."""
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(SHARPNESSfACTOR)
    return image

def contrast(image):
    """Increase image contrast, per predefined factor."""
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(CONTRASTfACTOR)
    return image

def save_jpg(image, n):
    """Save image as a jpeg."""
    output = os.path.join(OUTPUT, f"round{n}.jpg")
    image.save(output, "JPEG", quality=JpGqUALITY)
    return output

def save_webp(image, n):
    """Save image as webp."""
    output = os.path.join(OUTPUT, f"round{n}.webp")
    image.save(output, "WEBP", quality=WEBpQuALITY)
    return output

def save_gif(image, n):
    """Save image as gif."""
    output = os.path.join(OUTPUT, f"round{n}.gif")
    image.save(output, "GIF")
    return output

save = {
    0: save_jpg,
    1: save_webp,
    2: save_gif,
}

def main():

    # open the original image
    try:
        image = Image.open(f"{CwD}/{IMAGE}")
    except FileNotFoundError:
        print("error: original image not found.")
    except Image.UnidentifiedImageError:
        print("error: invalid or unsupported image format for original image.")

    # make the output dir or die trying; no overwrites
    os.mkdir(OUTPUT)

    # like 30 years of digital rot in a few moments
    for n in range(NIGHTmARES):

        # oversharpen, oversaturate, and overcontrast the image
        image = sharpen(image)
        image = saturate(image)
        image = contrast(image)

        # save the file, randomly swapping formats to degrade quality
        roll = random.randint(0, 2)
        output = save[roll](image, n)

        # close the original image and open the new one
        image.close()
        try:
            print(f"opening {output}...")
            image = Image.open(output)
            image = image.convert('RGB')
        except FileNotFoundError:
            print(f"error: could not find {output}.")
        except Image.UnidentifiedImageError:
            print(f"error: invalid or unsupported image format while processing {output}.")

    # let us know when its done
    print(f"Deep fry complete.  Images saved to {OUTPUT}")


if __name__ == "__main__":
    main()