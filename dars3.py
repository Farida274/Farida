text = "가"

utf8_bytes = text.encode("utf-8")
print(utf8_bytes)

euckr_bytes = text.encode("euc-kr")
print(euckr_bytes)

print(utf8_bytes.decode("utf-8"))
print(euckr_bytes.decode("euc-kr"))
print(utf8_bytes.decode("euc-kr"))                      