def overlay_text(text:str, org_path:str, save_path:str, is_ett:bool=True):
    org = pydicom.dcmread(org_path)
    npy = org.pixel_array
    dummy = np.zeros(npy.shape)
    if is_ett:
        text = cv2.putText(dummy, text, (int(npy.shape[1]*0.1),int(npy.shape[0]*0.9)), 0, 3, (255,255,255), 10)
    else:
        text = cv2.putText(dummy, text, (int(npy.shape[1]*0.1),int(npy.shape[0]*0.9)), 0, 3, (255,255,255), 10)
    text = ((text / 255) * npy.max()).astype(npy.dtype)
    overlay = np.maximum(text, npy)
    mod = pydicom.dcmread(org_path)
    mod.PixelData = overlay.tobytes()
    mod.file_meta.TransferSyntaxUID = '1.2.840.10008.1.2.1'
    mod.save_as(save_path)
