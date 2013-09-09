/* in AMD64 "long mode" all traditional opcodes stay 32bit
 * and 64bit cousins have to be encoded via REX prefixes.
 * The only exception are PUSH/POP/RET opcodes that will
 * implicitly be 64bit. This makes it so the following
 * opcode settings work in both 32bit and 64bit mode but
 * for one case: the "INCSI" bit series is dropped and used
 * for the "REX" prefix opcodes in AMD64 long mode.
 */
#		define iLOADSB   0xAC
#		define iLOADSW   0xAD
#		define iSTOSB    0xAA
#		define iSTOSW    0xAB
#		define iPUSHCX   0x51
#		define iPOPCX    0x59
#		define iINCSI    0x46
#		define iXCHGCXAX 0x91
#		define iPREFIX16 0x66
#		define iRET      0xC3
/*
 * does XCHG yield a fast register renaming on P >= P3 ?
 */
#		define PREP_1BYTE(dst)
#		define PREP_2BYTE(dst)
#		define PREP_3BYTE(dst)    { *dst++ = iPUSHCX; }
#		define PREP_4BYTE(dst)
#		define LOAD_1BYTE(dst)    {                     *dst++ = iLOADSB; }
#		define LOAD_2BYTE(dst)    { *dst++ = iPREFIX16; *dst++ = iLOADSW; }
#		define LOAD_3BYTE(dst)    {                     *dst++ = iLOADSB;   *dst++ = iXCHGCXAX; \
 		                             *dst++ = iPREFIX16; *dst++ = iLOADSW; }
#		define LOAD_4BYTE(dst)    {                     *dst++ = iLOADSW; }
#		define STORE_1BYTE(dst)   {                     *dst++ = iSTOSB; }
#		define STORE_2BYTE(dst)   { *dst++ = iPREFIX16; *dst++ = iSTOSW; }
#		define STORE_3BYTE(dst)   { *dst++ = iXCHGCXAX; *dst++ = iSTOSB;    *dst++ = iXCHGCXAX; \
									*dst++ = iPREFIX16; *dst++ = iSTOSW; }
#		define STORE_4BYTE(dst)   {                     *dst++ = iSTOSW; }
#		define RETURN_1BYTE(dst)  {                     *dst++ = iRET; }
#		define RETURN_2BYTE(dst)  {                     *dst++ = iRET; }
#		define RETURN_3BYTE(dst)  { *dst++ = iPOPCX;    *dst++ = iRET; }
#		define RETURN_4BYTE(dst)  {                     *dst++ = iRET; }
#		ifdef SDL_STRETCH_I386
#			define SKIP_1BYTE(dst)    {                     *dst++ = iINCSI; }
#			define SKIP_2BYTE(dst)    { *dst++ = iINCSI;    *dst++ = iINCSI; }
# 			define SKIP_3BYTE(dst)    { *dst++ = iINCSI;    *dst++ = iINCSI;    *dst++ = iINCSI; }
#		endif
#		define HAVE_NATIVE_CODE
