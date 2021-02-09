/*
 * File Name:         hdl_prj\ipcore\AxisPacketGenerator_v1_0\include\AxisPacketGenerator_addr.h
 * Description:       C Header File
 * Created:           2021-02-09 12:52:42
*/

#ifndef AXISPACKETGENERATOR_H_
#define AXISPACKETGENERATOR_H_

#define  IPCore_Reset_AxisPacketGenerator       0x0  //write 0x1 to bit 0 to reset IP core
#define  IPCore_Enable_AxisPacketGenerator      0x4  //enabled (by default) when bit 0 is 0x1
#define  IPCore_Timestamp_AxisPacketGenerator   0x8  //contains unique IP timestamp (yymmddHHMM): 2102091252
#define  packet_size_Data_AxisPacketGenerator   0x100  //data register for Inport packet_size
#define  transfer_Data_AxisPacketGenerator      0x104  //data register for Inport transfer

#endif /* AXISPACKETGENERATOR_H_ */
