import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'lib'))
import openfhe

cc = openfhe.GenCryptoContext(openfhe.CCParamsCKKSRNS())
print(help(openfhe.SerializeEvalMultKey))
print(help(openfhe.DeserializeEvalMultKey))
