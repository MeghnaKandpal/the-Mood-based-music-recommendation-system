from flask import Flask, request, redirect, render_template
from emotion_detection import detect_emotion_from_face
from music_recommendation import recommend_songs, create_playlist_with_songs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    emotion = detect_emotion_from_face()  
    recommended_songs = recommend_songs(emotion)  
    playlist_link = create_playlist_with_songs(emotion, recommended_songs)  
    return redirect(playlist_link)

@app.route('/recommend_text', methods=['POST'])
def recommend_text():
    emotion = request.form.get("emotion").lower() 
    recommended_songs = recommend_songs(emotion)
    playlist_link = create_playlist_with_songs(emotion, recommended_songs)
    return redirect(playlist_link)

if __name__ == "__main__":
    app.run(debug=True)
