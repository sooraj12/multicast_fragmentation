import ctypes

iphlpapi = ctypes.WinDLL('iphlpapi')
win32_GetAdapterIndex = iphlpapi.GetAdapterIndex
win32_GetAdapterIndex.argtypes = [ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_ulong)]

def iface_name_to_index(iface_name):
        if_idx = ctypes.c_ulong()
        iface_name_string = ctypes.c_wchar_p("\\DEVICE\\TCPIP_" + iface_name)
        ret = win32_GetAdapterIndex(iface_name_string, ctypes.byref(if_idx))
        return if_idx.value

