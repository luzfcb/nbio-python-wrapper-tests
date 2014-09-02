#ifndef _NITGEN_NBioAPI_NSEARCHTYPE_H
#define _NITGEN_NBioAPI_NSEARCHTYPE_H

#include "NBioAPI_Basic.h"

#define NBioAPI_CONF_LEVEL_LOWEST		      1
#define NBioAPI_CONF_LEVEL_LOWER		         2
#define NBioAPI_CONF_LEVEL_LOW			      3
#define NBioAPI_CONF_LEVEL_BELOW_NORMAL	   4
#define NBioAPI_CONF_LEVEL_NORMAL		      5
#define NBioAPI_CONF_LEVEL_ABOVE_NORMAL	   6
#define NBioAPI_CONF_LEVEL_HIGH			      7
#define NBioAPI_CONF_LEVEL_HIGHER		      8	
#define NBioAPI_CONF_LEVEL_HIGHEST		      9

/* NBioAPI_NSEARCH_INIT_INFO_0 */
typedef struct nbioapi_nsearch_init_info_0 {
   NBioAPI_UINT32                StructureType;           /* must be 0 */
   NBioAPI_UINT32                MaxCandidateNumber;      /* Default = 10 : for SEARCH */  
   NBioAPI_UINT32                researved0;              /* Reserved */
   NBioAPI_UINT32                researved1;              /* Reserved */
   NBioAPI_UINT32                researved2;              /* Reserved */
   NBioAPI_UINT32                researved3;              /* Reserved */
   NBioAPI_UINT32                researved4;              /* Reserved */
   NBioAPI_UINT32                researved5;              /* Reserved */
   NBioAPI_UINT32*               researved6;              /* Reserved */
} NBioAPI_NSEARCH_INIT_INFO_0, *NBioAPI_NSEARCH_INIT_INFO_PTR_0;

/* NBioAPI_NSEARCH_CANDIDATE */
typedef struct nbioapi_nsearch_candidate {
   NBioAPI_UINT32	ID;	
   NBioAPI_UINT8	FingerID;
   NBioAPI_UINT8	SampleNumber;
   NBioAPI_UINT8	ConfidenceLevel;
} NBioAPI_NSEARCH_CANDIDATE, *NBioAPI_NSEARCH_CANDIDATE_PTR;

/* NBioAPI_NSEARCH_FP_INFO */
typedef struct nbioapi_nsearch_fp_info {
   NBioAPI_UINT32	ID;	
   NBioAPI_UINT8	FingerID;  /* NBioAPI_FINGER_ID */
   NBioAPI_UINT8	SampleNumber;
} NBioAPI_NSEARCH_FP_INFO, *NBioAPI_NSEARCH_FP_INFO_PTR;

/* NBioAPI_NSEARCH_SAMPLE_INFO */
typedef struct nbioapi_nsearch_sample_info {
   NBioAPI_UINT32	ID;	
   NBioAPI_UINT8	SampleCount[11];  /* Unknown = 0, Right Thumb = 1, ... , Left Little = 10 */
} NBioAPI_NSEARCH_SAMPLE_INFO, *NBioAPI_NSEARCH_SAMPLE_INFO_PTR;

/* NBioAPI_NSEARCH_CANDIDATE_2 */
typedef struct nbioapi_nsearch_candidate_2 {
   NBioAPI_UINT32	ID;	
   NBioAPI_UINT8	FingerID;
   NBioAPI_UINT8	SampleNumber;
   NBioAPI_UINT8	ConfidenceLevel;  /* Range: 0 ~ 9 */
   NBioAPI_UINT32	ConfidenceLevelEx; /* Range: 0 ~ 9999 */
   NBioAPI_UINT32 Reserved[4];
} NBioAPI_NSEARCH_CANDIDATE_2, *NBioAPI_NSEARCH_CANDIDATE_PTR_2;

/* NBioAPI_NSEARCH_EXTENSION_INFO_0 */
typedef struct nbioapi_nsearch_extension_info_0 {
   NBioAPI_UINT32 InfoType;   // must be 0
   NBioAPI_NSEARCH_CANDIDATE_PTR_2  pCandidate2;
} NBioAPI_NSEARCH_EXTENSION_INFO_0, *NBioAPI_NSEARCH_EXTENSION_INFO_PTR_0;

typedef NBioAPI_VOID_PTR NBioAPI_NSEARCH_EXTENSION_INFO_PTR;

#endif/*_NITGEN_NBioAPI_NSEARCHTYPE_H */
