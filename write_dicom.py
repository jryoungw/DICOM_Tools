def write_dicom(orgpath, newpath, savepath):
    """
        Write dicom file using pydicom package.
        There are two dicom handling packages in python - SimpleITK and pydicom.
        As SimpleITK.WriteImage function does not support negative pixel value (Haunsfield unit), 
        I strongly recommend readers to use pydicom when write dicom images.
        
        Args:
            orgpath  - original dicom file path
            newpath  - new dicom file path (this file contains only Hounsfield value) 
                       if this file is npy, np.load will load image. 
                       if this file is not npy (i.e. .hdr, .dcm, .nii), SimpleITK will load image.
            savepath - path for new dicom to be saved.
    """
    dcm = pydicom.read_file(orgpath)
    ds = pydicom.FileDataset(savepath.split('/')[-1], {}, file_meta=pydicom.Dataset(), preamble=("\0"*128).encode())
    ds.ImageType=dcm.ImageType
    ds.SOPClassUID=dcm.SOPClassUID
    ds.SOPInstanceUID=dcm.SOPInstanceUID
    
    print(orgpath)
    try:
        ds.StudyDate=dcm.StudyDate
    except:
        print("[*] StudyDate not implemented")
    try:
        ds.SeriesDate=dcm.SeriesDate
    except:
        print("[*] SeriesDate not implemented")
    try:
        ds.AcquisitionDate=dcm.AcquisitionDate
    except:
        print("[*] AcquisitionDate not implemented")
    try:
        ds.ContentDate=dcm.ContentDate
    except:
        print("[*] ContentDate not implemented")
    try:
        ds.StudyTime=dcm.StudyTime
    except:
        print("[*] StudyTime not implemented")
    try:
        ds.SeriesTime=dcm.SeriesTime
    except:
        print("[*] SeriesTime not implemented")
    try:
        ds.AcquisitionTime=dcm.AcquisitionTime
    except:
        print("[*] AcquisitionTime not implemented")
    try:
        ds.ContentTime=dcm.ContentTime
    except:
        print("[*] ContentTime not implemented")
    try:
        ds.AccessionNumber=dcm.AccessionNumber
    except:
        print("[*] AccessionNumber not implemented")
    try:
        ds.Modality=dcm.Modality
    except:
        print("[*] Modality not implemented")
    try:
        ds.Manufacturer=dcm.Manufacturer
    except:
        print("[*] Manufacturer not implemented")
    try:
        ds.InstitutionName=dcm.InstitutionName
    except:
        print("[*] InstitutionName not implemented")
    try:
        ds.InstitutionAddress=dcm.InstitutionAddress
    except:
        print("[*] InstitutionAddress not implemented")
    try:
        ds.ReferringPhysicianName=dcm.ReferringPhysicianName
    except:
        print("[*] ReferringPhysicianName not implemented")
    try:
        ds.StationName=dcm.StationName
    except:
        print("[*] StationName not implemented")
    try:
        ds.StudyDescription=dcm.StudyDescription
    except:
        print("[*] StudyDescription not implemented")
    try:
        ds.SeriesDescription=dcm.SeriesDescription
    except:
        print("[*] SeriesDescription not implemented")
        #ds.PhysiciansOfRecord=dcm.PhysiciansOfRecord
    try:
        ds.PerformingPhysicianName=dcm.PerformingPhysicianName
    except:
        print("[*] PerformingPhysicianName not implemented")
    try:
        ds.OperatorsName=dcm.OperatorsName
    except:
        print("[*] OperatorsName not implemented")
    try:
        ds.ManufacturerModelName=dcm.ManufacturerModelName
    except:
        print("[*] ManufacturerModelName not implemented")
    try:
        ds.PatientName=dcm.PatientName
    except:
        print("[*] PatientName not implemented")
    try:
        ds.PatientID=dcm.PatientID
    except:
        print("[*] PatientID not implemented")
    try:
        ds.PatientBirthDate=dcm.PatientBirthDate
    except:
        print("[*] PatientBirthDatee not implemented")
    try:
        ds.PatientSex=dcm.PatientSex
    except:
        print("[*] PatientSex not implemented")
        #ds.OtherPatientNames=dcm.OtherPatientNames
    try:
        ds.PatientAge=dcm.PatientAge
    except:
        print("[*] PatientAge not implemented")
    try:
        ds.BodyPartExamined=dcm.BodyPartExamined
    except:
        print("[*] BodyPartExamined not implemented")
    try:
        ds.SliceThickness=dcm.SliceThickness
    except:
        print("[*] SliceThicness not implemented")
    try:
        ds.KVP=dcm.KVP
    except:
        print("[*] KVP not implemented")
    try:
        ds.DataCollectionDiameter=dcm.DataCollectionDiameter
    except:
        print("[*] DataCollectionDiameter not implemented")
    try:
        ds.DeviceSerialNumber=dcm.DeviceSerialNumber
    except:
        print("[*] DeviceSerialNumber not implemented")
    try:
        ds.SoftwareVersions=dcm.SoftwareVersions
    except:
        print("[*] SoftwareVersions not implemented")
    try:
        ds.ProtocolName=dcm.ProtocolName
    except:
        print("[*] ProtocolName not implemented")
    try:
        ds.ReconstructionDiameter=dcm.ReconstructionDiameter
    except:
        print("[*] ReconstructionDiameter not implemented")
    try:
        ds.DistanceSourceToDetector=dcm.DistanceSourceToDetector
    except:
        print("[*] DistanceSourceToDetector not implemented")
    try:
        ds.DistanceSourceToPatient=dcm.DistanceSourceToPatient
    except:
        print("[*] DistanceSourceToPatient not implemented")
    try:
        ds.GantryDetectorTilt=dcm.GantryDetectorTilt
    except:
        print("[*] GantryDetectorTilt not implemented")
    try:
        ds.TableHeight=dcm.TableHeight
    except:
        print("[*] TableHeight not implemented")
    try:
        ds.RotationDirection=dcm.RotationDirection
    except:
        print("[*] RotationDirection not implemented")
    try:
        ds.ExposureTime=dcm.ExposureTime
    except:
        print("[*] ExposureTime not implemented")
    try:
        ds.XRayTubeCurrent=dcm.XRayTubeCurrent
    except:
        print("[*] XRayTubeCurrent not implemented")
    try:
        ds.Exposure=dcm.Exposure
    except:
        print("[*] Exposure not implemented")
    try:
        ds.FilterType=dcm.FilterType
    except:
        print("[*] FilterType not implemented")
    try:
        ds.GeneratorPower=dcm.GeneratorPower
    except:
        print("[*] GeneratorPower not implemented")
    try:
        ds.FocalSpots=dcm.FocalSpots
    except:
        print("[*] FocalSpots not implemented")
    try:
        ds.DateOfLastCalibration=dcm.DateOfLastCalibration
    except:
        print("[*] DateOfLastCalibration not implemented")
    try:
        ds.TimeOfLastCalibration=dcm.TimeOfLastCalibration
    except:
        print("[*] TimeOfLastCalibration not implemented")
    try:
        ds.ConvolutionKernel=dcm.ConvolutionKernel
    except:
        print("[*] ConvolutionKernel not implemented")
    try:
        ds.PatientPosition=dcm.PatientPosition
    except:
        print("[*] PatientPosition not implemented")
    try:
        ds.StudyInstanceUID=dcm.StudyInstanceUID
    except:
        print("[*] StudyInsanceeUID not implemented")
    try:
        ds.SeriesInstanceUID=dcm.SeriesInstanceUID
    except:
        print("[*] SeriesInstanceUID not implemented")
    try:
        ds.StudyID=dcm.StudyID
    except:
        print("[*] StudyID not implemented")
    try:
        ds.SeriesNumber=dcm.SeriesNumber
    except:
        print("[*] SeriesNumber not implemented")
    try:
        ds.AcquisitionNumber=dcm.AcquisitionNumber
    except:
        print("[*] AcquisitionNumber not implemented")
    try:
        ds.InstanceNumber=dcm.InstanceNumber
    except:
        print("[*] InstanceNumber not implemented")
    try:
        ds.ImagePositionPatient=dcm.ImagePositionPatient
    except:
        print("[*] ImagePositionPatient not implemented")
    try:
        ds.ImageOrientationPatient=dcm.ImageOrientationPatient
    except:
        print("[*] ImageOrientationPatient not implemented")
    try:
        ds.FrameOfReferenceUID=dcm.FrameOfReferenceUID
    except:
        print("[*] FrameOfReferenceUID not implemented")
    try:
        ds.PositionReferenceIndicator=dcm.PositionReferenceIndicator
    except:
        print("[*] PositionReferenceIndicator not implemented")
    try:
        ds.SliceLocation=dcm.SliceLocation
    except:
        print("[*] SliceLocation not implemented")
    try:
        ds.ImageComments=dcm.ImageComments
    except:
        print("[*] ImageComments not implemented")
    try:
        ds.SamplesPerPixel=1
    except:
        print("[*] SamplesPerPixel not implemented")
    try:
        ds.PhotometricInterpretation=dcm.PhotometricInterpretation
    except:
        print("[*] PhotometricInterpretation not implemented")
    try:
        ds.Rows=dcm.Rows
#         print(dcm.Rows)
    except:
        print("[*] Rows not implemented")
    try:
        ds.Columns=dcm.Columns
#         print(dcm.Columns)
    except:
        print("[*] Columns not implemented")
    try:
        ds.PixelSpacing=dcm.PixelSpacing
    except:
        print("[*] PixelSpacing not implemented")
    try:
        ds.BitsAllocated=dcm.BitsAllocated
    except:
        print("[*] BitsAllocated not implemented")
    try:
        ds.BitsStored=dcm.BitsStored
    except:
        print("[*] BitsStored not implemented")
    try:
        ds.HighBit=dcm.HighBit
    except:
        print("[*] HighBit not implemented")
    try:
        ds.PixelRepresentation=dcm.PixelRepresentation
    except:
        print("[*] PixelRepresentation not implemented")
    try:
        ds.WindowCenter=dcm.WindowCenter
    except:
        print("[*] WindowCenter not implemented")
    try:
        ds.WindowWidth=dcm.WindowWidth
    except:
        print("[*] WindowWidth not implemented")
    try:
        ds.RescaleIntercept = '-1024'
    except:
        print("[*] RescaleIntercept not implemented")
    try:
        ds.RescaleSlope = '1'
    except:
        print("[*] RescaleSlope not implemented")
    try:
        ds.WindowCenterWidthExplanation=dcm.WindowCenterWidthExplanation
    except:
        print("[*] WindowCenterWidthExplanation not implemented")
        
    ds.is_little_endian = True
    
    ##################### If pixels are not written correctly, change this value to True #####################
    ds.is_implicit_VR = False
    ########################################################################################################## 
    
    if newpath[-1]=='y':
        npy = np.load(newpath).squeeze()
    else:
        npy = sitk.GetArrayFromImage(sitk.ReadImage(newpath)).squeeze()
    
    ds.PixelData = npy.tostring()
    ds.save_as(savepath)
