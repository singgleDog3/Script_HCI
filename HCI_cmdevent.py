#-*- utf-8 -*-

# HCI command     // OGF == 0x01
HCI_Command_1 ={
    0x0001, 'HCI_Inquiry', # LAP(3 octets) + inquirylength(1 octets) + num_response(1 octets)
    0x0002, 'HCI_Inquiry_Cancel', # stop inquiry ---- return status --0 is success other value is fail
    0x0003, "HCI_PerInq_Mode", # maxper_leg min_per_leg, LAP, inquiry length, num_response  return status 
    0x0004, "HCI_Exit_PerInq_Mode",# return status 
    0x0005, "HCI_Create_Conn", # bd_addr, packet_type, pageScanreptiton_mode, clock_offset, allowroleswitch
    0x0006, "HCI_Disconn", #conn_handle + reason
    0x0008, "HCI_CreConnCancel", # bd_addr  return status + bd_addr
    0x0009, "HCI_AcceptConnRequest", # bd_addr + role
    0x000a, "HCI_RejectConnReq", #bd_addr + reason
    0x000b, "HCI_LinkKeyReqReply", # bd_addr + link_key   return status+ bd_addr
    0x000c, "HCI_Lin_KeyReqNegative_Reply", # bd_addr  --- return status+bd_Addr
    0x000d, "HCI_PINCodeReqReply",
    0x000e, "HCI_PINCodeReqNegativeReply",
    0x000f, "HCI_ChangeConnectionPacketType",
    0x0011, "HCI_AuthenticationRequested",
    0x0013, "HCI_SetConnectionEncryption",
    0x0015, "HCI_ChangeConnectionLinkKey",
    0x0017, "HCI_Master_Link_Key",
    0x0019, "HCI_RemoteNameRequest",
    0x001a, "HCI_RemoteNameRequestCancel",
    0x001b, "HCI_ReadRemoteSupportedFeatures",
    0x001c, "HCI_ReadRemoteExtendedFeatures",
    0x001d, "HCI_ReadRemoteVersionInformation",
    0x001f, "HCI_ReadClockOffset",
    0x0020, "HCI_Read_LMP_Handle",
    0x0028, "HCI_SetupSynchronousConnection",
    0x0029, "HCI_AcceptSynchronousConnectionRequest",
    0x002a, "HCI_RejectSynchronousConnectionRequest",
    0x002b, "HCI_IOCapabilityRequestReply",
    0x002c, "HCI_UserConfirmationRequestReply",
    0x002d, "HCI_UserConfirmationRequestNegativeReply",
    0x002e, "HCI_UserPasskeyRequestReply",
    0x002f, "HCI_UserPasskeyRequestNegativeReply",
    0x0030, "HCI_RemoteOOBDataRequestReply",
    0x0033, "HCI_RemoteOOBDataRequestNegativeReply",
    0x0034, "HCI_IOCapabilityRequestNegativeReply",
    0x0035, "HCI_CreatePhysicalLink",
    0x0036, "HCI_Accept_Physical_Link",
    0x0037, "HCI_Disconnect_Physical_Link",
    0x0038, "HCI_Create_Logical_Link",
    0x0039, "HCI_Accept_Logical_Link",
    0x003a, "HCI_Disconnect_Logical_Link",
    0x003b, "HCI_Logical_Link_Cancel",
    0x003c, "HCI_Flow_Spec_Modify",
    0x003d, "HCI_Enhanced_Setup_Synchronous_Connection",
    0x003e, "HCI_Enhanced_Accept_Synchronous_Connection_Request",
    0x003f, "HCI_Truncated_Page",
    0x0040, "HCI_Truncated_Page_Cancel",
    
    }