#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from num2words import num2words

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    num = fdp.ConsumeFloatInRange(0, 10000000000000)

    try:
        num2words(num, to='currency')
    except OverflowError:
        pass


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()