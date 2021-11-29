from PIL import Image
from torchvision.transforms import transforms
from torch.utils.data import Dataset, DataLoader
import random




class CustomDataset(Dataset):
  def __init__(self, data, fgbgtransforms, masktransforms, depthtransforms):
    self.fgbg_files, self.mask_files, self.depth_files = zip(*data)
    self.fgbgtransforms = fgbgtransforms
    self.masktransforms = masktransforms
    self.depthtransforms = depthtransforms
    
  def __len__(self):
    return len(self.fgbg_files)
    
  def __getitem__(self, index):
    
    fgbg_image = Image.open(self.fgbg_files[index])
    mask_image = Image.open(self.mask_files[index])
    depth_image = Image.open(self.depth_files[index])

    
    fgbg_image = self.fgbgtransforms(fgbg_image)
    mask_image = self.masktransforms(mask_image)
    depth_image = self.depthtransforms(depth_image)
    

    
    return {'fgbg':fgbg_image, 'mask':mask_image, 'depth':depth_image}
  
