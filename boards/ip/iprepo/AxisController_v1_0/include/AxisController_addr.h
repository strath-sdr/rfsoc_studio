/*
 * File Name:         hdl_prj\ipcore\AxisController_v1_0\include\AxisController_addr.h
 * Description:       C Header File
 * Created:           2021-02-09 13:59:41
*/

#ifndef AXISCONTROLLER_H_
#define AXISCONTROLLER_H_

#define  IPCore_Reset_AxisController                           0x0  //write 0x1 to bit 0 to reset IP core
#define  IPCore_Enable_AxisController                          0x4  //enabled (by default) when bit 0 is 0x1
#define  IPCore_PacketSize_AXI4_Stream_Master_AxisController   0x8  //Packet size for AXI4-Stream Master interface, the default value is 1024. The TLAST output signal of the AXI4-Stream Master interface is generated based on the packet size.
#define  IPCore_Timestamp_AxisController                       0xC  //contains unique IP timestamp (yymmddHHMM): 2102091359
#define  Enable_Data_AxisController                            0x100  //data register for Inport Enable
#define  Value_Data_AxisController                             0x104  //data register for Inport Value

#endif /* AXISCONTROLLER_H_ */
