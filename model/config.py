import torch


def load_config():
    return {
        "BATCH_SIZE": 128,
        "GAMMA": 0.999,
        "EPS_START": 0.9,
        "EPS_END": 0.05,
        "EPS_DECAY": 200,
        "TARGET_UPDATE": 10,
        "DEVICE": torch.device("cuda" if torch.cuda.is_available() else "cpu"),
    }
