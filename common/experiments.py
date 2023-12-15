import asyncio
import os

import tensorflow as tf


def deep_dream(image_path, output_path):
    # Load the image
    img = tf.keras.preprocessing.image.load_img(image_path)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.keras.applications.inception_v3.preprocess_input(img_array)

    # Resize the image to match InceptionV3 input size
    img_array_resized = tf.image.resize(img_array, (299, 299))
    img_array_resized = tf.expand_dims(img_array_resized, axis=0)

    # Load the InceptionV3 model
    base_model = tf.keras.applications.InceptionV3(
        include_top=False,
        weights='/Users/peyman627/PycharmProjects/image_weaver/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'
    )

    # Choose a layer for feature visualization
    layer_name = 'mixed3'  # Adjust this based on the layers available in InceptionV3

    # Create a model that maps the input image to the chosen layer's activations
    dream_model = tf.keras.Model(inputs=base_model.input, outputs=base_model.get_layer(layer_name).output)

    # Define the loss function
    def calc_loss(img, model):
        img_batch = tf.keras.applications.inception_v3.preprocess_input(img)  # Preprocess the input image
        layer_activations = model(img_batch)
        return tf.reduce_mean(layer_activations)

    # Use a TensorFlow GradientTape to calculate the gradients of the input image
    def deepdream(model, img, steps=100, step_size=0.01):
        for step in range(steps):
            with tf.GradientTape() as tape:
                tape.watch(img)
                loss = calc_loss(img, model)

            # Calculate the gradients of the loss with respect to the input image
            gradients = tape.gradient(loss, img)

            # Normalize the gradients
            gradients /= tf.math.reduce_std(gradients) + 1e-8

            # Update the input image with the normalized gradients
            img = img + gradients * step_size
            img = tf.clip_by_value(img, -1, 1)

        return img

    # Generate the deep dream image
    dream_img = deepdream(model=dream_model, img=img_array_resized)

    # Save the resulting image
    output_image_path = os.path.join(output_path, 'dream_result.jpg')
    tf.keras.preprocessing.image.save_img(output_image_path, dream_img[0])


async def main():
    example_path = '/Users/peyman627/PycharmProjects/image_weaver/media/experiments/example.jpg'
    output_path = '/Users/peyman627/PycharmProjects/image_weaver/media/experiments/'

    await asyncio.to_thread(deep_dream, example_path, output_path)


if __name__ == '__main__':
    asyncio.run(main())
