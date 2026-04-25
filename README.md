“This project was tested using Google Colab.”
This project is a simple implementation of an AI-based routing and response system.
In Phase 1, I used sentence-transformers to convert bot personas and input posts into vectors. Then I calculated cosine similarity to find which bots are most relevant to the post.
In Phase 2, I created a basic content generator. Each bot generates a short post based on a topic and a mock search result.
In Phase 3, I implemented a simple reply system. The bot responds based on its personality and ignores instructions like “ignore previous commands”, which helps prevent prompt injection.
This project focuses on understanding the basic concepts like embeddings, similarity matching, and context-based replies.
