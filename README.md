*A Recurrent Neural Network (RNN) is a type of neural network designed for sequential data processing.

*Unlike traditional neural networks, RNNs have memory, allowing them to process and learn from previous inputs, making them ideal for tasks involving sequences like:

      -Text processing (chatbots, sentiment analysis)
      -Speech recognition
      -Time-series prediction (stock prices, weather forecasting)
      -Machine translation

Types of RNN (Recurrent Neural Networks):
      -Vanilla RNN
      -LSTM
      -Gated Recurrent Unt(GRU)
      -Bidirection RNN

      
1)What is IMDB?
      *IMDB (Internet Movie Database) is a large dataset containing movie-related information, such as reviews, ratings, and metadata.
      *It is widely used in sentiment analysis, natural language processing (NLP), and machine learning (ML) projects.
      *One of the most popular IMDB datasets is the IMDB Movie Reviews Dataset, which contains 50,000 reviews labeled as positive or negative. 
      *This dataset is commonly used for training sentiment analysis models.

VERSION:
     i) pip install imdb ==0.1.5
     ii)TensorFlow 2.6.0 or later (Latest stable version preferred).
         Keras comes bundled with TensorFlow 2.x, so no need to install separately
    iii)For running Streamlit("Open Terminal"):
        type "streamlit run main.py"
        NOTE : Here main.py is the current file name to be run
           
2)What is Emotion Recognition? 
       *Emotion Recognition is the process of identifying human emotions using machine learning (ML) and artificial intelligence (AI). 
       *It involves analyzing text, speech, facial expressions, or physiological signals to classify emotions like happiness, sadness, anger, fear, surprise, and neutrality.

VERSION:
    i)Recommended Versions to Run model_from_json
         -TensorFlow: 2.6.0 or later
         -Keras: Comes bundled with TensorFlow 2.x (tensorflow.keras)

Common Issues & Fixes:
1️⃣ ImportError: No module named 'keras'
🔹 Solution: Use tensorflow.keras instead of keras

2️⃣ Version Mismatch (AttributeError)
🔹 Solution: Upgrade TensorFlow with pip install --upgrade tensorflow

emotionRecognition.h5 and emotionRecognition.keras file "not uploaded due to larger in size"
