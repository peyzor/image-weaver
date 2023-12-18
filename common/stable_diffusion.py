import asyncio
import random
import string

import PIL.Image
import keras_cv
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


def generate_random_string(length=6):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits  # You can customize this if needed

    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string


def save(img):
    pil_img = PIL.Image.fromarray(np.array(img))
    name = generate_random_string()
    pil_img.save(
        f'/home/shaghayegh/image-weaver/media/experiments/{name}.jpg')


def plot_images(images):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        plt.subplot(1, len(images), i + 1)
        # plt.imshow(images[i])
        plt.axis("off")
        save(images[i])


async def generate_photo():
    model_path = '/home/shaghayegh/Downloads/kcv_diffusion_model.h5'
    tf.keras.mixed_precision.set_global_policy("mixed_float16")
    model = keras_cv.models.StableDiffusion(jit_compile=True)
    images = model.text_to_image("photograph of an astronaut riding a horse", batch_size=1)
    model.load_model(model_path)
    plot_images(images)


async def process_prompt(prompt):
    loop = asyncio.get_event_loop()
    images = await loop.run_in_executor(None, generate_photo, prompt)
    return images


if __name__ == '__main__':
    asyncio.run(generate_photo())
