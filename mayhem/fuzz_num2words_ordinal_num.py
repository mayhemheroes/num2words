#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from num2words import num2words

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    num = fdp.ConsumeFloatInRange(0, sys.float_info.max)

    try:
        num2words(num, to='ordinal_num')
    except OverflowError:
        pass


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()