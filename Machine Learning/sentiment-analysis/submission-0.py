import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self, vocabulary_size: int):
        super().__init__()
        torch.manual_seed(0)
        self.embedding = nn.Embedding(
            num_embeddings=vocabulary_size,
            embedding_dim=16
        )
        self.l = nn.Linear(16, 1)
        self.activation = nn.Sigmoid()

    def forward(self, x: TensorType[int]) -> TensorType[float]:

        emb = self.embedding(x) # B, T, embed_dim tensor

        avg_emb = torch.mean(emb, dim=1)
        logits = self.l(avg_emb)
        result = self.activation(logits)

        # Hint: The embedding layer outputs a B, T, embed_dim tensor
        # but you should average it into a B, embed_dim tensor before using the Linear layer

        return torch.round(result, decimals=4)
