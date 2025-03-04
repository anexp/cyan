# nvidia-container-toolkit

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html


#### Configuring Docker

Configure the container runtime by using the nvidia-ctk command:
```sh
sudo nvidia-ctk runtime configure --runtime=docker
```
The nvidia-ctk command modifies the /etc/docker/daemon.json file on the host. The file is updated so that Docker can use the NVIDIA Container Runtime.

Restart the Docker daemon:
```sh
sudo systemctl restart docker
```

#### Configuring containerd

Configure the container runtime by using the nvidia-ctk command:
```sh
sudo nvidia-ctk runtime configure --runtime=containerd
```
The nvidia-ctk command modifies the /etc/containerd/config.toml file on the host. The file is updated so that containerd can use the NVIDIA Container Runtime.

Restart containerd:
```sh
sudo systemctl restart containerd
```

#### Configuring CRI-O

Configure the container runtime by using the nvidia-ctk command:
```sh
sudo nvidia-ctk runtime configure --runtime=crio
```
The nvidia-ctk command modifies the /etc/crio/crio.conf file on the host. The file is updated so that CRI-O can use the NVIDIA Container Runtime.

Restart the CRI-O daemon:
```sh
sudo systemctl restart crio
```


#### Generating a CDI specification


Two typical locations for CDI specifications are /etc/cdi/ and /var/run/cdi. However, the path to create and use can depend on the container engine that you use.

Generate the CDI specification file:
```sh
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
The sample command uses sudo to ensure that the file at /etc/cdi/nvidia.yaml is created. You can omit the --output argument to print the generated specification to STDOUT.

Example Output
```
INFO[0000] Auto-detected mode as "nvml"
INFO[0000] Selecting /dev/nvidia0 as /dev/nvidia0
INFO[0000] Selecting /dev/dri/card1 as /dev/dri/card1
INFO[0000] Selecting /dev/dri/renderD128 as /dev/dri/renderD128
INFO[0000] Using driver version xxx.xxx.xx
```
(Optional) Check the names of the generated devices:
```sh
nvidia-ctk cdi list
```
The following example output is for a machine with a single GPU that does not support MIG.
```
INFO[0000] Found 9 CDI devices
nvidia.com/gpu=all
nvidia.com/gpu=0
```

## Running workload 

podman

```sh
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi -L
```

```sh
podman run --rm \
    --device nvidia.com/gpu=0 \
    --device nvidia.com/gpu=1:0 \
    --security-opt=label=disable \
    ubuntu nvidia-smi -L
```


#### Using CDI with Non-CDI-Enabled Runtimes

To support runtimes that do not natively support CDI, you can configure the NVIDIA Container Runtime in a cdi mode. In this mode, the NVIDIA Container Runtime does not inject the NVIDIA Container Runtime Hook into the incoming OCI runtime specification. Instead, the runtime performs the injection of the requested CDI devices.

The NVIDIA Container Runtime automatically uses cdi mode if you request devices by their CDI device names.

Using Docker as an example of a non-CDI-enabled runtime, the following command uses CDI to inject the requested devices into the container:
```sh
docker run --rm -ti --runtime=nvidia \
    -e NVIDIA_VISIBLE_DEVICES=nvidia.com/gpu=all \
      ubuntu nvidia-smi -L
```
The NVIDIA_VISIBLE_DEVICES environment variable indicates which devices to inject into the container and is explicitly set to nvidia.com/gpu=all.

docker

```sh
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

#### Setting the CDI Mode Explicitly

You can force CDI mode by explicitly setting the nvidia-container-runtime.mode option in the NVIDIA Container Runtime config to cdi:
```sh
sudo nvidia-ctk config --in-place --set nvidia-container-runtime.mode=cdi
```
In this case, the NVIDIA_VISIBLE_DEVICES environment variable is still used to select the devices to inject into the container, but the nvidia-container-runtime.modes.cdi.default-kind (with a default value of nvidia.com/gpu) is used to construct a fully-qualified CDI device name only when you specify a device index such as all, 0, or 1, and so on.

This means that if CDI mode is explicitly enabled, the following sample command has the same effect as specifying NVIDIA_VISIBLE_DEVICES=nvidia.com/gpu=all.
```sh
docker run --rm -ti --runtime=nvidia \
    -e NVIDIA_VISIBLE_DEVICES=all \
      ubuntu nvidia-smi -L
```



### Testing podman 

Testing Podman and NVIDIA Container Runtime

https://hub.docker.com/r/nvidia/cuda/tags

use image 12.3.1-devel-ubuntu22.04            
base,devel,runtime are available

Test nvidia-smi with the latest official CUDA image

```sh
podman run --rm --gpus all docker.io/nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
```
        

Multiple GPUs

Test nvidia-smi with the latest official CUDA image on two GPUs
```sh
podman run --rm --gpus 2 docker.io/nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
```
        


