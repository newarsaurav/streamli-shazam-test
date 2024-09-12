import streamlit as st
import os

# Define the HTML/JS for the audio recorder
recorder_html = """
<script>
  let mediaRecorder;
  let audioChunks = [];

  function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();

        mediaRecorder.addEventListener("dataavailable", event => {
          audioChunks.push(event.data);
        });

        mediaRecorder.addEventListener("stop", () => {
          const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' });
          const audioUrl = URL.createObjectURL(audioBlob);
          const audio = new Audio(audioUrl);
          const downloadLink = document.createElement('a');
          downloadLink.href = audioUrl;
          downloadLink.download = 'recording.mp3';
          downloadLink.click();
          audioChunks = [];
        });
      });
  }

  function stopRecording() {
    mediaRecorder.stop();
  }
</script>

<button onclick="startRecording()">Start Recording</button>
<button onclick="stopRecording()">Stop Recording</button>
"""

# Embed the HTML/JS in Streamlit
st.components.v1.html(recorder_html, height=300)

st.write("Use the buttons above to start and stop recording audio.")
