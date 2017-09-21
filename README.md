# SoundControl
Sound Control From Terminal on Linux Systems

Good for use on raspberry pi

# Dependencies
pyalsaaudio

# Use on Raspberry Pi:
You might need to change the line `mixer = alsaaudio.Mixer()` to `mixer = alsaaudio.Mixer("PCM")`
