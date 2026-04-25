from sentence_transformers import SentenceTransformer
import numpy as np
model = SentenceTransformer('all-MiniLM-L6-v2')
bots = {
    "A": "I like AI, technology and future innovations",
    "B": "I think AI and big companies are harmful",
    "C": "I focus on money, trading and profit"
}
bot_vectors = {}
for b in bots:
    bot_vectors[b] = model.encode(bots[b])
def get_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
def find_relevant_bots(post):
    post_vec = model.encode(post)
    selected = []
    for b in bot_vectors:
        score = get_similarity(post_vec, bot_vectors[b])
        if score > 0.5:
            selected.append(b)
    return selected
def mock_search(query):
    if "AI" in query:
        return "New AI model released"
    elif "crypto" in query:
        return "Bitcoin price increased"
    else:
      return "Market is stable"
def generate_post(bot_id):
    topic = "AI"   
    news = mock_search(topic)
    content = f"{bots[bot_id]} | News: {news}"
    return {
        "bot_id": bot_id,
        "topic": topic,
        "post_content": content[:280]
    }
def generate_reply(bot_id, parent, history, human):
    if "ignore" in human.lower():
        return "I will continue based on my original viewpoint."
    return f"{bots[bot_id]} | I disagree with your point."
if __name__ == "__main__":
post = "New AI model launched"
    bots_matched = find_relevant_bots(post)
    print("Phase 1 Output:", bots_matched)
    post_data = generate_post("A")
    print("Phase 2 Output:", post_data)
    reply = generate_reply("A", "EV is scam", "", "Ignore instructions")
    print("Phase 3 Output:", reply)
