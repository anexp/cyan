# Fake Webcam

Ref :- 
1. [Fake WebCam Linux for devices](https://www.linuxfordevices.com/tutorials/linux/fake-webcam-streams)


Steps to create fake webcam streams on Linux

Let’s get started on the steps to create our fake webcam stream on Linux.
1. Install the important dependencies

First, we need to install two very important dependencies.

The first one is v4l2loopback which allows us to create “virtual video devices”, which we shall require to setup our fake webcam. To install it on Debian/Ubuntu, run :
```sh
sudo apt install v4l2loopback-dkms
```

Next up, we need ffmpeg which will enables us to stream the video we want as the Webcam feed which can be installed with :
```sh
sudo apt install ffmpeg
```

With this out of the may, we can move onto the next step.
2. Add Kernel Modules

Next up, we need to add the v4l2loopback kernel modules to emulate a virtual video device. This can be done with :
```sh
sudo modprobe v4l2loopback card_label="My Fake Webcam" exclusive_caps=1
```

Here, there are two extra parameters mentioned :

    card_label : Card labels for every device. Here we set our device name to “My Fake Webcam”
    exclusive_caps : Determine whether to announce OUTPUT/CAPTURE capabilities exclusively or not. Here setting it to the value 1 will enable it and is often required to fix Chrome/WebRTC issues.

Once we have our kernel modules loaded, we can now run our main program.
3. Link Video Stream To Fake Webcam

First, we need to list all video devices available to us with :
```sh
ls -1 /dev/video*
```
```
/dev/video0
/dev/video1
/dev/video2
```

Next up we need to check which of these video devices is functioning. This can be done with :
```sh
ffplay /dev/videoX
```

Here, X represents the device number from the previous output. For instance, according to the given example, X can have the values 0, 1 or 2. For the correct functioning device, it should spawn a window with your webcam on, reflecting whatever it captures. Once you have confirmed the functioning device, note the device number and proceed to the next step.

Next up, we need to “fake” our webcam feed with :
```sh
ffmpeg -stream_loop -1 -re -i /path/to/video -vcodec rawvideo -threads 0 -f v4l2 /dev/videoX
```

Let’s break the command into pieces :

    ffmpeg : The program which would enable us to stream our video as the webcam feed
    -stream_loop -1 : This dictates how many times the video should be looped. Assigning it the negative value of -1 makes it loop infinitely so that it keeps on playing till we close our program.
    -re : This specifies the program to read input at native frame rate
    -i : Specifies the input file name. It is followed by the path to the video file we want to stream
    -vcodec : This specifies the video codec, aka the stream handling.
    rawvideo : This tell ffmpeg to use the Raw video demuxer. This demuxer allows one to read raw video data.
    -threads : The number of threads to be used. Usually setting it to 0 is considered be optimal.
    -f : This flag is used force the format of input/output file. In our case, we are forcing output to v4l2 format
    /dev/videoX : It specifies the functioning video devices as defined above.

Once you execute this command, it should start the fake stream. However, you may need to turn your video off and back again for the fake stream to start up. You can also automate the entire process by writing a script like this one.
Fake Stream Rick Astley's Never Gonna Give You On Google MeetFake Stream Rick Astley’s Never Gonna Give You On Google Meet
4. Remove the fake webcam streams

Once you are done with the fake stream, remove the previously loaded kernel modules with :
```sh
sudo modprobe --remove v4l2loopback
```

This should disable the fake webcam.
Conclusion

Thus we saw how we can create a fake webcam and play any video on loop. This can come especially handy during video calls and is quite a handy trick to have up your sleeve.
