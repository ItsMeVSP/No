print("POLYALPHABETIC CIPHER")
c1=5
c2=9
enclist=[c1,c2,c2,c1,c2]*20
def enc(word):
    w2=""
    for i in range(0,len(word)):
        w3=chr(ord(word[i])+enclist[i])
        w2+=w3
    return w2
def dec(word):
    w2=""
    for i in range(0,len(word)):
        w3=chr(ord(word[i])-enclist[i])
        w2+=w3
    return w2
w1=input("Enter Word:").lower()
enc_wrd=enc(w1)
dec_wrd=dec(enc_wrd)
print("Encrypted String:",enc_wrd)
print("Decryption of encrypted string:",dec_wrd)
    
