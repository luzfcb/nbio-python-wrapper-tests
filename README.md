nbio-python-wrapper-tests
=========================

> Only for tests. Actually still does not work.

my attempts and learn to create python wrappers to access C/C++ libraries for a real application.

Is a Python extension based on the Nitgen SDK for Linux. It currently supports Nitgen fingerprint recognition devices such as Fingkey Hamster DX


The headers files `NBioAPI.h`, `NBioAPI_Basic.h`, `NBioAPI_CheckValidity.h`, `NBioAPI_Error.h`, `NBioAPI_Export.h`, `NBioAPI_ExportType.h`, `NBioAPI_ImgConv.h`, `NBioAPI_IndexSearch.h`, `NBioAPI_IndexSearchType.h`, `NBioAPI_NSearch.h`, `NBioAPI_NSearchType.h`, `NBioAPI_Type.h`, all rights reserved to Nitgen Co., Ltd.

## First approach - Using pybindgen

### Usage

Install `pybindgen`

`pip install pybindgen`


Run `nbio_pybindgen_wrapper_generate_test.py.py`

`python nbio_pybindgen_wrapper_generate_test.py.py`

## Second approach-Using pure ctypes

### Usage

simple run `nbio_ctypes_test.py`