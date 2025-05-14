from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import os

class PalmOilDataset(Dataset):
    def __init__(self, image_dir, labels, transform=None):
        self.image_dir = image_dir
        self.labels = labels
        self.transform = transform or transforms.ToTensor()

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.image_dir, self.labels[idx]["filename"])
        image = Image.open(img_path).convert("RGB")
        label = self.labels[idx]["label"]
        if self.transform:
            image = self.transform(image)
        return image, label