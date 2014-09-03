# -*- coding:utf-8 -*-
#
from __future__ import unicode_literals

import pybindgen
import sys

OUT_FILE_NAME = 'nbio.c'
MASTER_HEADER_NAME = 'NBioAPI.h'

NBioAPI_SINT = 'int'
NBioAPI_SINT_PTR = 'int *'
NBioAPI_UINT = 'unsigned int'
NBioAPI_UINT_PTR = 'unsigned int *'
NBioAPI_SINT8 = 'signed char'
NBioAPI_SINT8_PTR = 'signed char *'
NBioAPI_UINT8 = 'unsigned char'
NBioAPI_UINT8_PTR = 'unsigned char *'
NBioAPI_SINT16 = 'signed short'
NBioAPI_SINT16_PRT = 'signed short *'
NBioAPI_UINT16 = 'unsigned short'
NBioAPI_UINT16_PTR = 'unsigned short *'
NBioAPI_SINT32 = 'signed int'
NBioAPI_SINT32_PTR = 'signed int *'
NBioAPI_UINT32 = 'unsigned int'
NBioAPI_UINT32_PTR = 'unsigned int *'
NBioAPI_SINT64 = 'long long int'
NBioAPI_SINT64_PTR = 'long long int *'
NBioAPI_UINT64 = 'unsigned long long int'
NBioAPI_UINT64_PTR = 'unsigned long long int *'
NBioAPI_SLONG = 'signed long'
NBioAPI_SLONG_PTR = 'signed long *'
NBioAPI_ULONG = 'unsigned long'
NBioAPI_ULONG_PTR = 'unsigned long *'
NBioAPI_DOUBLE = 'double'
NBioAPI_DOUBLE_PTR = 'double *'
NBioAPI_FLOAT = 'float'
NBioAPI_FLOAT_PTR = 'float *'

NBioAPI_BOOL = 'int'

NBioAPI_CHAR = 'char'
NBioAPI_CHAR_PTR = 'char *'
NBioAPI_WCHAR = 'wchar_t'
NBioAPI_WCHAR_PTR = 'wchar_t *'
NBioAPI_BYTE = 'unsigned char'
NBioAPI_BYTE_PTR = 'unsigned char *'

CHAR = NBioAPI_CHAR
LPSTR = NBioAPI_CHAR_PTR
NBioAPI_VOID = 'void'
NBioAPI_VOID_PTR = 'void*'

HINSTANCE = NBioAPI_VOID_PTR
NBioAPI_HWND = NBioAPI_UINT32

NBioAPI_FALSE = 0
NBioAPI_TRUE = 1

NBioAPI_RETURN = NBioAPI_UINT32
NBioAPI_HANDLE = NBioAPI_UINT32
NBioAPI_HANDLE_PTR = NBioAPI_UINT32_PTR
NBioAPI_INIT_INFO_PTR = NBioAPI_VOID_PTR
NBioAPI_DEVICE_ID = NBioAPI_UINT16
NBioAPI_DEVICE_ID_PTR_TO_PTR = '%s*' % NBioAPI_UINT16_PTR

NBioAPI_DEVICE_INFO_PTR = NBioAPI_VOID_PTR
NBioAPI_WINDOW_OPTION = 'nbioapi_version'
NBioAPI_WINDOW_OPTION_PTR = 'nbioapi_version *'
NBioAPI_VERSION_PTR = 'nbioapi_version *'

NBioAPI_DEVICE_INFO_EX = 'nbioapi_deviceinfoex'
NBioAPI_DEVICE_INFO_EX_PTR = 'nbioapi_deviceinfoex *'
NBioAPI_DEVICE_INFO_EX_PTR_TO_PTR = 'nbioapi_deviceinfoex **'


def generate_wrapper():
    mod = pybindgen.Module('nbio')

    mod.add_include('"NBioAPI_Basic.h"')
    mod.add_include('"NBioAPI_CheckValidity.h"')
    mod.add_include('"NBioAPI_Error.h"')
    mod.add_include('"NBioAPI_Export.h"')
    mod.add_include('"NBioAPI_ExportType.h"')
    mod.add_include('"NBioAPI_ImgConv.h"')
    mod.add_include('"NBioAPI_IndexSearch.h"')
    mod.add_include('"NBioAPI_IndexSearchType.h"')
    mod.add_include('"NBioAPI_NSearch.h"')
    mod.add_include('"NBioAPI_NSearchType.h"')
    mod.add_include('"NBioAPI_Type.h"')


    # NBioAPI_Type.h:19
    struct = mod.add_struct('nbioapi_version')
    struct.add_instance_attribute('Major', NBioAPI_UINT32)
    struct.add_instance_attribute('Minor', NBioAPI_UINT32)



    # NBioAPI_Type.h:535

    struct = mod.add_struct('nbioapi_deviceinfoex')
    struct.add_instance_attribute('NameID', NBioAPI_DEVICE_ID)
    struct.add_instance_attribute('Instance', NBioAPI_UINT16)
    struct.add_instance_attribute('Name[64]', NBioAPI_CHAR)
    struct.add_instance_attribute('Description[256]', NBioAPI_CHAR)
    struct.add_instance_attribute('Dll[64]', NBioAPI_CHAR)
    struct.add_instance_attribute('Sys[64]', NBioAPI_CHAR)
    struct.add_instance_attribute('AutoOn', NBioAPI_UINT32)
    struct.add_instance_attribute('Brightness', NBioAPI_UINT32)
    struct.add_instance_attribute('Contrast', NBioAPI_UINT32)
    struct.add_instance_attribute('Gain', NBioAPI_UINT32)
    struct.add_instance_attribute('Reserved[8]', NBioAPI_UINT32)

    #



    mod.add_function('NBioAPI_Init',
                     pybindgen.retval(NBioAPI_RETURN),
                     [pybindgen.param(NBioAPI_HANDLE_PTR, 'phHandle', transfer_ownership=False)
                     ])

    mod.add_function('NBioAPI_Terminate',
                     pybindgen.retval(NBioAPI_RETURN),
                     [pybindgen.param(NBioAPI_HANDLE, 'hHandle')
                     ])

    mod.add_function('NBioAPI_GetValidityCode',
                     pybindgen.retval(NBioAPI_RETURN),
                     [pybindgen.param(NBioAPI_HANDLE, 'hHandle'),
                      pybindgen.param(NBioAPI_UINT32, 'Code1'),
                      pybindgen.param(NBioAPI_UINT32, 'Code2'),
                      pybindgen.param(NBioAPI_UINT32, 'Code3'),
                      pybindgen.param(NBioAPI_UINT32, 'Code4'),
                      pybindgen.param(NBioAPI_UINT32_PTR, 'pResult1', transfer_ownership=False),
                      pybindgen.param(NBioAPI_UINT32_PTR, 'pResult2', transfer_ownership=False)
                     ])

    mod.add_function('NBioAPI_GetVersion',
                     pybindgen.retval(NBioAPI_RETURN),
                     [pybindgen.param(NBioAPI_HANDLE, 'hHandle'),
                      pybindgen.param(NBioAPI_VERSION_PTR, 'pVersion', transfer_ownership=False)
                     ])

    # mod.add_function('NBioAPI_EnumerateDevice',
    # pybindgen.retval(NBioAPI_RETURN),
    #                  [pybindgen.param(NBioAPI_HANDLE, 'hHandle'),
    #                   pybindgen.param(NBioAPI_UINT32_PTR, 'pNumDevice', transfer_ownership=False),
    #                   pybindgen.param(NBioAPI_DEVICE_ID_PTR_TO_PTR, 'ppDeviceID', transfer_ownership=False)
    #                  ])

    with open(OUT_FILE_NAME, 'w') as generated_source:
        mod.generate(generated_source)


if __name__ == "__main__":
    sys.argv.insert(1, MASTER_HEADER_NAME)
    print(sys.argv)
    print('generate python whapper to on %s on %s file' % (MASTER_HEADER_NAME, OUT_FILE_NAME))
    generate_wrapper()
    with open(OUT_FILE_NAME, 'r') as generated_source:
        print(generated_source.readlines())