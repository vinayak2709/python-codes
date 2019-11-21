def encode(input, d):
    Lfirst = input[0: d]
    Lsecond = input[d:]
    print("unique id : ", (Lsecond + Lfirst))
    return((Lsecond + Lfirst))
def decode(input, d):
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]
    print("mac ID : ", (Rsecond + Rfirst))
    return((Rsecond + Rfirst))

shift_para=4
mac_id='1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()0987654321'
print('input_mac_id=',mac_id)
i=encode(mac_id, shift_para)
k=decode(i, shift_para)
