import torch

device = torch.device(
    "cuda"if torch.cuda.is_available() else "CPU"
)

print("Device:", device)
