#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from num2words import num2words

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    num = fdp.ConsumeRegularFloat()

    try:
        num2words(num)
    except OverflowError:
        pass


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()