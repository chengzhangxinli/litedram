from litex.gen import *

class PhySettings:
    def __init__(self, memtype, dfi_databits,
                 nphases,
                 rdphase, wrphase,
                 rdcmdphase, wrcmdphase,
                 cl, read_latency, write_latency, cwl=0):
        self.memtype = memtype
        self.dfi_databits = dfi_databits

        self.nphases = nphases
        self.rdphase = rdphase
        self.wrphase = wrphase
        self.rdcmdphase = rdcmdphase
        self.wrcmdphase = wrcmdphase

        self.cl = cl
        self.read_latency = read_latency
        self.write_latency = write_latency
        self.cwl = cwl


class GeomSettings:
    def __init__(self, bankbits, rowbits, colbits):
        self.bankbits = bankbits
        self.rowbits = rowbits
        self.colbits =  colbits
        self.addressbits = max(rowbits, colbits)


class TimingSettings:
    def __init__(self, tRP, tRCD, tWR, tWTR, tREFI, tRFC):
        self.tRP = tRP
        self.tRCD = tRCD
        self.tWR = tWR
        self.tWTR = tWTR
        self.tREFI = tREFI
        self.tRFC = tRFC


class Interface(Record):
    def __init__(self, aw, dw, nbanks, req_queue_size, read_latency, write_latency):
        self.aw = aw
        self.dw = dw
        self.nbanks = nbanks
        self.req_queue_size = req_queue_size
        self.read_latency = read_latency
        self.write_latency = write_latency

        bank_layout = [
            ("adr",      aw, DIR_M_TO_S),
            ("we",        1, DIR_M_TO_S),
            ("stb",       1, DIR_M_TO_S),
            ("req_ack",   1, DIR_S_TO_M),
            ("dat_w_ack", 1, DIR_S_TO_M),
            ("dat_r_ack", 1, DIR_S_TO_M),
            ("lock",      1, DIR_S_TO_M)
        ]
        if nbanks > 1:
            layout = [("bank"+str(i), bank_layout) for i in range(nbanks)]
        else:
            layout = bank_layout
        layout += [
            ("dat_w",     dw, DIR_M_TO_S),
            ("dat_we", dw//8, DIR_M_TO_S),
            ("dat_r",     dw, DIR_S_TO_M)
        ]
        Record.__init__(self, layout)