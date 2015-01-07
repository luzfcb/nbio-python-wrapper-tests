# -*- coding:utf-8 -*-
import platform
import sys
import os
import ctypes
# http://tungwaiyip.info/blog/2009/07/16/ctype_performance_benchmark
# http://stackoverflow.com/questions/8638942/python-ctypes-pointer-to-pointer-to-structure
# http://stackoverflow.com/questions/3131854/how-to-return-a-pointer-to-a-structure-in-ctypes
# http://stackoverflow.com/questions/4351721/python-ctypes-passing-a-struct-to-a-function-as-a-pointer-to-get-back-data
# http://www.sagemath.org/doc/numerical_sage/ctypes.html
# http://www.sagemath.org/doc/numerical_sage/ctypes_examples.html
# http://tentacles666.wordpress.com/2012/01/21/python-ctypes-dereferencing-a-pointer-to-a-c/
# https://docs.python.org/2/library/ctypes.html#ctypes-fundamental-data-types-2
# http://stackoverflow.com/questions/1871375/python-ctypes-initializing-c-char-p
# http://eli.thegreenplace.net/2008/08/31/ctypes-calling-cc-code-from-python/
# http://stackoverflow.com/questions/12712585/readprocessmemory-with-ctypes


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
LIB_LINUX_X86 = os.path.join(CURRENT_DIR, 'libs', 'linux_x86', 'libNBioBSP.so')
LIB_LINUX_X86_X64 = os.path.join(CURRENT_DIR, 'libs', 'linux_x86_x64', 'libNBioBSP.so')
LIB_WIN32 = os.path.join(CURRENT_DIR, 'libs', 'win32', 'NBioBSP.dll')
#LIB_WIN64 = os.path.join(CURRENT_DIR, 'libs', 'win64', 'NBioBSP.dll')

print(CURRENT_DIR)
print(LIB_LINUX_X86)
print(LIB_LINUX_X86_X64)
print(LIB_WIN32)

lib = None

PLATFORM_SYSTEM = platform.system()
PLATFORM_ARCHITECTURE = platform.architecture()[0]
print(PLATFORM_SYSTEM)
print(PLATFORM_ARCHITECTURE)

is_64bits = sys.maxsize > 2**32

if '64' in PLATFORM_ARCHITECTURE and 'Linux' in PLATFORM_SYSTEM:
    lib = ctypes.CDLL(LIB_LINUX_X86_X64)
elif '32' in PLATFORM_ARCHITECTURE and 'Linux' in PLATFORM_SYSTEM:
    ctypes.CDLL(LIB_LINUX_X86)

if '64' in PLATFORM_ARCHITECTURE and 'Windows' in PLATFORM_SYSTEM:
    #lib = ctypes.CDLL(LIB_WIN64)
    pass
elif '32' in PLATFORM_ARCHITECTURE and 'Windows' in PLATFORM_SYSTEM:
    ctypes.CDLL(LIB_WIN32)

print(lib)





# NBioAPI_SINT = 'int'
NBioAPI_SINT = ctypes.c_int

#NBioAPI_SINT_PTR = 'int *'
NBioAPI_SINT_PTR = ctypes.POINTER(ctypes.c_int)

#NBioAPI_UINT = 'unsigned int'
NBioAPI_UINT = ctypes.c_uint

#NBioAPI_UINT_PTR = 'unsigned int *'
NBioAPI_UINT_PTR = ctypes.POINTER(ctypes.c_uint)

#NBioAPI_SINT8 = 'signed char'
NBioAPI_SINT8 = ctypes.c_int8

#NBioAPI_SINT8_PTR = 'signed char *'
NBioAPI_SINT8_PTR = ctypes.POINTER(ctypes.c_int8)

#NBioAPI_UINT8 = 'unsigned char'
NBioAPI_UINT8 = ctypes.c_uint8

#NBioAPI_UINT8_PTR = 'unsigned char *'
NBioAPI_UINT8_PTR = ctypes.POINTER(ctypes.c_uint8)

#NBioAPI_SINT16 = 'signed short'
NBioAPI_SINT16 = ctypes.c_int16

#NBioAPI_SINT16_PRT = 'signed short *'
NBioAPI_SINT16_PRT = ctypes.POINTER(ctypes.c_int16)

#NBioAPI_UINT16 = 'unsigned short'
NBioAPI_UINT16 = ctypes.c_uint16

#NBioAPI_UINT16_PTR = 'unsigned short *'
NBioAPI_UINT16_PTR = ctypes.POINTER(ctypes.c_uint16)

#NBioAPI_SINT32 = 'signed int'
NBioAPI_SINT32 = ctypes.c_int32

#NBioAPI_SINT32_PTR = 'signed int *'
NBioAPI_SINT32_PTR = ctypes.POINTER(ctypes.c_int32)

#NBioAPI_UINT32 = 'unsigned int'
NBioAPI_UINT32 = ctypes.c_uint32

#NBioAPI_UINT32_PTR = 'unsigned int *'
NBioAPI_UINT32_PTR = ctypes.POINTER(ctypes.c_uint32)

#NBioAPI_SINT64 = 'long long int'
NBioAPI_SINT64 = ctypes.c_int64

#NBioAPI_SINT64_PTR = 'long long int *'
NBioAPI_SINT64_PTR = ctypes.POINTER(ctypes.c_int64)

#NBioAPI_UINT64 = 'unsigned long long int'
NBioAPI_UINT64 = ctypes.c_uint64

#NBioAPI_UINT64_PTR = 'unsigned long long int *'
NBioAPI_UINT64_PTR = ctypes.POINTER(ctypes.c_uint64)

#NBioAPI_SLONG = 'signed long'
NBioAPI_SLONG = ctypes.c_long

#NBioAPI_SLONG_PTR = 'signed long *'
NBioAPI_SLONG_PTR = ctypes.POINTER(ctypes.c_long)

#NBioAPI_ULONG = 'unsigned long'
NBioAPI_ULONG = ctypes.c_ulong

#NBioAPI_ULONG_PTR = 'unsigned long *'
NBioAPI_ULONG_PTR = ctypes.POINTER(ctypes.c_ulong)

#NBioAPI_DOUBLE = 'double'
NBioAPI_DOUBLE = ctypes.c_double

#NBioAPI_FLOAT = 'float'
NBioAPI_FLOAT = ctypes.c_float

#NBioAPI_FLOAT_PTR = 'float *'
NBioAPI_FLOAT_PTR = ctypes.POINTER(ctypes.c_float)

#NBioAPI_DOUBLE_PTR = 'double *'
NBioAPI_DOUBLE_PTR = ctypes.POINTER(ctypes.c_double)


#NBioAPI_BOOL = 'int'
NBioAPI_BOOL = ctypes.c_bool

#NBioAPI_CHAR = 'char'
NBioAPI_CHAR = ctypes.c_char

#NBioAPI_CHAR_PTR = 'char *'
NBioAPI_CHAR_PTR = ctypes.c_char_p

#NBioAPI_BYTE = 'signed char'
NBioAPI_BYTE = ctypes.c_byte

#NBioAPI_BYTE_PTR = 'signed char *'
NBioAPI_BYTE_PTR = ctypes.POINTER(ctypes.c_byte)

#NBioAPI_BYTE = 'unsigned char'
NBioAPI_UBYTE = ctypes.c_ubyte

#NBioAPI_BYTE_PTR = 'unsigned char *'
NBioAPI_UBYTE_PTR = ctypes.POINTER(ctypes.c_ubyte)

#NBioAPI_WCHAR = 'wchar_t'
NBioAPI_WCHAR = ctypes.c_wchar

#NBioAPI_WCHAR_PTR = 'wchar_t *'
NBioAPI_WCHAR_PTR = ctypes.c_wchar_p

CHAR = NBioAPI_CHAR
LPSTR = NBioAPI_CHAR_PTR
NBioAPI_VOID = None
NBioAPI_VOID_PTR = ctypes.c_void_p

HINSTANCE = NBioAPI_VOID_PTR
NBioAPI_HWND = NBioAPI_UINT32

NBioAPI_FALSE = 0
NBioAPI_TRUE = 1

NBioAPI_RETURN = NBioAPI_UINT32
NBioAPI_HANDLE = NBioAPI_UINT32
NBioAPI_HANDLE_PTR = NBioAPI_UINT32_PTR
NBioAPI_INIT_INFO_PTR = NBioAPI_VOID_PTR
NBioAPI_DEVICE_ID = NBioAPI_UINT16
NBioAPI_DEVICE_ID_PTR_TO_PTR = ctypes.POINTER(ctypes.POINTER(ctypes.c_uint16))

NBioAPI_DEVICE_INFO_PTR = NBioAPI_VOID_PTR


class NBioAPI_VERSION(ctypes.Structure):
    # NBioAPI_Type.h:19
    # /*!
    #    \struct NBioAPI_VERSION
    #    \brief Ex) v3.12 (Build No.34) : Major = 3, Minor = 1234
    # */
    # typedef struct nbioapi_version
    # {
    #    NBioAPI_UINT32      Major;    //!< Major version information
    #    NBioAPI_UINT32      Minor;    //!< Minor version information
    # } NBioAPI_VERSION, * NBioAPI_VERSION_PTR;
    _fields_ = [("Major", NBioAPI_UINT32), ("Minor", NBioAPI_UINT32)]


NBioAPI_VERSION_PTR = ctypes.POINTER(NBioAPI_VERSION)

NBioAPI_WINDOW_OPTION = NBioAPI_VERSION
NBioAPI_WINDOW_OPTION_PTR = NBioAPI_VERSION_PTR


class NBioAPI_DEVICE_INFO_EX(ctypes.Structure):
    # NBioAPI_Type.h:535
    # /*!
    #    \struct NBioAPI_DEVICE_INFO_EX
    #    \brief eNBioBSP SDK Device information extension
    # */
    # typedef struct nbioapi_deviceinfoex
    # {
    #    NBioAPI_DEVICE_ID NameID;                 //!< Device ID
    #    NBioAPI_UINT16    Instance;               //!< Instance value
    #
    #    NBioAPI_CHAR      Name[64];               //!< Name string
    #    NBioAPI_CHAR      Description[256];       //!< Description string
    #    NBioAPI_CHAR      Dll[64];                //!< Dll name string
    #    NBioAPI_CHAR      Sys[64];                //!< Sys name string
    #
    #    NBioAPI_UINT32    AutoOn;                 //!< Is support Auto-on
    #    NBioAPI_UINT32    Brightness;             //!< Brightness value
    #    NBioAPI_UINT32    Contrast;               //!< Contrast value
    #    NBioAPI_UINT32    Gain;                   //!< Gain value
    #
    #    NBioAPI_UINT32    Reserved[8];            //!< reserved
    # } NBioAPI_DEVICE_INFO_EX, *NBioAPI_DEVICE_INFO_EX_PTR;
    #
    _fields_ = [('NameID', NBioAPI_DEVICE_ID),
                ('Instance', NBioAPI_UINT16),
                ('Name[64]', NBioAPI_CHAR),
                ('Description[256]', NBioAPI_CHAR),
                ('Dll[64]', NBioAPI_CHAR),
                ('Sys[64]', NBioAPI_CHAR),
                ('AutoOn', NBioAPI_UINT32),
                ('Brightness', NBioAPI_UINT32),
                ('Contrast', NBioAPI_UINT32),
                ('Gain', NBioAPI_UINT32),
                ('Reserved[8]', NBioAPI_UINT32)]


NBioAPI_DEVICE_INFO_EX_PTR = ctypes.POINTER(NBioAPI_DEVICE_INFO_EX)
NBioAPI_DEVICE_INFO_EX_PTR_TO_PTR = ctypes.POINTER(ctypes.POINTER(NBioAPI_DEVICE_INFO_EX))

lib.NBioAPI_Init.restype = NBioAPI_RETURN
print(lib.NBioAPI_Init())
lib.NBioAPI_GetVersion.restype = NBioAPI_RETURN

print(lib.NBioAPI_GetVersion())
