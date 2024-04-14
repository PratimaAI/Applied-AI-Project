from seamless_communication import SeamlessM4T

# Load the SeamlessM4T model
model = SeamlessM4T.from_pretrained("facebook/seamless-m4t-medium")

# Transcribe speech from English to French
audio_file = "test_1.wav"
output_text = model.transcribe(audio_file, source_lang="en", target_lang="fr")

