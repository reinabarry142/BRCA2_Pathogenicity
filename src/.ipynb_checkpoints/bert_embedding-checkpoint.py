import torch
from transformers import BertTokenizer, BertModel

# === Chargement du modèle ProtBERT ===
tokenizer = BertTokenizer.from_pretrained("Rostlab/prot_bert", do_lower_case=False)
model = BertModel.from_pretrained("Rostlab/prot_bert")
model.eval()

# === Fonction pour générer l'embedding ===
def get_embedding(sequence):
    spaced_seq = ' '.join(list(sequence.strip()))
    tokens = tokenizer(spaced_seq, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**tokens)
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
    return embedding