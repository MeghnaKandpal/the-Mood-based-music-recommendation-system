# **Emotion-Based Music Recommendation System**

This project is an **Emotion-Based Music Recommendation System** that detects the user's mood based on text input or facial expressions and recommends music accordingly. The recommended songs are added to a playlist on Spotify that users can access and play directly.

---

## **Features**

- Detect emotion using:
  - Text-based sentiment analysis
  - Facial expression detection (using DeepFace)
- Recommend songs based on detected emotion
- Automatically create a Spotify playlist with recommended songs
- Redirect users to the playlist for easy access

---

## **Technologies Used**

### Backend:
- **Python**
- **Flask** - For creating the web application

### Libraries/Modules:
- **TextBlob** - For text-based sentiment analysis
- **DeepFace** - For facial expression-based emotion detection
- **Spotipy** - For Spotify API integration
- **OpenCV** - For capturing and processing images from the webcam

---

## **Installation**

Follow these steps to set up the project locally:

### **1. Clone the repository**
```bash
git clone https://github.com/your-username/emotion-music-recommendation.git
cd emotion-music-recommendation
```

### **2. Create a virtual environment**
```bash
python -m venv env
```

### **3. Activate the virtual environment**
- On Windows:
  ```bash
  env\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### **4. Install dependencies**
```bash
pip install -r requirements.txt
```

### **5. Set up Spotify API credentials**
- Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
- Create a new app and get the **Client ID**, **Client Secret**, and **Redirect URI**.
- Update the `config.py` file with these details:
  ```python
  SPOTIFY_CLIENT_ID = "your_client_id"
  SPOTIFY_CLIENT_SECRET = "your_client_secret"
  SPOTIFY_REDIRECT_URI = "http://localhost:5000/callback"
  ```

---

## **Usage**

### **Run the Application**
1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Choose a mode of emotion detection:
   - Enter a text description of your mood (e.g., "I feel happy").
   - Use the facial emotion detection option.

4. A playlist will be created on Spotify based on your detected mood, and you'll be redirected to the playlist.

---

## **Folder Structure**

```
emotion-music-recommendation/
├── app.py                    # Main application file
├── config.py                 # Spotify API credentials
├── emotion_detection.py      # Emotion detection logic
├── music_recommendation.py   # Spotify API integration and music recommendation
├── templates/
│   └── index.html            # Frontend for user interaction
├── static/                   # Static assets (CSS, JS)
└── requirements.txt          # Project dependencies
```

---

## **Dependencies**

Install these dependencies via the `requirements.txt` file:

```text
Flask==2.3.3
spotipy==2.23.0
textblob==0.17.1
DeepFace==0.0.78
opencv-python==4.8.1.78
tensorflow==2.13.0
```

---

## **How it Works**

1. **Emotion Detection**:
   - Text input: Uses **TextBlob** to analyze sentiment and infer emotion (e.g., happy, sad, neutral).
   - Facial expression: Uses **DeepFace** and **OpenCV** to analyze facial emotions in real time.

2. **Music Recommendation**:
   - Maps emotions to Spotify's "mood" tags (e.g., happy → energetic, sad → calm).
   - Fetches tracks matching the mood using the Spotify API.

3. **Playlist Creation**:
   - A new Spotify playlist is created using the recommended tracks.
   - The user is redirected to their Spotify playlist.

---

## **Troubleshooting**

### Common Issues:
1. **`ModuleNotFoundError`**:
   - Ensure all dependencies are installed correctly using:
     ```bash
     pip install -r requirements.txt
     ```

2. **Spotify API Errors**:
   - Verify your **Client ID**, **Client Secret**, and **Redirect URI** in `config.py`.
   - Ensure your Spotify account is properly registered in the Spotify Developer Dashboard.

3. **DeepFace Errors**:
   - Ensure TensorFlow is installed and compatible with the `DeepFace` version:
     ```bash
     pip install tensorflow==2.13.0
     ```

---

## **Future Enhancements**

- Add support for multiple languages in text-based sentiment analysis.
- Integrate more advanced machine learning models for emotion detection.
- Expand to include video-based real-time emotion tracking.

---

## **Contributing**

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

---

