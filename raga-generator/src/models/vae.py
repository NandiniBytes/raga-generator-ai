from tensorflow.keras import layers, models, backend as K
import numpy as np

class VAE:
    def __init__(self, input_shape, latent_dim):
        self.input_shape = input_shape
        self.latent_dim = latent_dim
        self.encoder, self.decoder, self.model = self.build_model()

    def build_model(self):
        # Encoder
        inputs = layers.Input(shape=self.input_shape)
        x = layers.Flatten()(inputs)
        x = layers.Dense(128, activation='relu')(x)
        x = layers.Dense(64, activation='relu')(x)
        z_mean = layers.Dense(self.latent_dim)(x)
        z_log_var = layers.Dense(self.latent_dim)(x)

        # Sampling function
        def sampling(args):
            z_mean, z_log_var = args
            epsilon = layers.K.random_normal(shape=(layers.K.shape(z_mean)[0], self.latent_dim))
            return z_mean + layers.K.exp(0.5 * z_log_var) * epsilon

        z = layers.Lambda(sampling)([z_mean, z_log_var])
        encoder = models.Model(inputs, [z_mean, z_log_var, z], name='encoder')
        # Decoder
        latent_inputs = layers.Input(shape=(self.latent_dim,))
        x = layers.Dense(64, activation='relu')(latent_inputs)
        x = layers.Dense(128, activation='relu')(x)
        x = layers.Dense(np.prod(self.input_shape), activation='sigmoid')(x)
        outputs = layers.Reshape(self.input_shape)(x)

      
        decoder = models.Model(latent_inputs, outputs, name='decoder')

        

        # VAE
        outputs = decoder(encoder(inputs)[2])
        vae = models.Model(inputs, outputs, name='vae')

        # Loss
        reconstruction_loss = layers.K.sum(layers.K.binary_crossentropy(inputs, outputs), axis=(1, 2))
        kl_loss = -0.5 * layers.K.sum(1 + z_log_var - layers.K.square(z_mean) - layers.K.exp(z_log_var), axis=1)
        vae_loss = layers.K.mean(reconstruction_loss + kl_loss)
        vae.add_loss(vae_loss)
        vae.compile(optimizer='adam')

        return encoder, decoder, vae

    def compile(self):
        reconstruction_loss = layers.K.binary_crossentropy(layers.K.flatten(self.inputs), layers.K.flatten(self.outputs))
        kl_loss = -0.5 * layers.K.sum(1 + self.z_log_var - layers.K.square(self.z_mean) - layers.K.exp(self.z_log_var), axis=-1)
        vae_loss = layers.K.mean(reconstruction_loss + kl_loss)
        self.model.add_loss(vae_loss)

    def train(self, data, epochs=50, batch_size=32):
        self.model.fit(data, data, epochs=epochs, batch_size=batch_size)

    def generate(self, num_samples):
        z_sample = np.random.normal(size=(num_samples, self.latent_dim))
        return self.decoder.predict(z_sample)
