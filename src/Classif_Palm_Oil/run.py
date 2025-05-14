import torch
from torch.utils.data import DataLoader
from Classif_Palm_oil.dataset import PalmOilDataset
from Classif_Palm_oil.model import SimpleCNN
from Classif_Palm_oil.train import train_model
from Classif_Palm_oil.evaluate import evaluate_model


if __name__ == '__main__':
    # Placeholder data loading logic
    labels = [{"filename": f"image_{i}.jpg", "label": i % 2} for i in range(100)]
    image_dir = "./Raw_kaggle_data/images"

    dataset = PalmOilDataset(image_dir, labels)
    loader = DataLoader(dataset, batch_size=8, shuffle=True)

    model = SimpleCNN()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    train_model(model, loader, loader, num_epochs=5, device=device)
    evaluate_model(model, loader, device=device)


