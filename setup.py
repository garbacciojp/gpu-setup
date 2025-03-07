import os
import time
import subprocess

# List of model URLs (CIVIAI / HuggingFace models.)
model_urls = [
    "XX",
    "XX",
    "XX"
]

# API token for PLATFORM downloads from CIVIAI.
api_token = "API-KEY"

# Download path for Stable Diffusion models (PLATFORM)
download_path = "/workspace/stable-diffusion-webui/models/Stable-diffusion"
os.makedirs(download_path, exist_ok=True)

# Download each CIVIAI / HuggingFace models.
for url in model_urls:
    full_url = f"{url}?token={api_token}"
    command = ["wget", "--content-disposition", "-P", download_path, full_url]
    print(f"Downloading model: {full_url}")
    subprocess.run(command)
    # Sleep to prevent overloading the server
    time.sleep(2)

print("PLATFORM models download complete!")

# Download VAE from Hugging Face
vae_url = "https://huggingface.co/stabilityai/sdxl-vae/resolve/main/sdxl_vae.safetensors?download=true"
vae_download_path = "/workspace/stable-diffusion-webui/models/VAE"
os.makedirs(vae_download_path, exist_ok=True)

vae_command = ["wget", "--content-disposition", "-P", vae_download_path, vae_url]
print(f"Downloading VAE: {vae_url}")
subprocess.run(vae_command)

print("VAE download complete!")
