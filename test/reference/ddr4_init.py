dfii_control_sel     = 0x01
dfii_control_cke     = 0x02
dfii_control_odt     = 0x04
dfii_control_reset_n = 0x08

dfii_command_cs     = 0x01
dfii_command_we     = 0x02
dfii_command_cas    = 0x04
dfii_command_ras    = 0x08
dfii_command_wrdata = 0x10
dfii_command_rddata = 0x20

ddrx_mr1 = 0x301

init_sequence = [
    ("Release reset", 0, 0, dfii_control_odt|dfii_control_reset_n, 50000),
    ("Bring CKE high", 0, 0, dfii_control_cke|dfii_control_odt|dfii_control_reset_n, 10000),
    ("Load Mode Register 3", 0, 3, dfii_command_ras|dfii_command_cas|dfii_command_we|dfii_command_cs, 0),
    ("Load Mode Register 6", 0, 6, dfii_command_ras|dfii_command_cas|dfii_command_we|dfii_command_cs, 0),
    ("Load Mode Register 5", 1024, 5, dfii_command_ras|dfii_command_cas|dfii_command_we|dfii_command_cs, 0),
    ("Load Mode Register 4", 0, 4, dfii_command_ras|dfii_command_cas|dfii_command_we|dfii_command_cs, 0),
    ("Load Mode Register 2, CWL=9", 512, 2, dfii_command_ras|dfii_command_cas|dfii_command_we|dfii_command_cs, 0),
    ("Load Mode Register 1", 769, 1, dfii_command_ras|dfii_command_cas|dfii_command_we|dfii_command_cs, 0),
    ("Load Mode Register 0, CL=9, BL=8", 256, 0, dfii_command_ras|dfii_command_cas|dfii_command_we|dfii_command_cs, 200),
    ("ZQ Calibration", 1024, 0, dfii_command_we|dfii_command_cs, 200),
]
