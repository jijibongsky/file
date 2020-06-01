from pydub import AudioSegment

def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

sound = AudioSegment.from_file("../data/T0055G0002S0006.wav")
# print(1111111, sound.raw_data)
# print(1111111, sound.frame_rate)
# slow_sound = speed_change(sound, 0.9)
# fast_sound = speed_change(sound, 1.1)
# slow_sound.export("../data/ceshi_slow.wav", format='wav')
# fast_sound.export("../data/ceshi_fast.wav", format='wav')

# sound = AudioSegment.from_file("../data/T0055G0002S0006.wav")
# frame_rate = sound.frame_rate
# channel_count = sound.channels
# sample_width = sound.sample_width
# print(11111, frame_rate)
# print(22222, channel_count)
# print(33333, sample_width)
