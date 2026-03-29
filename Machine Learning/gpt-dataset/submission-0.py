import torch
from typing import List, Tuple

class Solution:
    def batch_loader(self, raw_dataset: str, context_length: int, batch_size: int) -> Tuple[List[List[str]]]:
        # You must start by generating batch_size different random indices in the appropriate range
        # using a single call to torch.randint()
        torch.manual_seed(0)
        words = raw_dataset.split()
        indices = torch.randint(low=0, high=len(words)-context_length, size=(batch_size,))
        X = [
            words[ind:ind+context_length] for ind in indices
        ]
        Y = [
            words[ind+1:ind+context_length+1] for ind in indices
        ]
        return (X, Y)

