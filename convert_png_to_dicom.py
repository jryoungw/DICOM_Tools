import pydicom
import numpy as np
import SimpleITK as sitk
import cv2

def png2dcm(
            img:str, 
            save_path:str,
            patient_sex:str,
            birth_year:int=2012,
            birth_month:int=8,
            birth_date:int=2,
            patient_name:str='ANONYMIZED',
            ) -> None:
    img = cv2.imread(img, -1)
    if img.shape[-1] > 1:
        try:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        except:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = img.astype(np.uint16)
    ds = pydicom.dataset.Dataset()
    from pydicom.uid import ExplicitVRLittleEndian
    ds.TransferSyntaxUID = ExplicitVRLittleEndian
    ds.ImplementationClassUID = '1.1'
    ds.FileMetaInformationVersion = b'\x00\x01'
    ds.MediaStorageSOPClassUID = '10101010' # Arbitrary value
    ds.MediaStorageSOPInstanceUID = '10101011' # Arbitrary value
    ds = pydicom.FileDataset(save_path, {}, file_meta=ds, preamble=b'\x00'*128)

    ds.SOPClassUID = 'Computed Radiography Image Storage' # Arbitrary value
    ds.SOPInstanceUID = '1111' # Arbrtrary value
    ds.SeriesInstanceUID = '2222'
    ds.StudyInstanceUID = '3333'
    ds.Modality = ''
    ds.AcquisitionDate = datetime.today().strftime('%Y%m%d')
    ds.AcquisitionTime = '142253'
    ds.is_little_endian = True
    ds.is_implicit_VR = False
    ds.BitsAllocated = 16
    ds.BitsStored = 16
    ds.HighBit = 12
    ds.SamplesPerPixel = 1
    ds.Rows = img.shape[0]
    ds.Columns = img.shape[1]
    ds.PhotometricInterpretation = 'MONOCHROME2'
    ds.PixelSpacing = '0.1' # Arbitrary value
    ds.PixelRepresentation = 0
    ds.PatientBirthDate = f"{birth_year}{birth_month:02}{birth_date:02}"
    ds.PatientName = patient_name
    ds.StudyDate = datetime.today().strftime('%Y%m%d')
    ds.StudyTime = '12345' # Arbitrary value
    ds.StudyID = '23456' # Arbitrary value
    ds.SeriesNumber = '34567' # Arbitrary value
    ds.SpecificCharacterSet = 'ISO_IR 100'
    ds.PatientID = '12345678' # Arbitrary value
    assert patient_sex in ['M', 'F', 'O'], "Patient Sex attribute should be one of M(Male), F(Female), O(Others)."
    ds.PatientSex = patient_sex
    ds.WindowCenter = 127
    ds.WindowWidth = 128
    ds.PatientOrientation = ''
    ds.RescaleIntercept = '0'
    ds.RescaleSlope = '1'
    ds.ImageType = ['ORIGINAL', 'PRIMARY', '']
    ds.PixelData = img.tobytes()
    ds.save_as(save_path, write_like_original=False)

def replace_only_pixels(orgpath, pngpath, savepath):
    
    """
    Pixel replacement using template DICOM (orgpath).
    """

    img = cv2.imread(pngpath, -1)
    if img.shape[-1] > 1:
        try:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        except:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = img.astype(np.uint16)
    dcm = pydicom.dcmread(orgpath)
    # print(dcm)
    from pydicom.uid import ExplicitVRLittleEndian
    ds = pydicom.dataset.Dataset()
    ds.TransferSyntaxUID = ExplicitVRLittleEndian
    ds.ImplementationClassUID = '1.1'
    ds.FileMetaInformationVersion = b'\x00\x01'
    ds.MediaStorageSOPClassUID = '10101010' # Arbitrary value
    ds.MediaStorageSOPInstanceUID = '10101011' # Arbitrary value


    ds = pydicom.FileDataset(savepath, {}, file_meta=ds, \
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
        ds.RescaleIntercept = '0'
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
    ds.PixelSpacing = ''
    ds.Rows = img.shape[0]
    ds.Columns = img.shape[1]
    ds.BitsAllocated = 16
    ds.BitsStored = 12
    ds.HighBit = 8
    ds.SamplesPerPixel = 1
    ds.WindowCenter = 127
    ds.WindowWidth = 128

    ds.is_little_endian = True
    
    ##################### If pixels are not written correctly, change this value to True #####################
    ds.is_implicit_VR = False
    ########################################################################################################## 
    ds.PixelData = img.tobytes()
    ds.save_as(savepath)
