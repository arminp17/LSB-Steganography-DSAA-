import zlib, base64

def compress(text):
    text = text.encode("utf8")
    code =  base64.b64encode(zlib.compress(text,9))
    return code.decode("utf8")

def decompress(code):
    code.encode("utf8")
    data = zlib.decompress(base64.b64decode(code))
    return data.decode("utf8")
