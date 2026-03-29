import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        words = []
        for text in set(positive + negative):
            words.extend(text.split())
        words = sorted(list(set(words)))
        word_to_ind = {
            v:k+1 for k,v in enumerate(words)
        }
        def encode(text):
            return [word_to_ind[w] for w in text.split()]
        
        positive_encoded = [encode(s) for s in positive]
        negative_encoded = [encode(s) for s in negative]
        all_encoded = positive_encoded + negative_encoded
        all_encoded = [torch.Tensor(i) for i in all_encoded]
        return nn.utils.rnn.pad_sequence(all_encoded, batch_first=True)

