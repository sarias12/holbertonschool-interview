# 0x09. UTF-8 Validation

## Resources:books:
Read or watch:
* [UTF-8](https://intranet.hbtn.io/rltoken/qVyzvKu0K89D0Aiz2Ssvgw)
* [Characters, Symbols, and the Unicode Miracle](https://intranet.hbtn.io/rltoken/fZDmbf_oigBn5Ziy7ai0pg)

---

### [0. UTF-8 Validation](./0-validate_utf8.py)
Write a method that determines if a given data set represents a valid UTF-8 encoding.

* Prototype: def validUTF8(data)
* Return: True if data is a valid UTF-8 encoding, else  return False
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

## Author
* **Sergio Steben Arias Quintero** - [sarias12](https://github.com/sarias12)
