# Audacity


To convert a .webm audio file to a format recognized by Audacity using FFmpeg, you can use the following command in your command prompt or terminal:

css
```
ffmpeg -i input.webm -vn -acodec pcm_s16le -ar 44100 -ac 2 output.wav
```
Here's what each parameter does:

    -i input.webm: Specifies the input file to be converted, in this case, "input.webm".
    -vn: Disables video processing, as we only want to convert the audio.
    -acodec pcm_s16le: Specifies the audio codec to be used for the output file. In this case, we're using PCM signed 16-bit little-endian audio, which is supported by Audacity.
    -ar 44100: Sets the audio sample rate to 44.1kHz, which is the standard CD-quality audio sample rate.
    -ac 2: Sets the audio channels to stereo.

Finally, we specify the output file name as "output.wav". You can change this to any filename you like, as long as it has a supported audio file extension (e.g. .wav, .mp3, .flac, etc.) that Audacity can recognize.

Once the conversion is complete, you should be able to open the output file in Audacity without any issues.
