import numpy as np
import SimpleITK as sitk
import pydicom


def save_dicom(orgpath, npy, config, idx):
    
    """
    Original code can be found in : https://github.com/jryoungw/DicomWrite/blob/master/write_dicom.py
    Supported by Mingyu Kim
    """

    
    dcm = pydicom.read_file(orgpath)
    savepath = config.result_path + '/' + '/'.join(orgpath.split('/')[:-1])
    os.makedirs(config.result_path + '/' + '/'.join(orgpath.split('/')[:-1]), exist_ok=True)
    ds = pydicom.FileDataset(config.result_path + '/' + '/'.join(orgpath.split('/')[:-1])+\
                             '/'+'{:05d}.dcm'.format(idx), {}, file_meta=pydicom.Dataset(), \
                             preamble=("\0"*128).encode())
    ds.ImageType=dcm.ImageType
    ds.SOPClassUID=dcm.SOPClassUID
    ds.SOPInstanceUID=dcm.SOPInstanceUID

    methods = [i for i in dcm.__dir__() if '_' not in i]

    for m in methods:
        try:
            exec('ds.'+m+'=dcm.'+m)
        except:
            print('[*] '+m+' is not implemented')
    try:
        ds.RescaleIntercept = '-1024'
    except:
        pass
    try:
        ds.RescaleSlope = '1'
    except:
        pass
    try:
        ds.WindowCenterWidthExplanation=dcm.WindowCenterWidthExplanation
    except:
        pass
        
    ds.is_little_endian = True
    
    ##################### If pixels are not written correctly, change this value to True #####################
    ds.is_implicit_VR = False
    ########################################################################################################## 
    savepath = os.path.join(savepath, '{:05d}.dcm'.format(idx+1))
    ds.PixelData = npy.tostring()
    ds.save_as(savepath)
