#ifndef _NITGEN_NBioAPI_NSEARCH_H
#define _NITGEN_NBioAPI_NSEARCH_H

#include "NBioAPI_Basic.h"
#include "NBioAPI_Type.h"
#include "NBioAPI_NSearchType.h"
#include "NBioAPI_Error.h"

#ifdef __cplusplus
extern "C" {
#endif

#ifndef _NBioAPI_LOAD_LIBRARY

   /* NSearch Functions */
   NBioAPI_RETURN NBioAPI NBioAPI_InitNSearchEngine(NBioAPI_HANDLE hHandle);
   NBioAPI_RETURN NBioAPI NBioAPI_TerminateNSearchEngine(NBioAPI_HANDLE hHandle);

   /* Parameter Funtions */
   NBioAPI_RETURN NBioAPI NBioAPI_SetNSearchInitInfo(
                 NBioAPI_HANDLE                    hHandle,
                 NBioAPI_UINT8                     nStructureType,
                 NBioAPI_INIT_INFO_PTR             pInitInfo);
   NBioAPI_RETURN NBioAPI NBioAPI_GetNSearchInitInfo(
                 NBioAPI_HANDLE                    hHandle,
                 NBioAPI_UINT8                     nStructureType,
                 NBioAPI_INIT_INFO_PTR             pInitInfo);

   /* Add Funtion */
   NBioAPI_RETURN NBioAPI NBioAPI_AddFIRToNSearchDB(
                 NBioAPI_HANDLE                    hHandle, 
                 const NBioAPI_INPUT_FIR_PTR       pInputFIR,
                 NBioAPI_UINT32                    nUserID,
                 NBioAPI_NSEARCH_SAMPLE_INFO_PTR   pSampleInfo);

   /* Remove Functions */
   NBioAPI_RETURN NBioAPI NBioAPI_RemoveDataFromNSearchDB(
                 NBioAPI_HANDLE                    hHandle,
                 NBioAPI_NSEARCH_FP_INFO_PTR       pFpInfo);
   NBioAPI_RETURN NBioAPI NBioAPI_RemoveUserFromNSearchDB(
                 NBioAPI_HANDLE                    hHandle,
                 NBioAPI_UINT32                    nUserID);
        
   /* Searching Funtions */
   NBioAPI_RETURN NBioAPI NBioAPI_SearchDataFromNSearchDB(
                 NBioAPI_HANDLE                    hHandle, 
                 const NBioAPI_INPUT_FIR_PTR       pInputFIR,
                 NBioAPI_NSEARCH_CANDIDATE_PTR*    ppCandidate,
                 NBioAPI_VOID_PTR                  pReserved = NULL);
   NBioAPI_RETURN NBioAPI NBioAPI_FreeNSearchCandidate(
                 NBioAPI_HANDLE                    hHandle, 
                 NBioAPI_NSEARCH_CANDIDATE_PTR     pCandidate);
   NBioAPI_RETURN NBioAPI NBioAPI_FreeNSearchExtensionInfo(
                 NBioAPI_HANDLE                    hHandle,
                 NBioAPI_NSEARCH_EXTENSION_INFO_PTR pInfoExtension);
        
   NBioAPI_RETURN NBioAPI NBioAPI_IdentifyDataFromNSearchDB(
                 NBioAPI_HANDLE                    hHandle, 
                 const NBioAPI_INPUT_FIR_PTR       pInputFIR,
                 NBioAPI_FIR_SECURITY_LEVEL        nSecuLevel,
                 NBioAPI_NSEARCH_FP_INFO_PTR       pFpInfo);

   /* DB Funtions */
   NBioAPI_RETURN NBioAPI NBioAPI_ClearNSearchDB(NBioAPI_HANDLE hHandle);

   NBioAPI_RETURN NBioAPI NBioAPI_SaveNSearchDBToFile(
                 NBioAPI_HANDLE                    hHandle, 
                 const NBioAPI_CHAR*               szFilepath);
   NBioAPI_RETURN NBioAPI NBioAPI_LoadNSearchDBFromFile(
                 NBioAPI_HANDLE                    hHandle, 
                 const NBioAPI_CHAR*               szFilepath);
   NBioAPI_RETURN NBioAPI NBioAPI_ImportIndexSearchDBToNSearchDB(
                 NBioAPI_HANDLE                    hHandle, 
                 const NBioAPI_CHAR*               szFilepath);

   /* Check Functions */
   NBioAPI_RETURN NBioAPI NBioAPI_GetDataCountFromNSearchDB(
                 NBioAPI_HANDLE                    hHandle, 
                 NBioAPI_UINT32*                   pDataCount);
   NBioAPI_RETURN NBioAPI NBioAPI_CheckDataExistFromNSearchDB(
                 NBioAPI_HANDLE                    hHandle, 
                 NBioAPI_NSEARCH_FP_INFO_PTR       pFpInfo,
                 NBioAPI_BOOL*                     pExist);
   
#endif/* _NBioAPI_LOAD_LIBRARY */
   
   /* NSearch Functions */
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_InitNSearchEngine)(NBioAPI_HANDLE hHandle);
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_TerminateNSearchEngine)(NBioAPI_HANDLE hHandle);

   /* Parameter Funtions */
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_SetNSearchInitInfo)(
                 NBioAPI_HANDLE                    hHandle,
                 NBioAPI_UINT8                     nStructureType,
                 NBioAPI_INIT_INFO_PTR             pInitInfo);
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_GetNSearchInitInfo)(
                 NBioAPI_HANDLE                    hHandle,
                 NBioAPI_UINT8                     nStructureType,
                 NBioAPI_INIT_INFO_PTR             pInitInfo);

   /* Add Funtion */
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_AddFIRToNSearchDB)(
                 NBioAPI_HANDLE                    hHandle,
                 const NBioAPI_INPUT_FIR_PTR       pInputFIR,
                 NBioAPI_UINT32                    nUserID,
                 NBioAPI_NSEARCH_SAMPLE_INFO_PTR   pSampleInfo);
   
   /* Remove Functions */
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_RemoveDataFromNSearchDB)(
                 NBioAPI_HANDLE                    hHandle,
                 NBioAPI_NSEARCH_FP_INFO_PTR       pFpInfo);
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_RemoveUserFromNSearchDB)(
                 NBioAPI_HANDLE                    hHandle,
                 NBioAPI_UINT32                    nUserID);
        
   /* Searching Funtions */
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_SearchDataFromNSearchDB)(
                 NBioAPI_HANDLE                    hHandle,
                 const NBioAPI_INPUT_FIR_PTR       pInputFIR,
                 NBioAPI_NSEARCH_CANDIDATE_PTR*    ppCandidate,
                 NBioAPI_VOID_PTR                  pReserved);
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_FreeNSearchCandidate)(
                 NBioAPI_HANDLE                    hHandle,
                 NBioAPI_NSEARCH_CANDIDATE_PTR     pCandidate);
        
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_IdentifyDataFromNSearchDB)(
                 NBioAPI_HANDLE                    hHandle,
                 const NBioAPI_INPUT_FIR_PTR       pInputFIR,
                 NBioAPI_FIR_SECURITY_LEVEL        nSecuLevel,
                 NBioAPI_NSEARCH_FP_INFO_PTR       pFpInfo);

   /* DB Funtions */
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_ClearNSearchDB)(NBioAPI_HANDLE hHandle);

   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_SaveNSearchDBToFile)(
                 NBioAPI_HANDLE                    hHandle,
                 const NBioAPI_CHAR*               szFilepath);
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_LoadNSearchDBFromFile)(
                 NBioAPI_HANDLE                    hHandle,
                 const NBioAPI_CHAR*               szFilepath);
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_ImportIndexSearchDBToNSearchDB)(
                 NBioAPI_HANDLE                    hHandle,
                 const NBioAPI_CHAR*               szFilepath);

   /* Check Functions */
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_GetDataCountFromNSearchDB)(
                 NBioAPI_HANDLE                    hHandle, 
                 NBioAPI_UINT32*                   pDataCount);
   typedef NBioAPI_RETURN (NBioAPI *FP_NBioAPI_CheckDataExistFromNSearchDB)(
                 NBioAPI_HANDLE                    hHandle, 
                 NBioAPI_NSEARCH_FP_INFO_PTR       pFpInfo,
                 NBioAPI_BOOL*                     pExist);

#ifdef __cplusplus
}
#endif

#endif/* _NITGEN_NBioAPI_NSEARCH_H */
