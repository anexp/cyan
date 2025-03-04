# NVIDIA

### Installation

On Debian

nvcc is in /usr/lib/nvidia-cuda-toolkit/bin/
nvidia-smi is in /usr/lib/nvidia/nvidia/

```sh
sudo apt install -y nvidia-driver
```

```sh
sudo apt install -y nvidia-cuda-dev nvidia-cuda-toolkit
```

or you could
```sh
sudo apt install "nvidia-cuda-*"
```

On Arch


```sh
sudo pacman -S nvidia-open
```

For custom kernels like linux-zen
```sh
sudo pacman -S nvidia-open-dkms
```


### Check

```sh
nvidia-smi --query-gpu=driver_version --format=csv
```
