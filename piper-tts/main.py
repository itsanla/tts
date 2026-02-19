from piper import PiperVoice
import sounddevice as sd

voice = PiperVoice.load("id_ID-news_tts-medium.onnx")
audio = voice.synthesize("Halo, ini suara AI yang sangat natural dalam Bahasa Indonesia. Gimana kabar kamu hari ini?")
sd.play(audio, samplerate=voice.sample_rate)
sd.wait()