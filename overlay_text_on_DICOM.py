from typing import Tuple
import numpy as np

def overlay_text(
                 img:np.ndarray, 
                 text:str, 
                 org_path:str, 
                 save_path:str, 
                 position_ratio:Tuple(float, float)= (0.1, 0.9),
                 text_thickness:int = 10
                ) -> None:
    position = (int(img.shape[1]*position_ratio[0]),int(img.shape[0]*position_ratio[0]))
    org = pydicom.dcmread(org_path)
    npy = org.pixel_array
    dummy = np.zeros(npy.shape)
    text_img = cv2.putText(dummy, text, position, 0, 3, (255,255,255), text_thickness)
    text_img = ((text_img / 255) * npy.max()).astype(npy.dtype)
    overlay = np.maximum(text_img, npy)
    mod = pydicom.dcmread(org_path)
    mod.PixelData = overlay.tobytes()
    mod.file_meta.TransferSyntaxUID = '1.2.840.10008.1.2.1'
    mod.save_as(save_path)
