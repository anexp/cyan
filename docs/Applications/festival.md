# Festival

Install on Arch Linux
```
sudo pacman -S festival

# To get American Male/Female and Scottish English Male speaker
sudo pacman -S festival-us

# To get British and American English Male speaker.
# (No need to install this)
# This is an alternative if you have low space on your device
sudo pacman -S festival-english
```

Usage
```
echo "Hello, world" | festival --tts
xclip -o | festival --tts
```

#### To stop voice use

Killing a background festival process will not stop the audio from continuing to play.
To stop audio from playing, the child **audsp** processes must be killed. This can be done by executing:

```
pkill audsp
```


### Screen reader

The following commands can be used as keybindings

Command to start playing
```
bash -c "xclip -o | festival --tts"
```


Command to stop playing
```
bash -c "pkill audsp"
```


### Interactive mode

Festival has an interactive prompt you can use for testing. Type festival to enter it. The following are some examples:

To show the voice festival speaks with:
```
voice_default 
```
To list available voices:
```
(voice.list)
```
To select another voice, enter (voice_name). For example:
```
(voice_cmu_us_rms_cg)
```
To hear it speak:
```
(SayText "Arch makes me happy") 
```
To list available commands:
```
help
```
To exit the shell:
```
(quit)
```

#### Reference

[ArchWiki webpage](https://wiki.archlinux.org/title/Festival)
