import pydicom
import cv2
import numpy as np

def png2dcm(
            img:str, 
            save_path:str
            ) -> None:
    img = cv2.imread(img, -1)
    if img.shape[-1] > 1:
        try:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        except:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ds = pydicom.dataset.Dataset()
    from pydicom.uid import ExplicitVRLittleEndian
    ds.TransferSyntaxUID = ExplicitVRLittleEndian
    ds.ImplementationClassUID = '1.1'
    ds = pydicom.FileDataset(save_path, {}, file_meta=ds, preamble=b'\x00'*128)
    ds.is_little_endian = True
    ds.is_implicit_VR = False
    ds.BitsAllocated = 8
    ds.Rows = img.shape[0]
    ds.Columns = img.shape[1]
    ds.BitsStored = 16
    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = 'MONOCHROME2'
    ds.PixelRepresentation = 0
    ds.PixelData = img.tobytes()
    ds.save_as(save_path)
