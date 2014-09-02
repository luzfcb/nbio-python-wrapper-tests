nbio-python-wrapper-tests
=========================

> Only for tests. Actually still does not work.

my attempts and learn to create python wrappers to access C/C++ libraries for a real application.

Is a Python extension based on the Nitgen SDK for Linux. It currently supports Nitgen fingerprint recognition devices such as Fingkey Hamster DX



The headers files `NBioAPI.h`, `NBioAPI_Basic.h`, `NBioAPI_CheckValidity.h`, `NBioAPI_Error.h`, `NBioAPI_Export.h`, `NBioAPI_ExportType.h`, `NBioAPI_ImgConv.h`, `NBioAPI_IndexSearch.h`, `NBioAPI_IndexSearchType.h`, `NBioAPI_NSearch.h`, `NBioAPI_NSearchType.h` and `NBioAPI_Type.h`, all rights reserved to Nitgen Co., Ltd.


## Usage

Install `pybindgen`

`pip install pybindgen`


Run `nbio_wrapper_generate.py`

`python nbio_wrapper_generate.py`