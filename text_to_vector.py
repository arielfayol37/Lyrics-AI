from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import heapq

# Load pre-trained BERT model and tokenizer
BERT_MODEL_NAME = 'bert-base-uncased'
bert_tokenizer = BertTokenizer.from_pretrained(BERT_MODEL_NAME)
bert_model = BertModel.from_pretrained(BERT_MODEL_NAME)
bert_model.eval()

def attention_pooling(hidden_states, attention_mask):
    # Apply attention mask to hidden states
    attention_mask_expanded = attention_mask.unsqueeze(-1).expand(hidden_states.size())
    masked_hidden_states = hidden_states * attention_mask_expanded
    
    # Calculate attention scores and apply softmax
    attention_scores = torch.nn.functional.softmax(masked_hidden_states, dim=1)
    
    # Weighted sum using attention scores
    pooled_output = (masked_hidden_states * attention_scores).sum(dim=1)
    return pooled_output


lyrics = {"ariel":"I love you babe", "john":"calamity is a bad thing", "naija":"Nigerians are scary", "girlfriend":"She is very beautiful, and she is lightskin. She also has very long hair and smells nice and she is good at physics."}

def search_lyric(lyric):
        input_text = lyric
        # Tokenize and encode the input text
        max_length = 512  # BERT's maximum sequence length
        input_tokens = bert_tokenizer.encode(input_text, add_special_tokens=True, max_length=max_length, truncation=True, padding='max_length')
        with torch.no_grad():
            input_tensor = torch.tensor([input_tokens])
            attention_mask = (input_tensor != 0).float()  # Create attention mask
            encoded_output = bert_model(input_tensor, attention_mask=attention_mask)[0]  # Take the hidden states

        # Apply attention-based pooling to encoded output
        encoded_output_pooled = attention_pooling(encoded_output, attention_mask)

        # Retrieve all question objects from the database
        all_lyrics = lyrics

        # Calculate cosine similarity with stored question encodings
        similar_questions = []
        with torch.no_grad():
                
            for lyric_title in all_lyrics:
                lyric_tokens = bert_tokenizer.encode(lyrics[lyric_title], add_special_tokens=True, \
                                                     max_length=max_length, truncation=True, padding='max_length')
                lyric_tensor = torch.tensor([lyric_tokens])
                attention_mask = (lyric_tensor != 0).float()  # Create attention mask
                encoded_output = bert_model(lyric_tensor, attention_mask=attention_mask)[0]  # Take the hidden states                
                question_encoded_output_pooled = attention_pooling(encoded_output, attention_mask)

                similarity_score = cosine_similarity(encoded_output_pooled, question_encoded_output_pooled).item()
                similar_questions.append({'lyric_title': lyric_title, 'similarity': similarity_score})

        # Sort by similarity score and get top n
        top_n = 3
        top_similar_questions = heapq.nlargest(top_n, similar_questions, key=lambda x: x['similarity'])
        print(top_similar_questions)

# search_lyric("My girlfriend has long hair and she is good at physics. She is gorgeous")