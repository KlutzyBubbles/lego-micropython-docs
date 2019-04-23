#!/usr/bin/env python
import zlib, sys

if len(sys.argv) != 2:
    print("Usage: %s <zlib-compressed-file>"%sys.argv[0])
    print("Produces decompressed file with \".out\" filename suffix.")
    sys.exit(0)

indata=open(sys.argv[1], "rb").read()
indata = indata if isinstance(indata, bytes) else indata.encode('utf-8')
outdata=zlib.decompress(indata)
with open(sys.argv[1] + ".out", "wb") as f:
    f.write(outdata)
    f.close()