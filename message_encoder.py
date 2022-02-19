def message_encoder(message):
    message_blocks = []
    for ch in message:
        message_blocks.append(str(format(ord(ch),'b')))
        # print(ord(ch))
    ans = []
    for mb in message_blocks:
        while len(mb)<7:
            mb = '0' + mb
        ans.append(mb)
    return ans

def message_decoder(message_blocks):
    ans = ""
    for block in message_blocks:
        ans = ans + chr(int(block,2))
    return ans

if __name__ == "__main__":
    print(message_encoder("Aello "))
    print(message_decoder(message_encoder("Hello World")))