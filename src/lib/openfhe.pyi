# Auto-generated stub for OpenFHE Python Bindings
from typing import Any, List, Dict, Overload, Union

class BINFHE_METHOD:
    """
    Members:

    INVALID_METHOD

    AP

    GINX

    LMKCDEY
    """
    def AP(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def GINX(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def INVALID_METHOD(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def LMKCDEY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.BINFHE_METHOD, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class BINFHE_OUTPUT:
    """
    Members:

    INVALID_OUTPUT

    FRESH

    BOOTSTRAPPED

    LARGE_DIM

    SMALL_DIM
    """
    def BOOTSTRAPPED(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def FRESH(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def INVALID_OUTPUT(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def LARGE_DIM(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def SMALL_DIM(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.BINFHE_OUTPUT, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class BINFHE_PARAMSET:
    """
    Members:

    TOY

    MEDIUM

    STD128_LMKCDEY

    STD128_AP

    STD128

    STD192

    STD256

    STD128Q

    STD128Q_LMKCDEY

    STD192Q

    STD256Q

    STD128_3

    STD128_3_LMKCDEY

    STD128Q_3

    STD128Q_3_LMKCDEY

    STD192Q_3

    STD256Q_3

    STD128_4

    STD128_4_LMKCDEY

    STD128Q_4

    STD128Q_4_LMKCDEY

    STD192Q_4

    STD256Q_4

    SIGNED_MOD_TEST
    """
    def MEDIUM(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def SIGNED_MOD_TEST(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128Q(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128Q_3(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128Q_3_LMKCDEY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128Q_4(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128Q_4_LMKCDEY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128Q_LMKCDEY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128_3(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128_3_LMKCDEY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128_4(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128_4_LMKCDEY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128_AP(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD128_LMKCDEY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD192(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD192Q(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD192Q_3(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD192Q_4(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD256(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD256Q(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD256Q_3(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STD256Q_4(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def TOY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.BINFHE_PARAMSET, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class BINGATE:
    """
    Members:

    OR

    AND

    NOR

    NAND

    XOR_FAST

    XNOR_FAST

    XOR

    XNOR
    """
    def AND(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def NAND(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def NOR(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def OR(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def XNOR(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def XNOR_FAST(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def XOR(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def XOR_FAST(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.BINGATE, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class BinFHEContext:
    def BTKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        BTKeyGen(self: openfhe.BinFHEContext, sk: openfhe.LWEPrivateKey, keygenMode: openfhe.KEYGEN_MODE = <KEYGEN_MODE.SYM_ENCRYPT: 0>) -> None


        Generates bootstrapping keys.

        :param sk: The secret key.
        :type sk: LWEPrivateKey
        """
        ...

    def Bootstrap(self, *args: Any, **kwargs: Any) -> Any:
        """Bootstrap(self: openfhe.BinFHEContext, ct: openfhe.LWECiphertext, extended: bool = False) -> openfhe.LWECiphertext"""
        ...

    def ClearBTKeys(self, *args: Any, **kwargs: Any) -> Any:
        """ClearBTKeys(self: openfhe.BinFHEContext) -> None"""
        ...

    def Decrypt(self, *args: Any, **kwargs: Any) -> Any:
        """
        Decrypt(self: openfhe.BinFHEContext, sk: openfhe.LWEPrivateKey, ct: openfhe.LWECiphertext, p: typing.SupportsInt | typing.SupportsIndex = 4) -> int


        Decrypts a ciphertext using a secret key.

        :param sk: The secret key.
        :type sk: LWEPrivateKey
        :param ct: The ciphertext.
        :type ct: LWECiphertext
        :param p: Plaintext modulus (default 4).
        """
        ...

    def Encrypt(self, *args: Any, **kwargs: Any) -> Any:
        """
        Encrypt(self: openfhe.BinFHEContext, sk: openfhe.LWEPrivateKey, m: typing.SupportsInt | typing.SupportsIndex, output: openfhe.BINFHE_OUTPUT = <BINFHE_OUTPUT.BOOTSTRAPPED: 2>, p: typing.SupportsInt | typing.SupportsIndex = 4, mod: typing.SupportsInt | typing.SupportsIndex = 0) -> openfhe.LWECiphertext


        Encrypts a bit or integer using a secret key (symmetric key encryption).

        :param sk: The secret key.
        :type sk: LWEPrivateKey
        :param m: The plaintext.
        :type m: int
        :param output: FRESH to generate a fresh ciphertext, BOOTSTRAPPED to generate a refreshed ciphertext (default).
        """
        ...

    def EvalBinGate(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalBinGate(*args, **kwargs)
        Overloaded function.

        1. EvalBinGate(self: openfhe.BinFHEContext, gate: openfhe.BINGATE, ct1: openfhe.LWECiphertext, ct2: openfhe.LWECiphertext, extended: bool = False) -> openfhe.LWECiphertext


            Evaluates a binary gate (calls bootstrapping as a subroutine).

            :param gate: The gate; can be AND, OR, NAND, NOR, XOR, or XNOR.
            :type gate: BINGATE
        """
        ...

    def EvalConstant(self, *args: Any, **kwargs: Any) -> Any:
        """EvalConstant(self: openfhe.BinFHEContext, arg0: bool) -> openfhe.LWECiphertext"""
        ...

    def EvalDecomp(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalDecomp(self: openfhe.BinFHEContext, ct: openfhe.LWECiphertext) -> list[openfhe.LWECiphertext]


        Evaluate ciphertext decomposition

        :param ct: ciphertext to be bootstrapped
        :type ct: LWECiphertext
        :return: a list with the resulting ciphertexts
        :rtype: List[LWECiphertext]
        """
        ...

    def EvalFloor(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalFloor(self: openfhe.BinFHEContext, ct: openfhe.LWECiphertext, roundbits: typing.SupportsInt | typing.SupportsIndex = 0) -> openfhe.LWECiphertext


        Evaluate a round down function

        :param ct: ciphertext to be bootstrapped
        :type ct: LWECiphertext
        :param roundbits: number of bits to be rounded
        :type roundbits: int
        :return: the resulting ciphertext
        """
        ...

    def EvalFunc(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalFunc(self: openfhe.BinFHEContext, ct: openfhe.LWECiphertext, LUT: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> openfhe.LWECiphertext


        Evaluate an arbitrary function

        :param ct: ciphertext to be bootstrapped
        :type ct: LWECiphertext
        :param LUT: the look-up table of the to-be-evaluated function
        :type LUT: List[int]
        :return: the resulting ciphertext
        """
        ...

    def EvalNOT(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalNOT(self: openfhe.BinFHEContext, ct: openfhe.LWECiphertext) -> openfhe.LWECiphertext


        Evaluates the NOT gate.

        :param ct: The input ciphertext.
        :type ct: LWECiphertext
        :return: The resulting ciphertext.
        :rtype: LWECiphertext
        """
        ...

    def EvalSign(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSign(self: openfhe.BinFHEContext, ct: openfhe.LWECiphertext, schemeSwitch: bool = False) -> openfhe.LWECiphertext


        Evaluate a sign function over large precisions

        :param ct: ciphertext to be bootstrapped
        :type ct: LWECiphertext
        :param schemeSwitch: flag that indicates if it should be compatible to scheme switching
        :type schemeSwitch: bool
        :return: the resulting ciphertext
        """
        ...

    def GenerateBinFHEContext(self, *args: Any, **kwargs: Any) -> Any:
        """
        GenerateBinFHEContext(*args, **kwargs)
        Overloaded function.

        1. GenerateBinFHEContext(self: openfhe.BinFHEContext, set: openfhe.BINFHE_PARAMSET, method: openfhe.BINFHE_METHOD = <BINFHE_METHOD.GINX: 2>) -> None


            Creates a crypto context using predefined parameters sets. Recommended for most users.

            :param set: the parameter set: TOY, MEDIUM, STD128, STD192, STD256 with variants
            :type set: BINFHE_PARAMSET
        """
        ...

    def GenerateLUTviaFunction(self, *args: Any, **kwargs: Any) -> Any:
        """
        GenerateLUTviaFunction(self: openfhe.BinFHEContext, f: collections.abc.Callable, p: typing.SupportsInt | typing.SupportsIndex) -> list[int]


        Generate the LUT for the to-be-evaluated function

        :param f: the to-be-evaluated function on an integer message and a plaintext modulus
        :type f: function(int, int) -> int
        :param p: plaintext modulus
        :type p: int
        :return: the resulting ciphertext
        """
        ...

    def GetBeta(self, *args: Any, **kwargs: Any) -> Any:
        """GetBeta(self: openfhe.BinFHEContext) -> int"""
        ...

    def GetBinFHEScheme(self, *args: Any, **kwargs: Any) -> Any:
        """GetBinFHEScheme(self: openfhe.BinFHEContext) -> lbcrypto::BinFHEScheme"""
        ...

    def GetLWEScheme(self, *args: Any, **kwargs: Any) -> Any:
        """GetLWEScheme(self: openfhe.BinFHEContext) -> lbcrypto::LWEEncryptionScheme"""
        ...

    def GetMaxPlaintextSpace(self, *args: Any, **kwargs: Any) -> Any:
        """GetMaxPlaintextSpace(self: openfhe.BinFHEContext) -> int"""
        ...

    def GetParams(self, *args: Any, **kwargs: Any) -> Any:
        """GetParams(self: openfhe.BinFHEContext) -> lbcrypto::BinFHECryptoParams"""
        ...

    def GetPublicKey(self, *args: Any, **kwargs: Any) -> Any:
        """GetPublicKey(self: openfhe.BinFHEContext) -> lbcrypto::LWEPublicKeyImpl"""
        ...

    def GetRefreshKey(self, *args: Any, **kwargs: Any) -> Any:
        """GetRefreshKey(self: openfhe.BinFHEContext) -> lbcrypto::RingGSWACCKeyImpl"""
        ...

    def GetSwitchKey(self, *args: Any, **kwargs: Any) -> Any:
        """GetSwitchKey(self: openfhe.BinFHEContext) -> lbcrypto::LWESwitchingKeyImpl"""
        ...

    def Getn(self, *args: Any, **kwargs: Any) -> Any:
        """Getn(self: openfhe.BinFHEContext) -> int"""
        ...

    def Getq(self, *args: Any, **kwargs: Any) -> Any:
        """Getq(self: openfhe.BinFHEContext) -> int"""
        ...

    def KeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        KeyGen(self: openfhe.BinFHEContext) -> openfhe.LWEPrivateKey


        Generates a secret key for the main LWE scheme.

        :return: The secret key.
        :rtype: LWEPrivateKey
        """
        ...

    def KeyGenN(self, *args: Any, **kwargs: Any) -> Any:
        """KeyGenN(self: openfhe.BinFHEContext) -> openfhe.LWEPrivateKey"""
        ...

    def KeyGenPair(self, *args: Any, **kwargs: Any) -> Any:
        """KeyGenPair(self: openfhe.BinFHEContext) -> lbcrypto::LWEKeyPairImpl"""
        ...

    def LoadBinary(self, *args: Any, **kwargs: Any) -> Any:
        """LoadBinary(self: openfhe.BinFHEContext, arg0: cereal::BinaryInputArchive, arg1: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def LoadJSON(self, *args: Any, **kwargs: Any) -> Any:
        """LoadJSON(self: openfhe.BinFHEContext, arg0: cereal::JSONInputArchive, arg1: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def LoadPortableBinary(self, *args: Any, **kwargs: Any) -> Any:
        """LoadPortableBinary(self: openfhe.BinFHEContext, arg0: cereal::PortableBinaryInputArchive, arg1: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SaveBinary(self, *args: Any, **kwargs: Any) -> Any:
        """SaveBinary(self: openfhe.BinFHEContext, arg0: cereal::BinaryOutputArchive, arg1: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SaveJSON(self, *args: Any, **kwargs: Any) -> Any:
        """SaveJSON(self: openfhe.BinFHEContext, arg0: cereal::JSONOutputArchive, arg1: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SavePortableBinary(self, *args: Any, **kwargs: Any) -> Any:
        """SavePortableBinary(self: openfhe.BinFHEContext, arg0: cereal::PortableBinaryOutputArchive, arg1: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SerializedObjectName(self, *args: Any, **kwargs: Any) -> Any:
        """
        SerializedObjectName(self: openfhe.BinFHEContext) -> str


        Return the serialized object name

        :return: object name
        :rtype: std::string
        """
        ...

    def SerializedVersion(self, *args: Any, **kwargs: Any) -> Any:
        """
        SerializedVersion() -> int


        Return the serialized version number in use.

        :return: the version number
        :rtype: uint32_t
        """
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.BinFHEContext) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class CCParamsBFVRNS:
    def GetBatchSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetBatchSize(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetCKKSDataType(self, *args: Any, **kwargs: Any) -> Any:
        """GetCKKSDataType(self: openfhe.CCParamsBFVRNS) -> openfhe.CKKSDataType"""
        ...

    def GetCompositeDegree(self, *args: Any, **kwargs: Any) -> Any:
        """GetCompositeDegree(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetDecryptionNoiseMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetDecryptionNoiseMode(self: openfhe.CCParamsBFVRNS) -> openfhe.DecryptionNoiseMode"""
        ...

    def GetDesiredPrecision(self, *args: Any, **kwargs: Any) -> Any:
        """GetDesiredPrecision(self: openfhe.CCParamsBFVRNS) -> float"""
        ...

    def GetDigitSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetDigitSize(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetEncryptionTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetEncryptionTechnique(self: openfhe.CCParamsBFVRNS) -> openfhe.EncryptionTechnique"""
        ...

    def GetEvalAddCount(self, *args: Any, **kwargs: Any) -> Any:
        """GetEvalAddCount(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetExecutionMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetExecutionMode(self: openfhe.CCParamsBFVRNS) -> openfhe.ExecutionMode"""
        ...

    def GetFirstModSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetFirstModSize(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetInteractiveBootCompressionLevel(self, *args: Any, **kwargs: Any) -> Any:
        """GetInteractiveBootCompressionLevel(self: openfhe.CCParamsBFVRNS) -> openfhe.CompressionLevel"""
        ...

    def GetKeySwitchCount(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeySwitchCount(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetKeySwitchTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeySwitchTechnique(self: openfhe.CCParamsBFVRNS) -> openfhe.KeySwitchTechnique"""
        ...

    def GetMaxRelinSkDeg(self, *args: Any, **kwargs: Any) -> Any:
        """GetMaxRelinSkDeg(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetMultipartyMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetMultipartyMode(self: openfhe.CCParamsBFVRNS) -> openfhe.MultipartyMode"""
        ...

    def GetMultiplicationTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetMultiplicationTechnique(self: openfhe.CCParamsBFVRNS) -> openfhe.MultiplicationTechnique"""
        ...

    def GetMultiplicativeDepth(self, *args: Any, **kwargs: Any) -> Any:
        """GetMultiplicativeDepth(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetNoiseEstimate(self, *args: Any, **kwargs: Any) -> Any:
        """GetNoiseEstimate(self: openfhe.CCParamsBFVRNS) -> float"""
        ...

    def GetNumAdversarialQueries(self, *args: Any, **kwargs: Any) -> Any:
        """GetNumAdversarialQueries(self: openfhe.CCParamsBFVRNS) -> float"""
        ...

    def GetNumLargeDigits(self, *args: Any, **kwargs: Any) -> Any:
        """GetNumLargeDigits(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetPREMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetPREMode(self: openfhe.CCParamsBFVRNS) -> openfhe.ProxyReEncryptionMode"""
        ...

    def GetPRENumHops(self, *args: Any, **kwargs: Any) -> Any:
        """GetPRENumHops(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetPlaintextModulus(self, *args: Any, **kwargs: Any) -> Any:
        """GetPlaintextModulus(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetRegisterWordSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetRegisterWordSize(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetRingDim(self, *args: Any, **kwargs: Any) -> Any:
        """GetRingDim(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetScalingModSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetScalingModSize(self: openfhe.CCParamsBFVRNS) -> int"""
        ...

    def GetScalingTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetScalingTechnique(self: openfhe.CCParamsBFVRNS) -> openfhe.ScalingTechnique"""
        ...

    def GetScheme(self, *args: Any, **kwargs: Any) -> Any:
        """GetScheme(self: openfhe.CCParamsBFVRNS) -> openfhe.SCHEME"""
        ...

    def GetSecretKeyDist(self, *args: Any, **kwargs: Any) -> Any:
        """GetSecretKeyDist(self: openfhe.CCParamsBFVRNS) -> openfhe.SecretKeyDist"""
        ...

    def GetSecurityLevel(self, *args: Any, **kwargs: Any) -> Any:
        """GetSecurityLevel(self: openfhe.CCParamsBFVRNS) -> openfhe.SecurityLevel"""
        ...

    def GetStandardDeviation(self, *args: Any, **kwargs: Any) -> Any:
        """GetStandardDeviation(self: openfhe.CCParamsBFVRNS) -> float"""
        ...

    def GetStatisticalSecurity(self, *args: Any, **kwargs: Any) -> Any:
        """GetStatisticalSecurity(self: openfhe.CCParamsBFVRNS) -> float"""
        ...

    def SetBatchSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetBatchSize(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetCKKSDataType(self, *args: Any, **kwargs: Any) -> Any:
        """SetCKKSDataType(self: openfhe.CCParamsBFVRNS, arg0: openfhe.CKKSDataType) -> None"""
        ...

    def SetCompositeDegree(self, *args: Any, **kwargs: Any) -> Any:
        """SetCompositeDegree(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetDecryptionNoiseMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetDecryptionNoiseMode(self: openfhe.CCParamsBFVRNS, arg0: openfhe.DecryptionNoiseMode) -> None"""
        ...

    def SetDesiredPrecision(self, *args: Any, **kwargs: Any) -> Any:
        """SetDesiredPrecision(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None"""
        ...

    def SetDigitSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetDigitSize(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetEncryptionTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetEncryptionTechnique(self: openfhe.CCParamsBFVRNS, arg0: openfhe.EncryptionTechnique) -> None"""
        ...

    def SetEvalAddCount(self, *args: Any, **kwargs: Any) -> Any:
        """SetEvalAddCount(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetExecutionMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetExecutionMode(self: openfhe.CCParamsBFVRNS, arg0: openfhe.ExecutionMode) -> None"""
        ...

    def SetFirstModSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetFirstModSize(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetInteractiveBootCompressionLevel(self, *args: Any, **kwargs: Any) -> Any:
        """SetInteractiveBootCompressionLevel(self: openfhe.CCParamsBFVRNS, arg0: openfhe.CompressionLevel) -> None"""
        ...

    def SetKeySwitchCount(self, *args: Any, **kwargs: Any) -> Any:
        """SetKeySwitchCount(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetKeySwitchTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetKeySwitchTechnique(self: openfhe.CCParamsBFVRNS, arg0: openfhe.KeySwitchTechnique) -> None"""
        ...

    def SetMaxRelinSkDeg(self, *args: Any, **kwargs: Any) -> Any:
        """SetMaxRelinSkDeg(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetMultipartyMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetMultipartyMode(self: openfhe.CCParamsBFVRNS, arg0: openfhe.MultipartyMode) -> None"""
        ...

    def SetMultiplicationTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetMultiplicationTechnique(self: openfhe.CCParamsBFVRNS, arg0: openfhe.MultiplicationTechnique) -> None"""
        ...

    def SetMultiplicativeDepth(self, *args: Any, **kwargs: Any) -> Any:
        """SetMultiplicativeDepth(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetNoiseEstimate(self, *args: Any, **kwargs: Any) -> Any:
        """SetNoiseEstimate(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None"""
        ...

    def SetNumAdversarialQueries(self, *args: Any, **kwargs: Any) -> Any:
        """SetNumAdversarialQueries(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetNumLargeDigits(self, *args: Any, **kwargs: Any) -> Any:
        """SetNumLargeDigits(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetPREMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetPREMode(self: openfhe.CCParamsBFVRNS, arg0: openfhe.ProxyReEncryptionMode) -> None"""
        ...

    def SetPRENumHops(self, *args: Any, **kwargs: Any) -> Any:
        """SetPRENumHops(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetPlaintextModulus(self, *args: Any, **kwargs: Any) -> Any:
        """SetPlaintextModulus(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetRegisterWordSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetRegisterWordSize(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetRingDim(self, *args: Any, **kwargs: Any) -> Any:
        """SetRingDim(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetScalingModSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetScalingModSize(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetScalingTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetScalingTechnique(self: openfhe.CCParamsBFVRNS, arg0: openfhe.ScalingTechnique) -> None"""
        ...

    def SetSecretKeyDist(self, *args: Any, **kwargs: Any) -> Any:
        """SetSecretKeyDist(self: openfhe.CCParamsBFVRNS, arg0: openfhe.SecretKeyDist) -> None"""
        ...

    def SetSecurityLevel(self, *args: Any, **kwargs: Any) -> Any:
        """SetSecurityLevel(self: openfhe.CCParamsBFVRNS, arg0: openfhe.SecurityLevel) -> None"""
        ...

    def SetStandardDeviation(self, *args: Any, **kwargs: Any) -> Any:
        """SetStandardDeviation(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None"""
        ...

    def SetStatisticalSecurity(self, *args: Any, **kwargs: Any) -> Any:
        """SetStatisticalSecurity(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetThresholdNumOfParties(self, *args: Any, **kwargs: Any) -> Any:
        """SetThresholdNumOfParties(self: openfhe.CCParamsBFVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.CCParamsBFVRNS) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class CCParamsBGVRNS:
    def GetBatchSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetBatchSize(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetCKKSDataType(self, *args: Any, **kwargs: Any) -> Any:
        """GetCKKSDataType(self: openfhe.CCParamsBGVRNS) -> openfhe.CKKSDataType"""
        ...

    def GetCompositeDegree(self, *args: Any, **kwargs: Any) -> Any:
        """GetCompositeDegree(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetDecryptionNoiseMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetDecryptionNoiseMode(self: openfhe.CCParamsBGVRNS) -> openfhe.DecryptionNoiseMode"""
        ...

    def GetDesiredPrecision(self, *args: Any, **kwargs: Any) -> Any:
        """GetDesiredPrecision(self: openfhe.CCParamsBGVRNS) -> float"""
        ...

    def GetDigitSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetDigitSize(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetEncryptionTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetEncryptionTechnique(self: openfhe.CCParamsBGVRNS) -> openfhe.EncryptionTechnique"""
        ...

    def GetEvalAddCount(self, *args: Any, **kwargs: Any) -> Any:
        """GetEvalAddCount(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetExecutionMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetExecutionMode(self: openfhe.CCParamsBGVRNS) -> openfhe.ExecutionMode"""
        ...

    def GetFirstModSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetFirstModSize(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetInteractiveBootCompressionLevel(self, *args: Any, **kwargs: Any) -> Any:
        """GetInteractiveBootCompressionLevel(self: openfhe.CCParamsBGVRNS) -> openfhe.CompressionLevel"""
        ...

    def GetKeySwitchCount(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeySwitchCount(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetKeySwitchTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeySwitchTechnique(self: openfhe.CCParamsBGVRNS) -> openfhe.KeySwitchTechnique"""
        ...

    def GetMaxRelinSkDeg(self, *args: Any, **kwargs: Any) -> Any:
        """GetMaxRelinSkDeg(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetMultipartyMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetMultipartyMode(self: openfhe.CCParamsBGVRNS) -> openfhe.MultipartyMode"""
        ...

    def GetMultiplicationTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetMultiplicationTechnique(self: openfhe.CCParamsBGVRNS) -> openfhe.MultiplicationTechnique"""
        ...

    def GetMultiplicativeDepth(self, *args: Any, **kwargs: Any) -> Any:
        """GetMultiplicativeDepth(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetNoiseEstimate(self, *args: Any, **kwargs: Any) -> Any:
        """GetNoiseEstimate(self: openfhe.CCParamsBGVRNS) -> float"""
        ...

    def GetNumAdversarialQueries(self, *args: Any, **kwargs: Any) -> Any:
        """GetNumAdversarialQueries(self: openfhe.CCParamsBGVRNS) -> float"""
        ...

    def GetNumLargeDigits(self, *args: Any, **kwargs: Any) -> Any:
        """GetNumLargeDigits(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetPREMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetPREMode(self: openfhe.CCParamsBGVRNS) -> openfhe.ProxyReEncryptionMode"""
        ...

    def GetPRENumHops(self, *args: Any, **kwargs: Any) -> Any:
        """GetPRENumHops(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetPlaintextModulus(self, *args: Any, **kwargs: Any) -> Any:
        """GetPlaintextModulus(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetRegisterWordSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetRegisterWordSize(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetRingDim(self, *args: Any, **kwargs: Any) -> Any:
        """GetRingDim(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetScalingModSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetScalingModSize(self: openfhe.CCParamsBGVRNS) -> int"""
        ...

    def GetScalingTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetScalingTechnique(self: openfhe.CCParamsBGVRNS) -> openfhe.ScalingTechnique"""
        ...

    def GetScheme(self, *args: Any, **kwargs: Any) -> Any:
        """GetScheme(self: openfhe.CCParamsBGVRNS) -> openfhe.SCHEME"""
        ...

    def GetSecretKeyDist(self, *args: Any, **kwargs: Any) -> Any:
        """GetSecretKeyDist(self: openfhe.CCParamsBGVRNS) -> openfhe.SecretKeyDist"""
        ...

    def GetSecurityLevel(self, *args: Any, **kwargs: Any) -> Any:
        """GetSecurityLevel(self: openfhe.CCParamsBGVRNS) -> openfhe.SecurityLevel"""
        ...

    def GetStandardDeviation(self, *args: Any, **kwargs: Any) -> Any:
        """GetStandardDeviation(self: openfhe.CCParamsBGVRNS) -> float"""
        ...

    def GetStatisticalSecurity(self, *args: Any, **kwargs: Any) -> Any:
        """GetStatisticalSecurity(self: openfhe.CCParamsBGVRNS) -> float"""
        ...

    def SetBatchSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetBatchSize(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetCKKSDataType(self, *args: Any, **kwargs: Any) -> Any:
        """SetCKKSDataType(self: openfhe.CCParamsBGVRNS, arg0: openfhe.CKKSDataType) -> None"""
        ...

    def SetCompositeDegree(self, *args: Any, **kwargs: Any) -> Any:
        """SetCompositeDegree(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetDecryptionNoiseMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetDecryptionNoiseMode(self: openfhe.CCParamsBGVRNS, arg0: openfhe.DecryptionNoiseMode) -> None"""
        ...

    def SetDesiredPrecision(self, *args: Any, **kwargs: Any) -> Any:
        """SetDesiredPrecision(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None"""
        ...

    def SetDigitSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetDigitSize(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetEncryptionTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetEncryptionTechnique(self: openfhe.CCParamsBGVRNS, arg0: openfhe.EncryptionTechnique) -> None"""
        ...

    def SetEvalAddCount(self, *args: Any, **kwargs: Any) -> Any:
        """SetEvalAddCount(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetExecutionMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetExecutionMode(self: openfhe.CCParamsBGVRNS, arg0: openfhe.ExecutionMode) -> None"""
        ...

    def SetFirstModSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetFirstModSize(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetInteractiveBootCompressionLevel(self, *args: Any, **kwargs: Any) -> Any:
        """SetInteractiveBootCompressionLevel(self: openfhe.CCParamsBGVRNS, arg0: openfhe.CompressionLevel) -> None"""
        ...

    def SetKeySwitchCount(self, *args: Any, **kwargs: Any) -> Any:
        """SetKeySwitchCount(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetKeySwitchTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetKeySwitchTechnique(self: openfhe.CCParamsBGVRNS, arg0: openfhe.KeySwitchTechnique) -> None"""
        ...

    def SetMaxRelinSkDeg(self, *args: Any, **kwargs: Any) -> Any:
        """SetMaxRelinSkDeg(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetMultipartyMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetMultipartyMode(self: openfhe.CCParamsBGVRNS, arg0: openfhe.MultipartyMode) -> None"""
        ...

    def SetMultiplicationTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetMultiplicationTechnique(self: openfhe.CCParamsBGVRNS, arg0: openfhe.MultiplicationTechnique) -> None"""
        ...

    def SetMultiplicativeDepth(self, *args: Any, **kwargs: Any) -> Any:
        """SetMultiplicativeDepth(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetNoiseEstimate(self, *args: Any, **kwargs: Any) -> Any:
        """SetNoiseEstimate(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None"""
        ...

    def SetNumAdversarialQueries(self, *args: Any, **kwargs: Any) -> Any:
        """SetNumAdversarialQueries(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetNumLargeDigits(self, *args: Any, **kwargs: Any) -> Any:
        """SetNumLargeDigits(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetPREMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetPREMode(self: openfhe.CCParamsBGVRNS, arg0: openfhe.ProxyReEncryptionMode) -> None"""
        ...

    def SetPRENumHops(self, *args: Any, **kwargs: Any) -> Any:
        """SetPRENumHops(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetPlaintextModulus(self, *args: Any, **kwargs: Any) -> Any:
        """SetPlaintextModulus(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetRegisterWordSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetRegisterWordSize(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetRingDim(self, *args: Any, **kwargs: Any) -> Any:
        """SetRingDim(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetScalingModSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetScalingModSize(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetScalingTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetScalingTechnique(self: openfhe.CCParamsBGVRNS, arg0: openfhe.ScalingTechnique) -> None"""
        ...

    def SetSecretKeyDist(self, *args: Any, **kwargs: Any) -> Any:
        """SetSecretKeyDist(self: openfhe.CCParamsBGVRNS, arg0: openfhe.SecretKeyDist) -> None"""
        ...

    def SetSecurityLevel(self, *args: Any, **kwargs: Any) -> Any:
        """SetSecurityLevel(self: openfhe.CCParamsBGVRNS, arg0: openfhe.SecurityLevel) -> None"""
        ...

    def SetStandardDeviation(self, *args: Any, **kwargs: Any) -> Any:
        """SetStandardDeviation(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None"""
        ...

    def SetStatisticalSecurity(self, *args: Any, **kwargs: Any) -> Any:
        """SetStatisticalSecurity(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetThresholdNumOfParties(self, *args: Any, **kwargs: Any) -> Any:
        """SetThresholdNumOfParties(self: openfhe.CCParamsBGVRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.CCParamsBGVRNS) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class CCParamsCKKSRNS:
    def GetBatchSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetBatchSize(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetCKKSDataType(self, *args: Any, **kwargs: Any) -> Any:
        """GetCKKSDataType(self: openfhe.CCParamsCKKSRNS) -> openfhe.CKKSDataType"""
        ...

    def GetCompositeDegree(self, *args: Any, **kwargs: Any) -> Any:
        """GetCompositeDegree(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetDecryptionNoiseMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetDecryptionNoiseMode(self: openfhe.CCParamsCKKSRNS) -> openfhe.DecryptionNoiseMode"""
        ...

    def GetDesiredPrecision(self, *args: Any, **kwargs: Any) -> Any:
        """GetDesiredPrecision(self: openfhe.CCParamsCKKSRNS) -> float"""
        ...

    def GetDigitSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetDigitSize(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetEncryptionTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetEncryptionTechnique(self: openfhe.CCParamsCKKSRNS) -> openfhe.EncryptionTechnique"""
        ...

    def GetEvalAddCount(self, *args: Any, **kwargs: Any) -> Any:
        """GetEvalAddCount(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetExecutionMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetExecutionMode(self: openfhe.CCParamsCKKSRNS) -> openfhe.ExecutionMode"""
        ...

    def GetFirstModSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetFirstModSize(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetInteractiveBootCompressionLevel(self, *args: Any, **kwargs: Any) -> Any:
        """GetInteractiveBootCompressionLevel(self: openfhe.CCParamsCKKSRNS) -> openfhe.CompressionLevel"""
        ...

    def GetKeySwitchCount(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeySwitchCount(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetKeySwitchTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeySwitchTechnique(self: openfhe.CCParamsCKKSRNS) -> openfhe.KeySwitchTechnique"""
        ...

    def GetMaxRelinSkDeg(self, *args: Any, **kwargs: Any) -> Any:
        """GetMaxRelinSkDeg(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetMultipartyMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetMultipartyMode(self: openfhe.CCParamsCKKSRNS) -> openfhe.MultipartyMode"""
        ...

    def GetMultiplicationTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetMultiplicationTechnique(self: openfhe.CCParamsCKKSRNS) -> openfhe.MultiplicationTechnique"""
        ...

    def GetMultiplicativeDepth(self, *args: Any, **kwargs: Any) -> Any:
        """GetMultiplicativeDepth(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetNoiseEstimate(self, *args: Any, **kwargs: Any) -> Any:
        """GetNoiseEstimate(self: openfhe.CCParamsCKKSRNS) -> float"""
        ...

    def GetNumAdversarialQueries(self, *args: Any, **kwargs: Any) -> Any:
        """GetNumAdversarialQueries(self: openfhe.CCParamsCKKSRNS) -> float"""
        ...

    def GetNumLargeDigits(self, *args: Any, **kwargs: Any) -> Any:
        """GetNumLargeDigits(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetPREMode(self, *args: Any, **kwargs: Any) -> Any:
        """GetPREMode(self: openfhe.CCParamsCKKSRNS) -> openfhe.ProxyReEncryptionMode"""
        ...

    def GetPRENumHops(self, *args: Any, **kwargs: Any) -> Any:
        """GetPRENumHops(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetPlaintextModulus(self, *args: Any, **kwargs: Any) -> Any:
        """GetPlaintextModulus(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetRegisterWordSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetRegisterWordSize(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetRingDim(self, *args: Any, **kwargs: Any) -> Any:
        """GetRingDim(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetScalingModSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetScalingModSize(self: openfhe.CCParamsCKKSRNS) -> int"""
        ...

    def GetScalingTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetScalingTechnique(self: openfhe.CCParamsCKKSRNS) -> openfhe.ScalingTechnique"""
        ...

    def GetScheme(self, *args: Any, **kwargs: Any) -> Any:
        """GetScheme(self: openfhe.CCParamsCKKSRNS) -> openfhe.SCHEME"""
        ...

    def GetSecretKeyDist(self, *args: Any, **kwargs: Any) -> Any:
        """GetSecretKeyDist(self: openfhe.CCParamsCKKSRNS) -> openfhe.SecretKeyDist"""
        ...

    def GetSecurityLevel(self, *args: Any, **kwargs: Any) -> Any:
        """GetSecurityLevel(self: openfhe.CCParamsCKKSRNS) -> openfhe.SecurityLevel"""
        ...

    def GetStandardDeviation(self, *args: Any, **kwargs: Any) -> Any:
        """GetStandardDeviation(self: openfhe.CCParamsCKKSRNS) -> float"""
        ...

    def GetStatisticalSecurity(self, *args: Any, **kwargs: Any) -> Any:
        """GetStatisticalSecurity(self: openfhe.CCParamsCKKSRNS) -> float"""
        ...

    def SetBatchSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetBatchSize(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetCKKSDataType(self, *args: Any, **kwargs: Any) -> Any:
        """SetCKKSDataType(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.CKKSDataType) -> None"""
        ...

    def SetCompositeDegree(self, *args: Any, **kwargs: Any) -> Any:
        """SetCompositeDegree(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetDecryptionNoiseMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetDecryptionNoiseMode(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.DecryptionNoiseMode) -> None"""
        ...

    def SetDesiredPrecision(self, *args: Any, **kwargs: Any) -> Any:
        """SetDesiredPrecision(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None"""
        ...

    def SetDigitSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetDigitSize(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetEncryptionTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetEncryptionTechnique(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.EncryptionTechnique) -> None"""
        ...

    def SetEvalAddCount(self, *args: Any, **kwargs: Any) -> Any:
        """SetEvalAddCount(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetExecutionMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetExecutionMode(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.ExecutionMode) -> None"""
        ...

    def SetFirstModSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetFirstModSize(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetInteractiveBootCompressionLevel(self, *args: Any, **kwargs: Any) -> Any:
        """SetInteractiveBootCompressionLevel(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.CompressionLevel) -> None"""
        ...

    def SetKeySwitchCount(self, *args: Any, **kwargs: Any) -> Any:
        """SetKeySwitchCount(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetKeySwitchTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetKeySwitchTechnique(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.KeySwitchTechnique) -> None"""
        ...

    def SetMaxRelinSkDeg(self, *args: Any, **kwargs: Any) -> Any:
        """SetMaxRelinSkDeg(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetMultipartyMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetMultipartyMode(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.MultipartyMode) -> None"""
        ...

    def SetMultiplicationTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetMultiplicationTechnique(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.MultiplicationTechnique) -> None"""
        ...

    def SetMultiplicativeDepth(self, *args: Any, **kwargs: Any) -> Any:
        """SetMultiplicativeDepth(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetNoiseEstimate(self, *args: Any, **kwargs: Any) -> Any:
        """SetNoiseEstimate(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None"""
        ...

    def SetNumAdversarialQueries(self, *args: Any, **kwargs: Any) -> Any:
        """SetNumAdversarialQueries(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetNumLargeDigits(self, *args: Any, **kwargs: Any) -> Any:
        """SetNumLargeDigits(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetPREMode(self, *args: Any, **kwargs: Any) -> Any:
        """SetPREMode(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.ProxyReEncryptionMode) -> None"""
        ...

    def SetPRENumHops(self, *args: Any, **kwargs: Any) -> Any:
        """SetPRENumHops(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetPlaintextModulus(self, *args: Any, **kwargs: Any) -> Any:
        """SetPlaintextModulus(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetRegisterWordSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetRegisterWordSize(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetRingDim(self, *args: Any, **kwargs: Any) -> Any:
        """SetRingDim(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetScalingModSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetScalingModSize(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetScalingTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """SetScalingTechnique(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.ScalingTechnique) -> None"""
        ...

    def SetSecretKeyDist(self, *args: Any, **kwargs: Any) -> Any:
        """SetSecretKeyDist(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.SecretKeyDist) -> None"""
        ...

    def SetSecurityLevel(self, *args: Any, **kwargs: Any) -> Any:
        """SetSecurityLevel(self: openfhe.CCParamsCKKSRNS, arg0: openfhe.SecurityLevel) -> None"""
        ...

    def SetStandardDeviation(self, *args: Any, **kwargs: Any) -> Any:
        """SetStandardDeviation(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None"""
        ...

    def SetStatisticalSecurity(self, *args: Any, **kwargs: Any) -> Any:
        """SetStatisticalSecurity(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetThresholdNumOfParties(self, *args: Any, **kwargs: Any) -> Any:
        """SetThresholdNumOfParties(self: openfhe.CCParamsCKKSRNS, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.CCParamsCKKSRNS) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class CKKSDataType:
    """
    Members:

    REAL

    COMPLEX
    """
    def COMPLEX(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def REAL(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.CKKSDataType, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class Ciphertext:
    def Clone(self, *args: Any, **kwargs: Any) -> Any:
        """Clone(self: openfhe.Ciphertext) -> openfhe.Ciphertext"""
        ...

    def GetCryptoContext(self, *args: Any, **kwargs: Any) -> Any:
        """GetCryptoContext(self: openfhe.Ciphertext) -> lbcrypto::CryptoContextImpl<lbcrypto::DCRTPolyImpl<bigintdyn::mubintvec<bigintdyn::ubint<unsigned long long> > > >"""
        ...

    def GetElements(self, *args: Any, **kwargs: Any) -> Any:
        """GetElements(self: openfhe.Ciphertext) -> list[openfhe.DCRTPoly]"""
        ...

    def GetElementsMutable(self, *args: Any, **kwargs: Any) -> Any:
        """GetElementsMutable(self: openfhe.Ciphertext) -> list[openfhe.DCRTPoly]"""
        ...

    def GetEncodingType(self, *args: Any, **kwargs: Any) -> Any:
        """GetEncodingType(self: openfhe.Ciphertext) -> lbcrypto::PlaintextEncodings"""
        ...

    def GetKeyTag(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeyTag(self: openfhe.Ciphertext) -> str"""
        ...

    def GetLevel(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetLevel(self: openfhe.Ciphertext) -> int


        Get the number of scalings performed.

        :return: The level of the ciphertext.
        :rtype: int
        """
        ...

    def GetNoiseScaleDeg(self, *args: Any, **kwargs: Any) -> Any:
        """GetNoiseScaleDeg(self: openfhe.Ciphertext) -> int"""
        ...

    def GetScalingFactor(self, *args: Any, **kwargs: Any) -> Any:
        """GetScalingFactor(self: openfhe.Ciphertext) -> float"""
        ...

    def GetSlots(self, *args: Any, **kwargs: Any) -> Any:
        """GetSlots(self: openfhe.Ciphertext) -> int"""
        ...

    def RemoveElement(self, *args: Any, **kwargs: Any) -> Any:
        """
        RemoveElement(self: openfhe.Ciphertext, index: typing.SupportsInt | typing.SupportsIndex) -> None


        Remove an element from the ciphertext inner vector given its index.

        :param index: The index of the element to remove.
        :type index: int
        """
        ...

    def SetElements(self, *args: Any, **kwargs: Any) -> Any:
        """SetElements(self: openfhe.Ciphertext, arg0: collections.abc.Sequence[openfhe.DCRTPoly]) -> None"""
        ...

    def SetElementsMove(self, *args: Any, **kwargs: Any) -> Any:
        """SetElementsMove(self: openfhe.Ciphertext, arg0: collections.abc.Sequence[openfhe.DCRTPoly]) -> None"""
        ...

    def SetLevel(self, *args: Any, **kwargs: Any) -> Any:
        """
        SetLevel(self: openfhe.Ciphertext, level: typing.SupportsInt | typing.SupportsIndex) -> None


        Set the number of scalings.

        :param level: The level to set.
        :type level: int
        """
        ...

    def SetNoiseScaleDeg(self, *args: Any, **kwargs: Any) -> Any:
        """SetNoiseScaleDeg(self: openfhe.Ciphertext, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetScalingFactor(self, *args: Any, **kwargs: Any) -> Any:
        """SetScalingFactor(self: openfhe.Ciphertext, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None"""
        ...

    def SetSlots(self, *args: Any, **kwargs: Any) -> Any:
        """SetSlots(self: openfhe.Ciphertext, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.Ciphertext) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


def ClearEvalMultKeys(*args: Any, **kwargs: Any) -> Any:
    """ClearEvalMultKeys() -> None"""
    ...

class CompressionLevel:
    """
    Members:

    COMPACT

    SLACK
    """
    def COMPACT(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def SLACK(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.CompressionLevel, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class CryptoContext:
    def ClearEvalAutomorphismKeys(self, *args: Any, **kwargs: Any) -> Any:
        """
        ClearEvalAutomorphismKeys() -> None


        Flush EvalAutomorphismKey cache
        """
        ...

    def Compress(self, *args: Any, **kwargs: Any) -> Any:
        """Compress(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, towersLeft: typing.SupportsInt | typing.SupportsIndex = 1, noiseScaleDeg: typing.SupportsInt | typing.SupportsIndex = 1) -> openfhe.Ciphertext"""
        ...

    def Decrypt(self, *args: Any, **kwargs: Any) -> Any:
        """
        Decrypt(*args, **kwargs)
        Overloaded function.

        1. Decrypt(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey, ciphertext: openfhe.Ciphertext) -> openfhe.Plaintext


        Decrypt a single ciphertext into the appropriate plaintext

        :param ciphertext: ciphertext to decrypt
        :type ciphertext: Ciphertext
        """
        ...

    def DeserializeEvalAutomorphismKey(self, *args: Any, **kwargs: Any) -> Any:
        """
        DeserializeEvalAutomorphismKey(*args, **kwargs)
        Overloaded function.

        1. DeserializeEvalAutomorphismKey(filename: str, sertype: openfhe.SERBINARY) -> bool


            DeserializeEvalAutomorphismKey deserialize all keys in the serialization deserialized keys silently replace any existing matching keys deserialization will create CryptoContext if necessary

            :param filename: path for the file to deserialize from
            :type filename: str
        """
        ...

    def DeserializeEvalMultKey(self, *args: Any, **kwargs: Any) -> Any:
        """
        DeserializeEvalMultKey(*args, **kwargs)
        Overloaded function.

        1. DeserializeEvalMultKey(filename: str, sertype: openfhe.SERBINARY) -> bool


            DeserializeEvalMultKey deserialize all keys in the serialization deserialized keys silently replace any existing matching keys deserialization will create CryptoContext if necessary

            :param filename: path for the file to deserialize from
            :type filename: str
        """
        ...

    def Enable(self, *args: Any, **kwargs: Any) -> Any:
        """
        Enable(self: openfhe.CryptoContext, feature: openfhe.PKESchemeFeature) -> None


        Enable a particular feature for use with this CryptoContext

        :param feature: the feature that should be enabled. 
                        The list of available features is defined in the PKESchemeFeature enum.
        :type feature: PKESchemeFeature
        """
        ...

    def Encrypt(self, *args: Any, **kwargs: Any) -> Any:
        """
        Encrypt(*args, **kwargs)
        Overloaded function.

        1. Encrypt(self: openfhe.CryptoContext, publicKey: openfhe.PublicKey, plaintext: openfhe.Plaintext) -> openfhe.Ciphertext


            Encrypt a plaintext using a given public key

            :param plaintext: plaintext
            :type plaintext: ConstPlaintext
        """
        ...

    def EvalAdd(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalAdd(*args, **kwargs)
        Overloaded function.

        1. EvalAdd(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> openfhe.Ciphertext


        Homomorphic addition of two ciphertexts

        :param ciphertext1: first addend
        :type ciphertext1: Ciphertext
        """
        ...

    def EvalAddInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalAddInPlace(*args, **kwargs)
        Overloaded function.

        1. EvalAddInPlace(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> None


        In-place homomorphic addition of two ciphertexts

        :param ciphertext1: ciphertext1
        :type ciphertext1: Ciphertext
        """
        ...

    def EvalAddMany(self, *args: Any, **kwargs: Any) -> Any:
        """EvalAddMany(self: openfhe.CryptoContext, ciphertextVec: collections.abc.Sequence[openfhe.Ciphertext]) -> openfhe.Ciphertext"""
        ...

    def EvalAddManyInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """EvalAddManyInPlace(self: openfhe.CryptoContext, ciphertextVec: collections.abc.Sequence[openfhe.Ciphertext]) -> openfhe.Ciphertext"""
        ...

    def EvalAddMutable(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalAddMutable(*args, **kwargs)
        Overloaded function.

        1. EvalAddMutable(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> openfhe.Ciphertext


        Homomorphic addition of two mutable ciphertexts (they can be changed during the operation)

        :param ciphertext1: first addend
        :type ciphertext1: Ciphertext
        """
        ...

    def EvalAddMutableInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalAddMutableInPlace(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> None


        Homomorphic addition a mutable ciphertext and plaintext

        :param ciphertext1: first addend
        :type ciphertext1: Ciphertext
        :param ciphertext2: second addend
        :type ciphertext2: Ciphertext
        :return: ciphertext1 contains ciphertext1 + ciphertext2
        """
        ...

    def EvalAtIndex(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalAtIndex(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, index: typing.SupportsInt | typing.SupportsIndex) -> openfhe.Ciphertext


        Rotates a ciphertext by an index (positive index is a left shift, negative index is a right shift). Uses a rotation key stored in a crypto context.

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :param i: rotation index
        :type i: int
        :return: a rotated ciphertext
        """
        ...

    def EvalAtIndexKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalAtIndexKeyGen(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey, indexList: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> None


        EvalAtIndexKeyGen generates evaluation keys for a list of rotation indices

        :param privateKey: the private key
        :type privateKey: PrivateKey
        :param indexList: list of indices
        :type indexList: list
        :return: None
        """
        ...

    def EvalAutomorphism(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalAutomorphism(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, i: typing.SupportsInt | typing.SupportsIndex, evalKeyMap: openfhe.EvalKeyMap) -> openfhe.Ciphertext

        Applies an automorphism to a ciphertext using the given evaluation keys.
        """
        ...

    def EvalAutomorphismKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalAutomorphismKeyGen(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey, indexList: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> openfhe.EvalKeyMap


        Generate automophism keys for a given private key; Uses the private key for encryption

        :param privateKey: private key.
        :type privateKey: PrivateKey
        :param indexList: list of automorphism indices to be computed.
        :type indexList: list
        :return: returns the evaluation key
        """
        ...

    def EvalBootstrap(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalBootstrap(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, numIterations: typing.SupportsInt | typing.SupportsIndex = 1, precision: typing.SupportsInt | typing.SupportsIndex = 0) -> openfhe.Ciphertext


        Defines the bootstrapping evaluation of ciphertext using either the FFT-like method or the linear method

        :param ciphertext: the input ciphertext
        :type ciphertext: Ciphertext
        :param numIterations: number of iterations to run iterative bootstrapping (Meta-BTS). Increasing the iterations increases the precision of bootstrapping
        :type numIterations: int
        :param precision: precision of initial bootstrapping algorithm. This value is determined by the user experimentally by first running EvalBootstrap with numIterations = 1 and precision = 0 (unused).
        """
        ...

    def EvalBootstrapKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalBootstrapKeyGen(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey, slots: typing.SupportsInt | typing.SupportsIndex) -> None


        Generates all automorphism keys for EvalBootstrap. Supported in CKKS only. EvalBootstrapKeyGen uses the baby-step/giant-step strategy.

        :param privateKey: private key.
        :type privateKey: PrivateKey
        :param slots: number of slots to support permutations on.
        :type slots: int
        :return: None
        """
        ...

    def EvalBootstrapSetup(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalBootstrapSetup(self: openfhe.CryptoContext, levelBudget: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex] = [5, 4], dim1: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex] = [0, 0], slots: typing.SupportsInt | typing.SupportsIndex = 0, correctionFactor: typing.SupportsInt | typing.SupportsIndex = 0, precompute: bool = True, BTSlotsEncoding: bool = False) -> None


        Bootstrap functionality: There are three methods that have to be called in this specific order:

        1. EvalBootstrapSetup: computes and encodes the coefficients for encoding and decoding and stores the necessary parameters

        2. EvalBootstrapKeyGen: computes and stores the keys for rotations and conjugation

        3. EvalBootstrap: refreshes the given ciphertext Sets all parameters for both linear and FTT-like methods. Supported in CKKS only.
        """
        ...

    def EvalCKKStoFHEW(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalCKKStoFHEW(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, numCtxts: typing.SupportsInt | typing.SupportsIndex = 0) -> list[openfhe.LWECiphertext]


        Switches a CKKS ciphertext to a vector of FHEW ciphertexts.

        :param ciphertext: Input CKKS ciphertext.
        :type ciphertext: Ciphertext
        :param numCtxts: Number of coefficients to extract (defaults to number of slots if 0).
        :type numCtxts: int
        """
        ...

    def EvalCKKStoFHEWKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalCKKStoFHEWKeyGen(self: openfhe.CryptoContext, keyPair: openfhe.KeyPair, lwesk: openfhe.LWEPrivateKey) -> None


        Sets all parameters for switching from CKKS to FHEW.

        :param keyPair: CKKS key pair.
        :type keyPair: KeyPair
        :param lwesk: FHEW secret key.
        :type lwesk: LWEPrivateKey
        """
        ...

    def EvalCKKStoFHEWPrecompute(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalCKKStoFHEWPrecompute(self: openfhe.CryptoContext, scale: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> None


        Performs precomputations for CKKS homomorphic decoding. Allows setting a custom scale factor. Given as a separate method than EvalCKKStoFHEWSetup to allow the user to specify a scale that depends on the CKKS and FHEW cryptocontexts

        :param scale: Scaling factor for the linear transform matrix.
        :type scale: float
        """
        ...

    def EvalCKKStoFHEWSetup(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalCKKStoFHEWSetup(self: openfhe.CryptoContext, schswchparams: lbcrypto::SchSwchParams) -> openfhe.LWEPrivateKey


        Sets all parameters for switching from CKKS to FHEW.

        :param schswchparams: Parameters for CKKS-to-FHEW scheme switching.
        :type schswchparams: SchSwchParams
        :return: FHEW secret key.
        :rtype: LWEPrivateKey
        """
        ...

    def EvalChebyshevFunction(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalChebyshevFunction(self: openfhe.CryptoContext, func: collections.abc.Callable[[typing.SupportsFloat | typing.SupportsIndex], float], ciphertext: openfhe.Ciphertext, a: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex, degree: typing.SupportsInt | typing.SupportsIndex) -> openfhe.Ciphertext


        Method for calculating Chebyshev evaluation on a ciphertext for a smooth input function over the range [a,b]. Supported only in CKKS.

        :param func: the function to be approximated
        :type func: function
        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :param a: lower bound of argument for which the coefficients were found
        """
        ...

    def EvalChebyshevSeries(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalChebyshevSeries(*args, **kwargs)
        Overloaded function.

        1. EvalChebyshevSeries(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, coefficients: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], a: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex) -> openfhe.Ciphertext


            Method for evaluating Chebyshev polynomial interpolation; first the range [a,b] is mapped to [-1,1] using linear transformation 1 + 2 (x-a)/(b-a) If the degree of the polynomial is less than 5, use EvalChebyshevSeriesLinear (naive linear method), otherwise, use EvalChebyshevSeriesPS (Paterson-Stockmeyer method). Supported only in CKKS.

            :param ciphertext: input ciphertext
            :type ciphertext: Ciphertext
        """
        ...

    def EvalChebyshevSeriesLinear(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalChebyshevSeriesLinear(*args, **kwargs)
        Overloaded function.

        1. EvalChebyshevSeriesLinear(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, coefficients: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], a: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex) -> openfhe.Ciphertext


            Naive linear method for evaluating Chebyshev polynomial interpolation; first the range [a,b] is mapped to [-1,1] using linear transformation 1 + 2 (x-a)/(b-a). Supported only in CKKS.

            :param ciphertext: input ciphertext
            :type ciphertext: Ciphertext
        """
        ...

    def EvalChebyshevSeriesPS(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalChebyshevSeriesPS(*args, **kwargs)
        Overloaded function.

        1. EvalChebyshevSeriesPS(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, coefficients: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], a: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex) -> openfhe.Ciphertext


            Paterson-Stockmeyer method for evaluating Chebyshev polynomial interpolation; first the range [a,b] is mapped to [-1,1] using linear transformation 1 + 2 (x-a)/(b-a). Supported only in CKKS.

            :param ciphertext: input ciphertext
            :type ciphertext: Ciphertext
        """
        ...

    def EvalCompareSchemeSwitching(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalCompareSchemeSwitching(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext, numCtxts: typing.SupportsInt | typing.SupportsIndex = 0, numSlots: typing.SupportsInt | typing.SupportsIndex = 0, pLWE: typing.SupportsInt | typing.SupportsIndex = 0, scaleSign: typing.SupportsFloat | typing.SupportsIndex = 1.0, unit: bool = False) -> openfhe.Ciphertext


        Compares two CKKS ciphertexts using FHEW-based scheme switching and returns CKKS result.

        :param ciphertext1:  First input CKKS ciphertext.
        :type  ciphertext1:  Ciphertext.
        :param ciphertext2:  Second input CKKS ciphertext.
        :type  ciphertext2:  Ciphertext.
        :param numCtxts:     Number of coefficients to extract.
        """
        ...

    def EvalCompareSwitchPrecompute(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalCompareSwitchPrecompute(self: openfhe.CryptoContext, pLWE: typing.SupportsInt | typing.SupportsIndex = 0, scaleSign: typing.SupportsFloat | typing.SupportsIndex = 1.0, unit: bool = False) -> None


        Performs precomputations for scheme switching in CKKS-to-FHEW comparison. Given as a separate method than EvalSchemeSwitchingSetup to allow the user to specify a scale.

        :param pLWE:       Target plaintext modulus for FHEW ciphertexts.
        :type  pLWE:       int.
        :param scaleSign:  Scaling factor for CKKS ciphertexts before switching.
        :type  scaleSign:  float.
        :param unit:       Indicates if input messages are normalized to unit circle.
        """
        ...

    def EvalCos(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalCos(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, a: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex, degree: typing.SupportsInt | typing.SupportsIndex) -> openfhe.Ciphertext


        Evaluate approximate cosine function on a ciphertext using the Chebyshev approximation. Supported only in CKKS.

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :param a: lower bound of argument for which the coefficients were found
        :type a: float
        :param b: upper bound of argument for which the coefficients were found
        """
        ...

    def EvalDivide(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalDivide(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, a: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex, degree: typing.SupportsInt | typing.SupportsIndex) -> openfhe.Ciphertext


        Evaluate approximate division function 1/x where x >= 1 on a ciphertext using the Chebyshev approximation. Supported only in CKKS.

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :param a: lower bound of argument for which the coefficients were found
        :type a: float
        :param b: upper bound of argument for which the coefficients were found
        """
        ...

    def EvalFHEWtoCKKS(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalFHEWtoCKKS(self: openfhe.CryptoContext, LWECiphertexts: collections.abc.Sequence[openfhe.LWECiphertext], numCtxts: typing.SupportsInt | typing.SupportsIndex = 0, numSlots: typing.SupportsInt | typing.SupportsIndex = 0, p: typing.SupportsInt | typing.SupportsIndex = 4, pmin: typing.SupportsFloat | typing.SupportsIndex = 0.0, pmax: typing.SupportsFloat | typing.SupportsIndex = 2.0, dim1: typing.SupportsInt | typing.SupportsIndex = 0) -> openfhe.Ciphertext


        Switches a vector of FHEW ciphertexts to a single CKKS ciphertext.

        :param LWECiphertexts:  Input vector of FHEW ciphertexts.
        :type  LWECiphertexts:  list of LWECiphertext.
        :param numCtxts:        Number of values to encode.
        :type  numCtxts:        int
        :param numSlots:        Number of CKKS slots to use.
        """
        ...

    def EvalFHEWtoCKKSKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalFHEWtoCKKSKeyGen(self: openfhe.CryptoContext, keyPair: openfhe.KeyPair, lwesk: openfhe.LWEPrivateKey, numSlots: typing.SupportsInt | typing.SupportsIndex = 0, numCtxts: typing.SupportsInt | typing.SupportsIndex = 0, dim1: typing.SupportsInt | typing.SupportsIndex = 0, L: typing.SupportsInt | typing.SupportsIndex = 0) -> None


        Generates keys for switching from FHEW to CKKS.

        :param keyPair:   CKKS key pair.
        :type keyPair:    KeyPair
        :param lwesk:     FHEW secret key.
        :type lwesk:      LWEPrivateKey
        :param numSlots:  Number of slots for CKKS encryption.
        """
        ...

    def EvalFHEWtoCKKSSetup(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalFHEWtoCKKSSetup(self: openfhe.CryptoContext, ccLWE: openfhe.BinFHEContext, numSlotsCKKS: typing.SupportsInt | typing.SupportsIndex = 0, logQ: typing.SupportsInt | typing.SupportsIndex = 25) -> None


        Sets parameters for switching from FHEW to CKKS. Requires existing CKKS context.

        :param ccLWE: Source FHEW crypto context.
        :type ccLWE: BinFHEContext
        :param numSlotsCKKS:  Number of slots in resulting CKKS ciphertext.
        :type numSlotsCKKS: int
        :param logQ: Ciphertext modulus size in FHEW (for high precision).
        """
        ...

    def EvalFastRotation(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalFastRotation(*args, **kwargs)
        Overloaded function.

        1. EvalFastRotation(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, index: typing.SupportsInt | typing.SupportsIndex, m: typing.SupportsInt | typing.SupportsIndex, digits: openfhe.Ciphertext) -> openfhe.Ciphertext


            EvalFastRotation implements the automorphism and key switching step of hoisted automorphisms.

            Please refer to Section 5 of Halevi and Shoup, "Faster Homomorphic
            linear transformations in HELib." for more details, link:
        """
        ...

    def EvalFastRotationExt(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalFastRotationExt(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, index: typing.SupportsInt | typing.SupportsIndex, digits: openfhe.Ciphertext, addFirst: bool) -> openfhe.Ciphertext


        Only supported for hybrid key switching. Performs fast (hoisted) rotation and returns the results in the extended CRT basis P*Q

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :param index: the rotation index
        :type index: int
        :param digits: the precomputed ciphertext created by EvalFastRotationPrecompute
        """
        ...

    def EvalFastRotationPrecompute(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalFastRotationPrecompute(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        EvalFastRotationPrecompute implements the precomputation step of hoisted automorphisms.

        Please refer to Section 5 of Halevi and Shoup, "Faster Homomorphic
        linear transformations in HELib." for more details, link:
        https://eprint.iacr.org/2018/244.

        Generally, automorphisms are performed with three steps:
        """
        ...

    def EvalInnerProduct(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalInnerProduct(*args, **kwargs)
        Overloaded function.

        1. EvalInnerProduct(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext, batchSize: typing.SupportsInt | typing.SupportsIndex) -> openfhe.Ciphertext


            Evaluates inner product in packed encoding (uses EvalSum)

            :param ciphertext1: first vector
            :type ciphertext1: Ciphertext
        """
        ...

    def EvalLinearWSum(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalLinearWSum(*args, **kwargs)
        Overloaded function.

        1. EvalLinearWSum(self: openfhe.CryptoContext, ciphertextVec: collections.abc.Sequence[openfhe.Ciphertext], constantVec: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> openfhe.Ciphertext

        Evaluate a weighted sum of ciphertexts using scalar coefficients

        2. EvalLinearWSum(self: openfhe.CryptoContext, ciphertextVec: collections.abc.Sequence[openfhe.Ciphertext], constantVec: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> openfhe.Ciphertext

        Evaluate a weighted sum of ciphertexts using scalar coefficients
        """
        ...

    def EvalLinearWSumMutable(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalLinearWSumMutable(*args, **kwargs)
        Overloaded function.

        1. EvalLinearWSumMutable(self: openfhe.CryptoContext, constantsVec: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], ciphertextVec: collections.abc.Sequence[openfhe.Ciphertext]) -> openfhe.Ciphertext

        Evaluate a weighted sum (mutable version) with given coefficients

        2. EvalLinearWSumMutable(self: openfhe.CryptoContext, constantsVec: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ciphertextVec: collections.abc.Sequence[openfhe.Ciphertext]) -> openfhe.Ciphertext

        Evaluate a weighted sum (mutable version) with given coefficients
        """
        ...

    def EvalLogistic(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalLogistic(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, a: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex, degree: typing.SupportsInt | typing.SupportsIndex) -> openfhe.Ciphertext


        Evaluate approximate logistic function 1/(1 + exp(-x)) on a ciphertext using the Chebyshev approximation. Supported only in CKKS.

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :param a: lower bound of argument for which the coefficients were found
        :type a: float
        :param b: upper bound of argument for which the coefficients were found
        """
        ...

    def EvalMaxSchemeSwitching(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMaxSchemeSwitching(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, publicKey: openfhe.PublicKey, numValues: typing.SupportsInt | typing.SupportsIndex = 0, numSlots: typing.SupportsInt | typing.SupportsIndex = 0, pLWE: typing.SupportsInt | typing.SupportsIndex = 0, scaleSign: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> list[openfhe.Ciphertext]


        Computes maximum and index from the first packed values using scheme switching.

        :param ciphertext:  Input CKKS ciphertext.
        :type  ciphertext:  Ciphertext.
        :param publicKey:   CKKS public key.
        :type  publicKey:   PublicKey.
        :param numValues:   Number of values to compare (we assume that numValues is a power of two).
        """
        ...

    def EvalMaxSchemeSwitchingAlt(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMaxSchemeSwitchingAlt(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, publicKey: openfhe.PublicKey, numValues: typing.SupportsInt | typing.SupportsIndex = 0, numSlots: typing.SupportsInt | typing.SupportsIndex = 0, pLWE: typing.SupportsInt | typing.SupportsIndex = 0, scaleSign: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> list[openfhe.Ciphertext]


        Computes max and index via scheme switching, with more FHEW operations for better precision than EvalMaxSchemeSwitching.

        :param ciphertext:  Input CKKS ciphertext.
        :type  ciphertext:  Ciphertext.
        :param publicKey:   CKKS public key.
        :type  publicKey:   PublicKey.
        :param numValues:   Number of values to compare.
        """
        ...

    def EvalMerge(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMerge(self: openfhe.CryptoContext, ciphertextVec: collections.abc.Sequence[openfhe.Ciphertext]) -> openfhe.Ciphertext


        Merges multiple ciphertexts with encrypted results in slot 0 into a single ciphertext. The slot assignment is done based on the order of ciphertexts in the vector. Requires the generation of rotation keys for the indices that are needed.

        :param ciphertextVec: vector of ciphertexts to be merged.
        :type ciphertextVec: list
        :return: resulting ciphertext
        :rtype: Ciphertext
        """
        ...

    def EvalMinSchemeSwitching(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMinSchemeSwitching(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, publicKey: openfhe.PublicKey, numValues: typing.SupportsInt | typing.SupportsIndex = 0, numSlots: typing.SupportsInt | typing.SupportsIndex = 0, pLWE: typing.SupportsInt | typing.SupportsIndex = 0, scaleSign: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> list[openfhe.Ciphertext]


        Computes minimum and index of the first packed values using scheme switching.

        :param ciphertext:  Input CKKS ciphertext.
        :type  ciphertext:  Ciphertext.
        :param publicKey:   CKKS public key.
        :type  publicKey:   PublicKey.
        :param numValues:   Number of values to compare (we assume that numValues is a power of two).
        """
        ...

    def EvalMinSchemeSwitchingAlt(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMinSchemeSwitchingAlt(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, publicKey: openfhe.PublicKey, numValues: typing.SupportsInt | typing.SupportsIndex = 0, numSlots: typing.SupportsInt | typing.SupportsIndex = 0, pLWE: typing.SupportsInt | typing.SupportsIndex = 0, scaleSign: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> list[openfhe.Ciphertext]


        Computes minimum and index using more FHEW operations than CKKS with higher precision, but slower than EvalMinSchemeSwitching.

        :param ciphertext:  Input CKKS ciphertext.
        :type  ciphertext:  Ciphertext.
        :param publicKey:   CKKS public key.
        :type  publicKey:   PublicKey.
        :param numValues:   Number of packed values to compare.
        """
        ...

    def EvalMult(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMult(*args, **kwargs)
        Overloaded function.

        1. EvalMult(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> openfhe.Ciphertext


        EvalMult - OpenFHE EvalMult method for a pair of ciphertexts (uses a relinearization key from the crypto context)

        :param ciphertext1: multiplier
        :type ciphertext1: Ciphertext
        """
        ...

    def EvalMultAndRelinearize(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMultAndRelinearize(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> openfhe.Ciphertext


        Homomorphic multiplication of two ciphertexts followed by relinearization to the lowest level

        :param ciphertext1: first input ciphertext
        :type ciphertext1: Ciphertext
        :param ciphertext2: second input ciphertext
        :type ciphertext2: Ciphertext
        :return: new ciphertext
        """
        ...

    def EvalMultKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMultKeyGen(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey) -> None


        EvalMultKeyGen creates a key that can be used with the OpenFHE EvalMult operator.
        The new evaluation key is stored in cryptocontext.

        :param privateKey: the private key
        :type privateKey: PrivateKey
        """
        ...

    def EvalMultKeysGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMultKeysGen(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey) -> None


        EvalMultsKeyGen creates a vector evalmult keys that can be used with the OpenFHE EvalMult operator.
        The 1st key (for s^2) is used for multiplication of ciphertexts of depth 1.
        The 2nd key (for s^3) is used for multiplication of ciphertexts of depth 2, etc.
        A vector of new evaluation keys is stored in cryptocontext.

        :param privateKey: the private key
        :type privateKey: PrivateKey
        """
        ...

    def EvalMultMany(self, *args: Any, **kwargs: Any) -> Any:
        """EvalMultMany(self: openfhe.CryptoContext, ciphertextVec: collections.abc.Sequence[openfhe.Ciphertext]) -> openfhe.Ciphertext"""
        ...

    def EvalMultMutable(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMultMutable(*args, **kwargs)
        Overloaded function.

        1. EvalMultMutable(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> openfhe.Ciphertext


        EvalMult - OpenFHE EvalMult method for a pair of mutable ciphertexts (uses a relinearization key from the crypto context)

        :param ciphertext1: multiplier
        :type ciphertext1: Ciphertext
        """
        ...

    def EvalMultMutableInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMultMutableInPlace(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> None


        In-place EvalMult method for a pair of mutable ciphertexts (uses a relinearization key from the crypto context)

        :param ciphertext1: multiplier
        :type ciphertext1: Ciphertext
        :param ciphertext2: multiplicand
        :type ciphertext2: Ciphertext
        """
        ...

    def EvalMultNoRelin(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalMultNoRelin(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> openfhe.Ciphertext


        Homomorphic multiplication of two ciphertexts without relinearization

        :param ciphertext1: multiplier
        :type ciphertext1: Ciphertext
        :param ciphertext2: multiplicand
        :type ciphertext2: Ciphertext
        :return: new ciphertext for ciphertext1 * ciphertext2
        """
        ...

    def EvalNegate(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalNegate(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        Negates a ciphertext

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :return: new ciphertext: -ciphertext
        :rtype: Ciphertext
        """
        ...

    def EvalNegateInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalNegateInPlace(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> None


        In-place negation of a ciphertext

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        """
        ...

    def EvalPoly(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalPoly(*args, **kwargs)
        Overloaded function.

        1. EvalPoly(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, coefficients: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> openfhe.Ciphertext


            Evaluates a polynomial (given as a power series) on a ciphertext (CKKS only). Use EvalPolyLinear() for low polynomial degrees (degree < 5), or EvalPolyPS() for higher degrees.

            :param ciphertext: Input ciphertext.
            :type ciphertext: Ciphertext
        """
        ...

    def EvalPolyLinear(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalPolyLinear(*args, **kwargs)
        Overloaded function.

        1. EvalPolyLinear(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, coefficients: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> openfhe.Ciphertext


            Naive method for polynomial evaluation for polynomials represented in the power series (fast only for small-degree polynomials; less than 10). Uses a binary tree computation of the polynomial powers. Supported only in CKKS.

            :param ciphertext: input ciphertext
            :type ciphertext: Ciphertext
        """
        ...

    def EvalPolyPS(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalPolyPS(*args, **kwargs)
        Overloaded function.

        1. EvalPolyPS(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, coefficients: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> openfhe.Ciphertext


            Paterson-Stockmeyer method for evaluation for polynomials represented in the power series. Supported only in CKKS.

            :param ciphertext: input ciphertext
            :type ciphertext: Ciphertext
        """
        ...

    def EvalRotate(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalRotate(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, index: typing.SupportsInt | typing.SupportsIndex) -> openfhe.Ciphertext


        Rotates a ciphertext by an index (positive index is a left shift, negative index is a right shift). Uses a rotation key stored in a crypto context. Calls EvalAtIndex under the hood.

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :param index: rotation index
        :type index: int
        :return: a rotated ciphertext
        """
        ...

    def EvalRotateKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalRotateKeyGen(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey, indexList: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> None


        EvalRotateKeyGen generates evaluation keys for a list of indices. Calls EvalAtIndexKeyGen under the hood.

        :param privateKey: private key
        :type privateKey: PrivateKey
        :param indexList: list of integers representing the indices
        :type indexList: list
        """
        ...

    def EvalSchemeSwitchingKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSchemeSwitchingKeyGen(self: openfhe.CryptoContext, keyPair: openfhe.KeyPair, lwesk: openfhe.LWEPrivateKey) -> None


        Generates keys for switching between CKKS and FHEW.

        :param keyPair:  CKKS key pair.
        :type  keyPair:  KeyPair.
        :param lwesk:    FHEW secret key.
        :type  lwesk:    LWEPrivateKey.
        """
        ...

    def EvalSchemeSwitchingSetup(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSchemeSwitchingSetup(self: openfhe.CryptoContext, schswchparams: lbcrypto::SchSwchParams) -> openfhe.LWEPrivateKey


        Sets parameters for switching between CKKS and FHEW.

        :param schswchparams:  Scheme switching parameter object.
        :type  schswchparams:  SchSwchParams.
        :return:               FHEW secret key.
        :rtype:                LWEPrivateKey.
        """
        ...

    def EvalSin(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSin(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, a: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex, degree: typing.SupportsInt | typing.SupportsIndex) -> openfhe.Ciphertext


        Evaluate approximate sine function on a ciphertext using the Chebyshev approximation. Supported only in CKKS.

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :param a: lower bound of argument for which the coefficients were found
        :type a: float
        :param b: upper bound of argument for which the coefficients were found
        """
        ...

    def EvalSquare(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSquare(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        Efficient homomorphic squaring of a ciphertext - uses a relinearization key stored in the crypto context

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :return: squared ciphertext
        :rtype: Ciphertext
        """
        ...

    def EvalSquareInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSquareInPlace(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> None


        In-place homomorphic squaring of a mutable ciphertext - uses a relinearization key stored in the crypto context

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :return: squared ciphertext
        """
        ...

    def EvalSquareMutable(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSquareMutable(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        Efficient homomorphic squaring of a mutable ciphertext - uses a relinearization key stored in the crypto context

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :return: squared ciphertext
        :rtype: Ciphertext
        """
        ...

    def EvalSub(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSub(*args, **kwargs)
        Overloaded function.

        1. EvalSub(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> openfhe.Ciphertext


        Homomorphic subtraction of two ciphertexts

        :param ciphertext1: minuend
        :type ciphertext1: Ciphertext
        """
        ...

    def EvalSubInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSubInPlace(*args, **kwargs)
        Overloaded function.

        1. EvalSubInPlace(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> None


        In-place homomorphic subtraction of two ciphertexts

        :param ciphertext1: minuend
        :type ciphertext1: Ciphertext
        """
        ...

    def EvalSubMutable(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSubMutable(*args, **kwargs)
        Overloaded function.

        1. EvalSubMutable(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> openfhe.Ciphertext


        Homomorphic subtraction of two mutable ciphertexts

        :param ciphertext1: minuend
        :type ciphertext1: Ciphertext
        """
        ...

    def EvalSubMutableInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSubMutableInPlace(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> None


        In-place homomorphic subtraction of two mutable ciphertexts

        :param ciphertext1: minuend
        :type ciphertext1: Ciphertext
        :param ciphertext2: subtrahend
        :type ciphertext2: Ciphertext
        :return: the updated minuend
        """
        ...

    def EvalSum(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSum(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, batchSize: typing.SupportsInt | typing.SupportsIndex) -> openfhe.Ciphertext


        Function for evaluating a sum of all components in a vector.

        :param ciphertext: the input ciphertext
        :type ciphertext: Ciphertext
        :param batchSize: size of the batch
        :type batchSize: int
        :return: resulting ciphertext
        """
        ...

    def EvalSumCols(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSumCols(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, numCols: typing.SupportsInt | typing.SupportsIndex, evalSumKeyMap: openfhe.EvalKeyMap) -> openfhe.Ciphertext


        Sums all elements across each column in a packed-encoded matrix ciphertext.

        :param ciphertext: Input ciphertext.
        :type ciphertext: Ciphertext
        :param numCols: Number of columns in the matrix.
        :type numCols: int
        :param evalSumKeyMap: Map of evaluation keys generated for column summation.
        """
        ...

    def EvalSumColsKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSumColsKeyGen(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey) -> openfhe.EvalKeyMap


        Generates automorphism keys for EvalSumCols (only for packed encoding).

        :param privateKey: Private key used for key generation.
        :type privateKey: PrivateKey
        :param publicKey: Public key (used in NTRU schemes; unused now).
        :type publicKey: PublicKey
        :return: Map of generated evaluation keys.
        """
        ...

    def EvalSumKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSumKeyGen(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey) -> None


        EvalSumKeyGen Generates the key map to be used by EvalSum

        :param privateKey: private key
        :type privateKey: PrivateKey
        :return: None
        """
        ...

    def EvalSumRows(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSumRows(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, numRows: typing.SupportsInt | typing.SupportsIndex, evalSumKeyMap: openfhe.EvalKeyMap, subringDim: typing.SupportsInt | typing.SupportsIndex = 0) -> openfhe.Ciphertext


        Sums all elements across each row in a packed-encoded matrix ciphertext.

        :param ciphertext: Input ciphertext.
        :type ciphertext: Ciphertext
        :param numRows: Number of rows in the matrix.
        :type numRows: int
        :param evalSumKeyMap: Map of evaluation keys generated for row summation.
        """
        ...

    def EvalSumRowsKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        EvalSumRowsKeyGen(*args, **kwargs)
        Overloaded function.

        1. EvalSumRowsKeyGen(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey, rowSize: typing.SupportsInt | typing.SupportsIndex = 0, subringDim: typing.SupportsInt | typing.SupportsIndex = 0) -> openfhe.EvalKeyMap


            Generates automorphism keys for EvalSumRows (only for packed encoding).

            :param privateKey: Private key used for key generation.
            :type privateKey: PrivateKey
        """
        ...

    def FindAutomorphismIndex(self, *args: Any, **kwargs: Any) -> Any:
        """
        FindAutomorphismIndex(self: openfhe.CryptoContext, idx: typing.SupportsInt | typing.SupportsIndex) -> int


        Finds an automorphism index for a given vector index using a scheme-specific algorithm

        :param idx: regular vector index
        :type idx: int
        :return: the automorphism index
        :rtype: int
        """
        ...

    def FindAutomorphismIndices(self, *args: Any, **kwargs: Any) -> Any:
        """
        FindAutomorphismIndices(self: openfhe.CryptoContext, idxList: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> list[int]


        Finds automorphism indices for a given list of vector indices using a scheme-specific algorithm

        :param idxList: list of indices
        :type idxList: List[int]
        :return: a list of automorphism indices
        :rtype: List[int]
        """
        ...

    def GetBatchSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetBatchSize(self: openfhe.CryptoContext) -> int"""
        ...

    def GetBinCCForSchemeSwitch(self, *args: Any, **kwargs: Any) -> Any:
        """GetBinCCForSchemeSwitch(self: openfhe.CryptoContext) -> openfhe.BinFHEContext"""
        ...

    def GetCKKSBootCorrectionFactor(self, *args: Any, **kwargs: Any) -> Any:
        """GetCKKSBootCorrectionFactor(self: openfhe.CryptoContext) -> int"""
        ...

    def GetCKKSDataType(self, *args: Any, **kwargs: Any) -> Any:
        """GetCKKSDataType(self: openfhe.CryptoContext) -> openfhe.CKKSDataType"""
        ...

    def GetCompositeDegree(self, *args: Any, **kwargs: Any) -> Any:
        """GetCompositeDegree(self: openfhe.CryptoContext) -> int"""
        ...

    def GetCyclotomicOrder(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetCyclotomicOrder(self: openfhe.CryptoContext) -> int


        Getter for cyclotomic order

        :return: cyclotomic order
        :rtype: int
        """
        ...

    def GetDigitSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetDigitSize(self: openfhe.CryptoContext) -> int"""
        ...

    def GetEvalAddCount(self, *args: Any, **kwargs: Any) -> Any:
        """GetEvalAddCount(self: openfhe.CryptoContext) -> int"""
        ...

    def GetEvalAutomorphismKeyMap(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetEvalAutomorphismKeyMap(keyTag: str = '') -> openfhe.EvalKeyMap


        Get automorphism keys for a specific secret key tag

        :param keyId: key identifier used for private key
        :type keyId: str
        :return: EvalKeyMap: map with all automorphism keys.
        :rtype: EvalKeyMap
        """
        ...

    def GetEvalMultKeyVector(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetEvalMultKeyVector(keyTag: str = '') -> list[openfhe.EvalKey]


        Get relinearization keys for a specific secret key tag

        :param keyId: key identifier used for private key
        :type keyId: str
        :return: EvalKeyVector: vector with all relinearization keys.
        :rtype: EvalKeyVector
        """
        ...

    def GetEvalSumKeyMap(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetEvalSumKeyMap(self: openfhe.CryptoContext, keyTag: str) -> openfhe.EvalKeyMap


        Get a map of summation keys (each is composed of several automorphism keys) for a specific secret key tag
        :return: EvalKeyMap: key map
        :rtype: EvalKeyMap
        """
        ...

    def GetKeyGenLevel(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetKeyGenLevel(self: openfhe.CryptoContext) -> int


        For future use: getter for the level at which evaluation keys should be generated

        :return: The level used for key generation
        :rtype: int
        """
        ...

    def GetKeySwitchCount(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeySwitchCount(self: openfhe.CryptoContext) -> int"""
        ...

    def GetKeySwitchTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeySwitchTechnique(self: openfhe.CryptoContext) -> openfhe.KeySwitchTechnique"""
        ...

    def GetModulus(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetModulus(self: openfhe.CryptoContext) -> float


        Getter for ciphertext modulus

        :return: modulus
        :rtype: int
        """
        ...

    def GetModulusCKKS(self, *args: Any, **kwargs: Any) -> Any:
        """GetModulusCKKS(self: openfhe.CryptoContext) -> int"""
        ...

    def GetMultiplicativeDepth(self, *args: Any, **kwargs: Any) -> Any:
        """GetMultiplicativeDepth(self: openfhe.CryptoContext) -> int"""
        ...

    def GetNoiseEstimate(self, *args: Any, **kwargs: Any) -> Any:
        """GetNoiseEstimate(self: openfhe.CryptoContext) -> float"""
        ...

    def GetPRENumHops(self, *args: Any, **kwargs: Any) -> Any:
        """GetPRENumHops(self: openfhe.CryptoContext) -> int"""
        ...

    def GetPlaintextModulus(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetPlaintextModulus(self: openfhe.CryptoContext) -> int


        Get the plaintext modulus used for this context

        :return: The plaintext modulus
        :rtype: int
        """
        ...

    def GetRegisterWordSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetRegisterWordSize(self: openfhe.CryptoContext) -> int"""
        ...

    def GetRingDimension(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetRingDimension(self: openfhe.CryptoContext) -> int


        Getter for ring dimension

        :return: The ring dimension
        :rtype: int
        """
        ...

    def GetScalingFactorReal(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetScalingFactorReal(self: openfhe.CryptoContext, level: typing.SupportsInt | typing.SupportsIndex) -> float


        Method to retrieve the scaling factor of level l. For FIXEDMANUAL scaling technique method always returns 2^p, where p corresponds to plaintext modulus

        :param l:  For FLEXIBLEAUTO scaling technique the level whose scaling factor we want to learn. Levels start from 0 (no scaling done - all towers) and go up to K-1, where K is the number of towers supported.
        :type l: int
        :return: the scaling factor.
        :rtype: float
        """
        ...

    def GetScalingTechnique(self, *args: Any, **kwargs: Any) -> Any:
        """GetScalingTechnique(self: openfhe.CryptoContext) -> openfhe.ScalingTechnique"""
        ...

    def InsertEvalAutomorphismKey(self, *args: Any, **kwargs: Any) -> Any:
        """
        InsertEvalAutomorphismKey(evalKeyMap: openfhe.EvalKeyMap, keyTag: str = '') -> None


        Add the given map of keys to the map, replacing the existing map if there is one

        :param evalKeyMap: map of keys to be inserted
        :type evalKeyMap: EvalKeyMap
        :param keyTag: key identifier for the given key map
        :type keyTag: str
        """
        ...

    def InsertEvalMultKey(self, *args: Any, **kwargs: Any) -> Any:
        """
        InsertEvalMultKey(evalKeyVec: collections.abc.Sequence[openfhe.EvalKey], keyTag: str = '') -> None


        Adds the given vector of keys to the map, replacing the existing vector if there

        :param evalKeyVec: vector of keys
        :type evalKeyVec: List[EvalKey]
        """
        ...

    def InsertEvalSumKey(self, *args: Any, **kwargs: Any) -> Any:
        """
        InsertEvalSumKey(evalKeyMap: openfhe.EvalKeyMap, keyTag: str = '') -> None


        InsertEvalSumKey - add the given map of keys to the map, replacing the existing map if there

        :param evalKeyMap: key map
        :type evalKeyMap: EvalKeyMap
        """
        ...

    def IntBootAdd(self, *args: Any, **kwargs: Any) -> Any:
        """
        IntBootAdd(self: openfhe.CryptoContext, ciphertext1: openfhe.Ciphertext, ciphertext2: openfhe.Ciphertext) -> openfhe.Ciphertext


        Combines encrypted and unencrypted masked decryptions in 2-party interactive bootstrapping. It is the last step in the boostrapping.

        :param ciphertext1: Encrypted masked decryption
        :type ciphertext1: Ciphertext
        :param ciphertext2: Unencrypted masked decryption
        :type ciphertext2: Ciphertext
        :return: Refreshed ciphertext
        """
        ...

    def IntBootAdjustScale(self, *args: Any, **kwargs: Any) -> Any:
        """
        IntBootAdjustScale(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        Prepares a ciphertext for interactive bootstrapping.

        :param ciphertext: Input ciphertext
        :type ciphertext: Ciphertext
        :return: Adjusted ciphertext
        :rtype: Ciphertext
        """
        ...

    def IntBootDecrypt(self, *args: Any, **kwargs: Any) -> Any:
        """
        IntBootDecrypt(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        Performs masked decryption for interactive bootstrapping (2-party protocol).

        :param privateKey: Secret key share
        :type privateKey: PrivateKey
        :param ciphertext: Input Ciphertext
        :type ciphertext: Ciphertext
        :return: Resulting ciphertext
        """
        ...

    def IntBootEncrypt(self, *args: Any, **kwargs: Any) -> Any:
        """
        IntBootEncrypt(self: openfhe.CryptoContext, publicKey: openfhe.PublicKey, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        Encrypts Client's masked decryption for interactive bootstrapping. Increases ciphertext modulus to allow further computation. Done by Client.

        :param publicKey: Joined public key (Threshold FHE)
        :type publicKey: PublicKey
        :param ciphertext: Input Ciphertext
        :type ciphertext: Ciphertext
        :return: Resulting ciphertext
        """
        ...

    def IntMPBootAdd(self, *args: Any, **kwargs: Any) -> Any:
        """
        IntMPBootAdd(self: openfhe.CryptoContext, sharePairVec: collections.abc.Sequence[collections.abc.Sequence[openfhe.Ciphertext]]) -> list[openfhe.Ciphertext]


        Threshold FHE: Aggregates a vector of masked decryptions and re-encryotion shares, which is the second step of the interactive multiparty bootstrapping procedure.

        :param sharesPairVec: vector of pair of ciphertexts, each element of this vector contains (h_0i, h_1i) - the masked-decryption and encryption shares ofparty i
        :type sharesPairVec: List[List[Ciphertext]]
        :return: aggregated pair of shares ((h_0, h_1)
        :rtype: List[Ciphertext]
        """
        ...

    def IntMPBootAdjustScale(self, *args: Any, **kwargs: Any) -> Any:
        """
        IntMPBootAdjustScale(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        Threshold FHE: Prepare a ciphertext for Multi-Party Interactive Bootstrapping.

        :param ciphertext: Input Ciphertext
        :type ciphertext: Ciphertext
        :return: Resulting Ciphertext
        :rtype: Ciphertext
        """
        ...

    def IntMPBootDecrypt(self, *args: Any, **kwargs: Any) -> Any:
        """
        IntMPBootDecrypt(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey, ciphertext: openfhe.Ciphertext, a: openfhe.Ciphertext) -> list[openfhe.Ciphertext]


        Threshold FHE: Does masked decryption as part of Multi-Party Interactive Bootstrapping. Each party calls this function as part of the protocol

        :param privateKey: secret key share for party i
        :type privateKey: PrivateKey
        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :param a: input common random polynomial
        """
        ...

    def IntMPBootEncrypt(self, *args: Any, **kwargs: Any) -> Any:
        """
        IntMPBootEncrypt(self: openfhe.CryptoContext, publicKey: openfhe.PublicKey, sharePair: collections.abc.Sequence[openfhe.Ciphertext], a: openfhe.Ciphertext, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        Threshold FHE: Does public key encryption of lead party's masked decryption as part of interactive multi-party bootstrapping, which increases the ciphertext modulus and enables future computations. This operation is done by the lead party as the final step of interactive multi-party bootstrapping.

        :param publicKey: the lead party's public key
        :type publicKey: PublicKey
        :param sharesPair: aggregated decryption and re-encryption shares
        :type sharesPair: List[Ciphertext]
        :param a: common random ring element
        """
        ...

    def IntMPBootRandomElementGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        IntMPBootRandomElementGen(*args, **kwargs)
        Overloaded function.

        1. IntMPBootRandomElementGen(self: openfhe.CryptoContext, publicKey: openfhe.PublicKey) -> openfhe.Ciphertext


            Threshold FHE: Generate a common random polynomial for Multi-Party Interactive Bootstrapping

            :param publicKey: the scheme public key (you can also provide the lead party's public-key)
            :type publicKey: PublicKey
        """
        ...

    def KeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        KeyGen(self: openfhe.CryptoContext) -> openfhe.KeyPair


        Generates a standard public/secret key pair.

        :return: a public/secret key pair
        :rtype: KeyPair
        """
        ...

    def KeySwitchGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        KeySwitchGen(self: openfhe.CryptoContext, oldPrivateKey: openfhe.PrivateKey, newPrivateKey: openfhe.PrivateKey) -> openfhe.EvalKey


        Generates a key switching key from one secret key to another.

        :param oldPrivateKey: Original secret key.
        :type oldPrivateKey: PrivateKey
        :param newPrivateKey: Target secret key.
        :type newPrivateKey: PrivateKey
        :return: New evaluation key for key switching.
        """
        ...

    def MakeCKKSPackedPlaintext(self, *args: Any, **kwargs: Any) -> Any:
        """
        MakeCKKSPackedPlaintext(*args, **kwargs)
        Overloaded function.

        1. MakeCKKSPackedPlaintext(self: openfhe.CryptoContext, value: collections.abc.Sequence[typing.SupportsComplex | typing.SupportsFloat | typing.SupportsIndex], noiseScaleDeg: typing.SupportsInt | typing.SupportsIndex = 1, level: typing.SupportsInt | typing.SupportsIndex = 0, params: openfhe.ParmType = None, slots: typing.SupportsInt | typing.SupportsIndex = 0) -> openfhe.Plaintext


            COMPLEX ARITHMETIC IS NOT AVAILABLE, AND THIS METHOD BE DEPRECATED. USE THE REAL-NUMBER METHOD INSTEAD. MakeCKKSPackedPlaintext constructs a CKKSPackedEncoding in this context from a vector of complex numbers

            :param value: input vector of complex numbers
            :type value: List[complex]
        """
        ...

    def MakeCoefPackedPlaintext(self, *args: Any, **kwargs: Any) -> Any:
        """
        MakeCoefPackedPlaintext(self: openfhe.CryptoContext, value: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], noiseScaleDeg : typing.SupportsInt | typing.SupportsIndex = 1, level: typing.SupportsInt | typing.SupportsIndex = 0) -> openfhe.Plaintext


        MakeCoefPackedPlaintext constructs a CoefPackedEncoding in this context

        :param value: vector of signed integers mod t
        :type value: List[int]
        :param noiseScaleDeg: is degree of the scaling factor to encode the plaintext at
        :type noiseScaleDeg: int
        :param level: is the level to encode the plaintext at
        """
        ...

    def MakePackedPlaintext(self, *args: Any, **kwargs: Any) -> Any:
        """
        MakePackedPlaintext(self: openfhe.CryptoContext, value: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], noiseScaleDeg: typing.SupportsInt | typing.SupportsIndex = 1, level: typing.SupportsInt | typing.SupportsIndex = 0) -> openfhe.Plaintext


        MakePackedPlaintext constructs a PackedEncoding in this context

        :param value: vector of signed integers mod t
        :type value: List[int]
        :param noiseScaleDeg: is degree of the scaling factor to encode the plaintext at
        :type noiseScaleDeg: int
        :param level: is the level to encode the plaintext at
        """
        ...

    def MakeStringPlaintext(self, *args: Any, **kwargs: Any) -> Any:
        """
        MakeStringPlaintext(self: openfhe.CryptoContext, str: str) -> openfhe.Plaintext


        MakeStringPlaintext constructs a StringEncoding in this context.

        :param str: string to be encoded
        :type str: str
        :return: plaintext
        """
        ...

    def ModReduce(self, *args: Any, **kwargs: Any) -> Any:
        """
        ModReduce(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        ModReduce - OpenFHE ModReduce method used only for BGV/CKKS.

        :param ciphertext: ciphertext
        :type ciphertext: Ciphertext
        :return: Ciphertext: mod reduced ciphertext
        :rtype: Ciphertext
        """
        ...

    def ModReduceInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """
        ModReduceInPlace(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> None


        ModReduce - OpenFHE ModReduceInPlace method used only for BGV/CKKS.

        :param ciphertext: ciphertext to be mod-reduced in-place
        :type ciphertext: Ciphertext
        """
        ...

    def MultiAddEvalAutomorphismKeys(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultiAddEvalAutomorphismKeys(self: openfhe.CryptoContext, evalKeyMap1: openfhe.EvalKeyMap, evalKeyMap2: openfhe.EvalKeyMap, keyTag: str = '') -> openfhe.EvalKeyMap


        Threshold FHE: Adds two prior evaluation key sets for automorphisms

        :param evalKeyMap1: first automorphism key set
        :type evalKeyMap1: EvalKeyMap
        :param evalKeyMap2: second automorphism key set
        :type evalKeyMap2: EvalKeyMap
        :param keyId: new key identifier used for resulting evaluation key
        """
        ...

    def MultiAddEvalKeys(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultiAddEvalKeys(self: openfhe.CryptoContext, evalKey1: openfhe.EvalKey, evalKey2: openfhe.EvalKey, keyTag: str = '') -> openfhe.EvalKey


        Threshold FHE: Adds two prior evaluation keys

        :param evalKey1: first evaluation key
        :type evalKey1: EvalKey
        :param evalKey2: second evaluation key
        :type evalKey2: EvalKey
        :param keyId: new key identifier used for resulting evaluation key
        """
        ...

    def MultiAddEvalMultKeys(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultiAddEvalMultKeys(self: openfhe.CryptoContext, evalKey1: openfhe.EvalKey, evalKey2: openfhe.EvalKey, keyTag: str = '') -> openfhe.EvalKey


        Threshold FHE: Adds two prior evaluation key sets for summation

        :param evalKey1: first evaluation key
        :type evalKey1: EvalKey
        :param evalKey2: second evaluation key
        :type evalKey2: EvalKey
        :param keyId: new key identifier used for resulting evaluation key
        """
        ...

    def MultiAddEvalSumKeys(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultiAddEvalSumKeys(self: openfhe.CryptoContext, evalKeyMap1: openfhe.EvalKeyMap, evalKeyMap2: openfhe.EvalKeyMap, keyTag: str = '') -> openfhe.EvalKeyMap


        Threshold FHE: Adds two prior evaluation key sets for summation

        :param evalKeyMap1: first summation key set
        :type evalKeyMap1: EvalKeyMap
        :param evalKeyMap2: second summation key set
        :type evalKeyMap2: EvalKeyMap
        :param keyId: new key identifier used for resulting evaluation key
        """
        ...

    def MultiAddPubKeys(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultiAddPubKeys(self: openfhe.CryptoContext, publicKey1: openfhe.PublicKey, publicKey2: openfhe.PublicKey, keyTag: str = '') -> openfhe.PublicKey


        Threshold FHE: Adds two prior public keys

        :param publicKey1: first public key
        :type publicKey1: PublicKey
        :param publicKey2: second public key
        :type publicKey2: PublicKey
        :param keyId: new key identifier used for the resulting key
        """
        ...

    def MultiEvalAtIndexKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultiEvalAtIndexKeyGen(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey, evalKeyMap: openfhe.EvalKeyMap, indexList: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], keyTag: str = '') -> openfhe.EvalKeyMap


        Threshold FHE: Generates joined rotation keys from the current secret key and prior joined rotation keys

        :param privateKey: secret key share
        :type privateKey: PrivateKey
        :param evalKeyMap: a map with prior joined rotation keys
        :type evalKeyMap: EvalKeyMap
        :param indexList: a vector of rotation indices
        """
        ...

    def MultiEvalSumKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultiEvalSumKeyGen(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey, evalKeyMap: openfhe.EvalKeyMap, keyTag: str = '') -> openfhe.EvalKeyMap


        Threshold FHE: Generates joined summation evaluation keys from the current secret share and prior joined summation keys

        :param privateKey: secret key share
        :type privateKey: PrivateKey
        :param evalKeyMap: a map with prior joined summation keys
        :type evalKeyMap: EvalKeyMap
        :param keyId: new key identifier used for resulting evaluation key
        """
        ...

    def MultiKeySwitchGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultiKeySwitchGen(self: openfhe.CryptoContext, originalPrivateKey: openfhe.PrivateKey, newPrivateKey: openfhe.PrivateKey, evalKey: openfhe.EvalKey) -> openfhe.EvalKey


        Threshold FHE: Generates a joined evaluation key from the current secret share and a prior joined evaluation key

        :param originalPrivateKey: secret key transformed from.
        :type originalPrivateKey: PrivateKey
        :param newPrivateKey: secret key transformed from.
        :type newPrivateKey: PrivateKey
        :param evalKey: the prior joined evaluation key.
        """
        ...

    def MultiMultEvalKey(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultiMultEvalKey(self: openfhe.CryptoContext, privateKey: openfhe.PrivateKey, evalKey: openfhe.EvalKey, keyTag: str = '') -> openfhe.EvalKey


        Threshold FHE: Generates a partial evaluation key for homomorphic multiplication based on the current secret share and an existing partial evaluation key

        :param privateKey: current secret share
        :type privateKey: PrivateKey
        :param evalKey: prior evaluation key
        :type evalKey: EvalKey
        :param keyId: new key identifier used for resulting evaluation key
        """
        ...

    def MultipartyDecryptFusion(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultipartyDecryptFusion(self: openfhe.CryptoContext, partialCiphertextVec: collections.abc.Sequence[openfhe.Ciphertext]) -> openfhe.Plaintext


        Threshold FHE: Method for combining the partially decrypted ciphertexts and getting the final decryption in the clear.

        :param partialCiphertextVec: list of "partial" decryptions
        :type partialCiphertextVec: list
        :return: Plaintext: resulting plaintext
        :rtype: Plaintext
        """
        ...

    def MultipartyDecryptLead(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultipartyDecryptLead(self: openfhe.CryptoContext, ciphertextVec: collections.abc.Sequence[openfhe.Ciphertext], privateKey: openfhe.PrivateKey) -> list[openfhe.Ciphertext]


        Threshold FHE: Method for decryption operation run by the lead decryption client

        :param ciphertextVec: a list of ciphertexts
        :type ciphertextVec: list
        :param privateKey:  secret key share used for decryption.
        :type privateKey: PrivateKey
        :return: list of partially decrypted ciphertexts.
        """
        ...

    def MultipartyDecryptMain(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultipartyDecryptMain(self: openfhe.CryptoContext, ciphertextVec: collections.abc.Sequence[openfhe.Ciphertext], privateKey: openfhe.PrivateKey) -> list[openfhe.Ciphertext]


        Threshold FHE: "Partial" decryption computed by all parties except for the lead one

        :param ciphertextVec: a list of ciphertexts
        :type ciphertextVec: list
        :param privateKey:  secret key share used for decryption.
        :type privateKey: PrivateKey
        :return: list of partially decrypted ciphertexts.
        """
        ...

    def MultipartyKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        MultipartyKeyGen(*args, **kwargs)
        Overloaded function.

        1. MultipartyKeyGen(self: openfhe.CryptoContext, publicKey: openfhe.PublicKey, makeSparse: bool = False, fresh: bool = False) -> openfhe.KeyPair


            Threshold FHE: Generation of a public key derived from a previous joined public key (for prior secret shares) and the secret key share of the current party.

            :param publicKey:  joined public key from prior parties.
            :type publicKey: PublicKey
        """
        ...

    def ReEncrypt(self, *args: Any, **kwargs: Any) -> Any:
        """
        ReEncrypt(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext, evalKey: openfhe.EvalKey, publicKey: openfhe.PublicKey = None) -> openfhe.Ciphertext


        ReEncrypt - Proxy Re-Encryption mechanism for OpenFHE

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :param evalKey: evaluation key for PRE keygen method
        :type evalKey: EvalKey
        :param publicKey: the public key of the recipient of the reencrypted ciphertext
        """
        ...

    def ReKeyGen(self, *args: Any, **kwargs: Any) -> Any:
        """
        ReKeyGen(self: openfhe.CryptoContext, oldPrivateKey: openfhe.PrivateKey, newPublicKey: openfhe.PublicKey) -> openfhe.EvalKey


        ReKeyGen produces an Eval Key that OpenFHE can use for Proxy Re-Encryption

        :param oldPrivateKey: original private key
        :type privateKey: PrivateKey
        :param newPublicKey: public key
        :type publicKey: PublicKey
        :return: new evaluation key
        """
        ...

    def Relinearize(self, *args: Any, **kwargs: Any) -> Any:
        """
        Relinearize(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        Homomorphic multiplication of two ciphertexts withour relinearization

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        :return: relinearized ciphertext
        :rtype: Ciphertext
        """
        ...

    def RelinearizeInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """
        RelinearizeInPlace(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> None


        In-place relinearization of a ciphertext to the lowest level (with 2 polynomials per ciphertext).

        :param ciphertext: input ciphertext
        :type ciphertext: Ciphertext
        """
        ...

    def Rescale(self, *args: Any, **kwargs: Any) -> Any:
        """
        Rescale(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> openfhe.Ciphertext


        Rescale - An alias for OpenFHE ModReduce method. This is because ModReduce is called Rescale in CKKS.

        :param ciphertext: ciphertext
        :type ciphertext: Ciphertext
        :return: Ciphertext: rescaled ciphertext
        :rtype: Ciphertext
        """
        ...

    def RescaleInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """
        RescaleInPlace(self: openfhe.CryptoContext, ciphertext: openfhe.Ciphertext) -> None


        Rescale - An alias for OpenFHE ModReduceInPlace method. This is because ModReduceInPlace is called RescaleInPlace in CKKS.

        :param ciphertext:  ciphertext to be rescaled in-place
        :type ciphertext: Ciphertext
        """
        ...

    def SerializeEvalAutomorphismKey(self, *args: Any, **kwargs: Any) -> Any:
        """
        SerializeEvalAutomorphismKey(*args, **kwargs)
        Overloaded function.

        1. SerializeEvalAutomorphismKey(filename: str, sertype: openfhe.SERBINARY, keyTag: str = '') -> bool


            SerializeEvalAutomorphismKey for a single EvalAuto key or all of the EvalAuto keys

            :param filename: output file
            :type filename: str
        """
        ...

    def SerializeEvalMultKey(self, *args: Any, **kwargs: Any) -> Any:
        """
        SerializeEvalMultKey(*args, **kwargs)
        Overloaded function.

        1. SerializeEvalMultKey(filename: str, sertype: openfhe.SERBINARY, keyTag: str = '') -> bool


            SerializeEvalMultKey for a single EvalMult key or all of the EvalMult keys

            :param filename: output file to serialize to
            :type filename: str
        """
        ...

    def SetCKKSBootCorrectionFactor(self, *args: Any, **kwargs: Any) -> Any:
        """SetCKKSBootCorrectionFactor(self: openfhe.CryptoContext, cf: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetEvalAddCount(self, *args: Any, **kwargs: Any) -> Any:
        """SetEvalAddCount(self: openfhe.CryptoContext, evalAddCount: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetKeyGenLevel(self, *args: Any, **kwargs: Any) -> Any:
        """
        SetKeyGenLevel(self: openfhe.CryptoContext, level: typing.SupportsInt | typing.SupportsIndex) -> None


        For future use: setter for the level at which evaluation keys should be generated

        :param level: the level to set the key generation to
        :type level: int
        """
        ...

    def SetKeySwitchCount(self, *args: Any, **kwargs: Any) -> Any:
        """SetKeySwitchCount(self: openfhe.CryptoContext, keySwitchCount: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetMultiplicativeDepth(self, *args: Any, **kwargs: Any) -> Any:
        """SetMultiplicativeDepth(self: openfhe.CryptoContext, multiplicativeDepth: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetNoiseEstimate(self, *args: Any, **kwargs: Any) -> Any:
        """SetNoiseEstimate(self: openfhe.CryptoContext, noiseEstimate: typing.SupportsFloat | typing.SupportsIndex) -> None"""
        ...

    def SetPRENumHops(self, *args: Any, **kwargs: Any) -> Any:
        """SetPRENumHops(self: openfhe.CryptoContext, PRENumHops: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.CryptoContext) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def get_ptr(self, *args: Any, **kwargs: Any) -> Any:
        """get_ptr(self: openfhe.CryptoContext) -> None"""
        ...


class DCRTPoly:
    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.DCRTPoly) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class DecryptionNoiseMode:
    """
    Members:

    FIXED_NOISE_DECRYPT

    NOISE_FLOODING_DECRYPT
    """
    def FIXED_NOISE_DECRYPT(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def NOISE_FLOODING_DECRYPT(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.DecryptionNoiseMode, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


def DeserializeCiphertext(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializeCiphertext(*args, **kwargs)
    Overloaded function.

    1. DeserializeCiphertext(filename: str, sertype: openfhe.SERJSON) -> tuple[openfhe.Ciphertext, bool]

    2. DeserializeCiphertext(filename: str, sertype: openfhe.SERBINARY) -> tuple[openfhe.Ciphertext, bool]
    """
    ...

def DeserializeCiphertextString(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializeCiphertextString(*args, **kwargs)
    Overloaded function.

    1. DeserializeCiphertextString(str: str, sertype: openfhe.SERJSON) -> openfhe.Ciphertext

    2. DeserializeCiphertextString(str: bytes, sertype: openfhe.SERBINARY) -> openfhe.Ciphertext
    """
    ...

def DeserializeCryptoContext(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializeCryptoContext(*args, **kwargs)
    Overloaded function.

    1. DeserializeCryptoContext(filename: str, sertype: openfhe.SERJSON) -> tuple[openfhe.CryptoContext, bool]

    2. DeserializeCryptoContext(filename: str, sertype: openfhe.SERBINARY) -> tuple[openfhe.CryptoContext, bool]
    """
    ...

def DeserializeCryptoContextString(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializeCryptoContextString(*args, **kwargs)
    Overloaded function.

    1. DeserializeCryptoContextString(str: str, sertype: openfhe.SERJSON) -> openfhe.CryptoContext

    2. DeserializeCryptoContextString(str: bytes, sertype: openfhe.SERBINARY) -> openfhe.CryptoContext
    """
    ...

def DeserializeEvalAutomorphismKeyString(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializeEvalAutomorphismKeyString(*args, **kwargs)
    Overloaded function.

    1. DeserializeEvalAutomorphismKeyString(data: str, sertype: openfhe.SERJSON) -> None

    2. DeserializeEvalAutomorphismKeyString(bytes: bytes, sertype: openfhe.SERBINARY) -> None
    """
    ...

def DeserializeEvalKey(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializeEvalKey(*args, **kwargs)
    Overloaded function.

    1. DeserializeEvalKey(filename: str, sertype: openfhe.SERJSON) -> tuple[openfhe.EvalKey, bool]

    2. DeserializeEvalKey(filename: str, sertype: openfhe.SERBINARY) -> tuple[openfhe.EvalKey, bool]
    """
    ...

def DeserializeEvalKeyMap(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializeEvalKeyMap(*args, **kwargs)
    Overloaded function.

    1. DeserializeEvalKeyMap(filename: str, sertype: openfhe.SERJSON) -> tuple[openfhe.EvalKeyMap, bool]

    2. DeserializeEvalKeyMap(filename: str, sertype: openfhe.SERBINARY) -> tuple[openfhe.EvalKeyMap, bool]
    """
    ...

def DeserializeEvalKeyMapString(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializeEvalKeyMapString(*args, **kwargs)
    Overloaded function.

    1. DeserializeEvalKeyMapString(str: bytes, sertype: openfhe.SERJSON) -> openfhe.EvalKeyMap

    2. DeserializeEvalKeyMapString(str: bytes, sertype: openfhe.SERBINARY) -> openfhe.EvalKeyMap
    """
    ...

def DeserializeEvalKeyMapVectorString(*args: Any, **kwargs: Any) -> Any:
    """DeserializeEvalKeyMapVectorString(str: bytes, sertype: openfhe.SERBINARY) -> list[openfhe.EvalKey]"""
    ...

def DeserializeEvalKeyString(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializeEvalKeyString(*args, **kwargs)
    Overloaded function.

    1. DeserializeEvalKeyString(str: str, sertype: openfhe.SERJSON) -> openfhe.EvalKey

    2. DeserializeEvalKeyString(str: bytes, sertype: openfhe.SERBINARY) -> openfhe.EvalKey
    """
    ...

def DeserializeEvalMultKeyString(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializeEvalMultKeyString(*args, **kwargs)
    Overloaded function.

    1. DeserializeEvalMultKeyString(data: str, sertype: openfhe.SERJSON) -> None

    2. DeserializeEvalMultKeyString(bytes: bytes, sertype: openfhe.SERBINARY) -> None
    """
    ...

def DeserializePrivateKey(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializePrivateKey(*args, **kwargs)
    Overloaded function.

    1. DeserializePrivateKey(filename: str, sertype: openfhe.SERJSON) -> tuple[openfhe.PrivateKey, bool]

    2. DeserializePrivateKey(filename: str, sertype: openfhe.SERBINARY) -> tuple[openfhe.PrivateKey, bool]
    """
    ...

def DeserializePrivateKeyString(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializePrivateKeyString(*args, **kwargs)
    Overloaded function.

    1. DeserializePrivateKeyString(str: str, sertype: openfhe.SERJSON) -> openfhe.PrivateKey

    2. DeserializePrivateKeyString(str: bytes, sertype: openfhe.SERBINARY) -> openfhe.PrivateKey
    """
    ...

def DeserializePublicKey(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializePublicKey(*args, **kwargs)
    Overloaded function.

    1. DeserializePublicKey(filename: str, sertype: openfhe.SERJSON) -> tuple[openfhe.PublicKey, bool]

    2. DeserializePublicKey(filename: str, sertype: openfhe.SERBINARY) -> tuple[openfhe.PublicKey, bool]
    """
    ...

def DeserializePublicKeyString(*args: Any, **kwargs: Any) -> Any:
    """
    DeserializePublicKeyString(*args, **kwargs)
    Overloaded function.

    1. DeserializePublicKeyString(str: str, sertype: openfhe.SERJSON) -> openfhe.PublicKey

    2. DeserializePublicKeyString(str: bytes, sertype: openfhe.SERBINARY) -> openfhe.PublicKey
    """
    ...

def DisablePrecomputeCRTTablesAfterDeserializaton(*args: Any, **kwargs: Any) -> Any:
    """
    DisablePrecomputeCRTTablesAfterDeserializaton() -> None

    Disable CRT precomputation after deserialization
    """
    ...

def EnablePrecomputeCRTTablesAfterDeserializaton(*args: Any, **kwargs: Any) -> Any:
    """
    EnablePrecomputeCRTTablesAfterDeserializaton() -> None

    Enable CRT precomputation after deserialization
    """
    ...

class EncryptionTechnique:
    """
    Members:

    STANDARD

    EXTENDED
    """
    def EXTENDED(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def STANDARD(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.EncryptionTechnique, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


def EvalChebyshevCoefficients(*args: Any, **kwargs: Any) -> Any:
    """EvalChebyshevCoefficients(func: collections.abc.Callable[[typing.SupportsFloat | typing.SupportsIndex], float], a: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex, degree: typing.SupportsInt | typing.SupportsIndex) -> list[float]"""
    ...

def EvalChebyshevFunctionPtxt(*args: Any, **kwargs: Any) -> Any:
    """EvalChebyshevFunctionPtxt(func: collections.abc.Callable[[typing.SupportsFloat | typing.SupportsIndex], float], ptxt: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], a: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex, degree: typing.SupportsInt | typing.SupportsIndex) -> list[float]"""
    ...

class EvalKey:
    def GetKeyTag(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeyTag(self: openfhe.EvalKey) -> str"""
        ...

    def SetKeyTag(self, *args: Any, **kwargs: Any) -> Any:
        """SetKeyTag(self: openfhe.EvalKey, arg0: str) -> None"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.EvalKey) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class EvalKeyMap:
    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.EvalKeyMap) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class ExecutionMode:
    """
    Members:

    EXEC_EVALUATION

    EXEC_NOISE_ESTIMATION
    """
    def EXEC_EVALUATION(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def EXEC_NOISE_ESTIMATION(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.ExecutionMode, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class FHECKKSRNS:
    def GetBootstrapDepth(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetBootstrapDepth(*args, **kwargs)
        Overloaded function.

        1. GetBootstrapDepth(depth: typing.SupportsInt | typing.SupportsIndex, levelBudget: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], keyDist: openfhe.SecretKeyDist) -> int

        2. GetBootstrapDepth(levelBudget: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], keyDist: openfhe.SecretKeyDist) -> int
        """
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.FHECKKSRNS) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class Format:
    """
    Members:

    EVALUATION

    COEFFICIENT
    """
    def COEFFICIENT(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def EVALUATION(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.Format, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


def GenCryptoContext(*args: Any, **kwargs: Any) -> Any:
    """
    GenCryptoContext(*args, **kwargs)
    Overloaded function.

    1. GenCryptoContext(params: openfhe.CCParamsBFVRNS) -> openfhe.CryptoContext

    2. GenCryptoContext(params: openfhe.CCParamsBGVRNS) -> openfhe.CryptoContext

    3. GenCryptoContext(params: openfhe.CCParamsCKKSRNS) -> openfhe.CryptoContext
    """
    ...

def GetAllContexts(*args: Any, **kwargs: Any) -> Any:
    """GetAllContexts() -> list[openfhe.CryptoContext]"""
    ...

class KEYGEN_MODE:
    """
    Members:

    SYM_ENCRYPT

    PUB_ENCRYPT
    """
    def PUB_ENCRYPT(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def SYM_ENCRYPT(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.KEYGEN_MODE, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class KeyPair:
    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def good(self, *args: Any, **kwargs: Any) -> Any:
        """
        good(self: openfhe.KeyPair) -> bool


        Checks whether both public key and secret key are non-null, or correctly initialized.

        :return: Result.
        :rtype: bool
        """
        ...

    def publicKey(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def secretKey(self, *args: Any, **kwargs: Any) -> Any:
        ...


class KeySwitchTechnique:
    """
    Members:

    INVALID_KS_TECH

    BV

    HYBRID
    """
    def BV(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def HYBRID(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def INVALID_KS_TECH(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.KeySwitchTechnique, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class LWECiphertext:
    def GetLength(self, *args: Any, **kwargs: Any) -> Any:
        """GetLength(self: openfhe.LWECiphertext) -> int"""
        ...

    def GetModulus(self, *args: Any, **kwargs: Any) -> Any:
        """GetModulus(self: openfhe.LWECiphertext) -> int"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.LWECiphertext) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class LWEPrivateKey:
    def GetLength(self, *args: Any, **kwargs: Any) -> Any:
        """GetLength(self: openfhe.LWEPrivateKey) -> int"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.LWEPrivateKey) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class MultipartyMode:
    """
    Members:

    INVALID_MULTIPARTY_MODE

    FIXED_NOISE_MULTIPARTY

    NOISE_FLOODING_MULTIPARTY
    """
    def FIXED_NOISE_MULTIPARTY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def INVALID_MULTIPARTY_MODE(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def NOISE_FLOODING_MULTIPARTY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.MultipartyMode, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class MultiplicationTechnique:
    """
    Members:

    BEHZ

    HPS

    HPSPOVERQ

    HPSPOVERQLEVELED
    """
    def BEHZ(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def HPS(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def HPSPOVERQ(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def HPSPOVERQLEVELED(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.MultiplicationTechnique, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class PKESchemeFeature:
    """
    Members:

    PKE

    KEYSWITCH

    PRE

    LEVELEDSHE

    ADVANCEDSHE

    MULTIPARTY

    FHE

    SCHEMESWITCH
    """
    def ADVANCEDSHE(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def FHE(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def KEYSWITCH(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def LEVELEDSHE(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def MULTIPARTY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def PKE(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def PRE(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def SCHEMESWITCH(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.PKESchemeFeature, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class ParmType:
    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class Plaintext:
    def Decode(self, *args: Any, **kwargs: Any) -> Any:
        """
        Decode(*args, **kwargs)
        Overloaded function.

        1. Decode(self: openfhe.Plaintext) -> bool


            Decode the polynomial into a plaintext.


        2. Decode(self: openfhe.Plaintext, arg0: typing.SupportsInt | typing.SupportsIndex, arg1: typing.SupportsFloat | typing.SupportsIndex, arg2: openfhe.ScalingTechnique, arg3: openfhe.ExecutionMode) -> bool
        """
        ...

    def Encode(self, *args: Any, **kwargs: Any) -> Any:
        """
        Encode(self: openfhe.Plaintext) -> bool


        Encode the plaintext into a polynomial.
        """
        ...

    def GetCKKSPackedValue(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetCKKSPackedValue(self: openfhe.Plaintext) -> list[complex]


        Get the packed value of the plaintext for CKKS-based plaintexts.

        :return: The packed value of the plaintext.
        :rtype: List[complex]
        """
        ...

    def GetCoefPackedValue(self, *args: Any, **kwargs: Any) -> Any:
        """GetCoefPackedValue(self: openfhe.Plaintext) -> list[int]"""
        ...

    def GetFormattedValues(self, *args: Any, **kwargs: Any) -> Any:
        """GetFormattedValues(self: openfhe.Plaintext, arg0: typing.SupportsInt | typing.SupportsIndex) -> str"""
        ...

    def GetLength(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetLength(self: openfhe.Plaintext) -> int


        Get method to return the length of the plaintext.

        :return: The length of the plaintext in terms of the number of bits.
        :rtype: int
        """
        ...

    def GetLevel(self, *args: Any, **kwargs: Any) -> Any:
        """GetLevel(self: openfhe.Plaintext) -> int"""
        ...

    def GetLogError(self, *args: Any, **kwargs: Any) -> Any:
        """GetLogError(self: openfhe.Plaintext) -> float"""
        ...

    def GetLogPrecision(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetLogPrecision(*args, **kwargs)
        Overloaded function.

        1. GetLogPrecision(self: openfhe.Plaintext) -> float


            Get the log of the plaintext precision.

            :return: The log of the plaintext precision.
            :rtype: float
        """
        ...

    def GetNoiseScaleDeg(self, *args: Any, **kwargs: Any) -> Any:
        """GetNoiseScaleDeg(self: openfhe.Plaintext) -> int"""
        ...

    def GetPackedValue(self, *args: Any, **kwargs: Any) -> Any:
        """GetPackedValue(self: openfhe.Plaintext) -> list[int]"""
        ...

    def GetRealPackedValue(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetRealPackedValue(self: openfhe.Plaintext) -> list[float]


        Get the real component of the packed value of the plaintext for CKKS-based plaintexts.

        :return: The real-component of the packed value of the plaintext.
        :rtype: List[double]
        """
        ...

    def GetScalingFactor(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetScalingFactor(self: openfhe.Plaintext) -> float


        Get the scaling factor of the plaintext for CKKS-based plaintexts.

        :return: The scaling factor of the plaintext.
        :rtype: float
        """
        ...

    def GetSchemeID(self, *args: Any, **kwargs: Any) -> Any:
        """
        GetSchemeID(self: openfhe.Plaintext) -> openfhe.SCHEME


        Get the encryption technique of the plaintext for BFV-based plaintexts.

        :return: The scheme ID of the plaintext.
        :rtype: SCHEME
        """
        ...

    def GetSlots(self, *args: Any, **kwargs: Any) -> Any:
        """GetSlots(self: openfhe.Plaintext) -> int"""
        ...

    def GetStringValue(self, *args: Any, **kwargs: Any) -> Any:
        """GetStringValue(self: openfhe.Plaintext) -> str"""
        ...

    def HighBound(self, *args: Any, **kwargs: Any) -> Any:
        """
        HighBound(self: openfhe.Plaintext) -> int


        Calculate and return upper bound that can be encoded with the plaintext modulus the number to encode MUST be less than this value

        :return: floor(p/2)
        :rtype: int
        """
        ...

    def IsEncoded(self, *args: Any, **kwargs: Any) -> Any:
        """
        IsEncoded(self: openfhe.Plaintext) -> bool


        Check if the plaintext is encoded.

        :return: True if the plaintext is encoded, False otherwise.
        :rtype: bool
        """
        ...

    def LowBound(self, *args: Any, **kwargs: Any) -> Any:
        """
        LowBound(self: openfhe.Plaintext) -> int


        Calculate and return lower bound that can be encoded with the plaintext modulus the number to encode MUST be greater than this value

        :return: floor(-p/2)
        :rtype: int
        """
        ...

    def SetFormat(self, *args: Any, **kwargs: Any) -> Any:
        """
        SetFormat(self: openfhe.Plaintext, fmt: openfhe.Format) -> None


        SetFormat - allows format to be changed for openfhe.Plaintext evaluations

        :param fmt:
        :type format: Format
        """
        ...

    def SetIntVectorValue(self, *args: Any, **kwargs: Any) -> Any:
        """SetIntVectorValue(self: openfhe.Plaintext, arg0: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> None"""
        ...

    def SetLength(self, *args: Any, **kwargs: Any) -> Any:
        """
        SetLength(self: openfhe.Plaintext, newSize: typing.SupportsInt | typing.SupportsIndex) -> None


        Resize the plaintext; only works for plaintexts that support a resizable vector (coefpacked).

        :param newSize: The new size of the plaintext.
        :type newSize: int
        """
        ...

    def SetLevel(self, *args: Any, **kwargs: Any) -> Any:
        """SetLevel(self: openfhe.Plaintext, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetNoiseScaleDeg(self, *args: Any, **kwargs: Any) -> Any:
        """SetNoiseScaleDeg(self: openfhe.Plaintext, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetScalingFactor(self, *args: Any, **kwargs: Any) -> Any:
        """
        SetScalingFactor(self: openfhe.Plaintext, sf: typing.SupportsFloat | typing.SupportsIndex) -> None


        Set the scaling factor of the plaintext for CKKS-based plaintexts.

        :param sf: The scaling factor to set.
        :type sf: float
        """
        ...

    def SetSlots(self, *args: Any, **kwargs: Any) -> Any:
        """SetSlots(self: openfhe.Plaintext, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetStringValue(self, *args: Any, **kwargs: Any) -> Any:
        """SetStringValue(self: openfhe.Plaintext, arg0: str) -> None"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class PrivateKey:
    def GetCryptoContext(self, *args: Any, **kwargs: Any) -> Any:
        """GetCryptoContext(self: openfhe.PrivateKey) -> lbcrypto::CryptoContextImpl<lbcrypto::DCRTPolyImpl<bigintdyn::mubintvec<bigintdyn::ubint<unsigned long long> > > >"""
        ...

    def GetKeyTag(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeyTag(self: openfhe.PrivateKey) -> str"""
        ...

    def SetKeyTag(self, *args: Any, **kwargs: Any) -> Any:
        """SetKeyTag(self: openfhe.PrivateKey, arg0: str) -> None"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.PrivateKey) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class ProxyReEncryptionMode:
    """
    Members:

    NOT_SET

    INDCPA

    FIXED_NOISE_HRA

    NOISE_FLOODING_HRA
    """
    def FIXED_NOISE_HRA(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def INDCPA(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def NOISE_FLOODING_HRA(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def NOT_SET(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.ProxyReEncryptionMode, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class PublicKey:
    def GetKeyTag(self, *args: Any, **kwargs: Any) -> Any:
        """GetKeyTag(self: openfhe.PublicKey) -> str"""
        ...

    def SetKeyTag(self, *args: Any, **kwargs: Any) -> Any:
        """SetKeyTag(self: openfhe.PublicKey, arg0: str) -> None"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.PublicKey) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


def ReleaseAllContexts(*args: Any, **kwargs: Any) -> Any:
    """ReleaseAllContexts() -> None"""
    ...

class SCHEME:
    """
    Members:

    INVALID_SCHEME

    CKKSRNS_SCHEME

    BFVRNS_SCHEME

    BGVRNS_SCHEME
    """
    def BFVRNS_SCHEME(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def BGVRNS_SCHEME(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def CKKSRNS_SCHEME(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def INVALID_SCHEME(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.SCHEME, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class SERBINARY:
    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class SERJSON:
    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class ScalingTechnique:
    """
    Members:

    FIXEDMANUAL

    FIXEDAUTO

    FLEXIBLEAUTO

    FLEXIBLEAUTOEXT

    NORESCALE

    COMPOSITESCALINGAUTO

    COMPOSITESCALINGMANUAL

    INVALID_RS_TECHNIQUE
    """
    def COMPOSITESCALINGAUTO(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def COMPOSITESCALINGMANUAL(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def FIXEDAUTO(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def FIXEDMANUAL(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def FLEXIBLEAUTO(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def FLEXIBLEAUTOEXT(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def INVALID_RS_TECHNIQUE(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def NORESCALE(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.ScalingTechnique, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class SchSwchParams:
    def GetArbitraryFunctionEvaluation(self, *args: Any, **kwargs: Any) -> Any:
        """GetArbitraryFunctionEvaluation(self: openfhe.SchSwchParams) -> bool"""
        ...

    def GetBStepLTrCKKStoFHEW(self, *args: Any, **kwargs: Any) -> Any:
        """GetBStepLTrCKKStoFHEW(self: openfhe.SchSwchParams) -> int"""
        ...

    def GetBStepLTrFHEWtoCKKS(self, *args: Any, **kwargs: Any) -> Any:
        """GetBStepLTrFHEWtoCKKS(self: openfhe.SchSwchParams) -> int"""
        ...

    def GetBatchSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetBatchSize(self: openfhe.SchSwchParams) -> int"""
        ...

    def GetComputeArgmin(self, *args: Any, **kwargs: Any) -> Any:
        """GetComputeArgmin(self: openfhe.SchSwchParams) -> bool"""
        ...

    def GetCtxtModSizeFHEWIntermedSwch(self, *args: Any, **kwargs: Any) -> Any:
        """GetCtxtModSizeFHEWIntermedSwch(self: openfhe.SchSwchParams) -> int"""
        ...

    def GetCtxtModSizeFHEWLargePrec(self, *args: Any, **kwargs: Any) -> Any:
        """GetCtxtModSizeFHEWLargePrec(self: openfhe.SchSwchParams) -> int"""
        ...

    def GetInitialCKKSModulus(self, *args: Any, **kwargs: Any) -> Any:
        """GetInitialCKKSModulus(self: openfhe.SchSwchParams) -> intnat::NativeIntegerT<unsigned long long>"""
        ...

    def GetLevelLTrCKKStoFHEW(self, *args: Any, **kwargs: Any) -> Any:
        """GetLevelLTrCKKStoFHEW(self: openfhe.SchSwchParams) -> int"""
        ...

    def GetLevelLTrFHEWtoCKKS(self, *args: Any, **kwargs: Any) -> Any:
        """GetLevelLTrFHEWtoCKKS(self: openfhe.SchSwchParams) -> int"""
        ...

    def GetNumSlotsCKKS(self, *args: Any, **kwargs: Any) -> Any:
        """GetNumSlotsCKKS(self: openfhe.SchSwchParams) -> int"""
        ...

    def GetNumValues(self, *args: Any, **kwargs: Any) -> Any:
        """GetNumValues(self: openfhe.SchSwchParams) -> int"""
        ...

    def GetOneHotEncoding(self, *args: Any, **kwargs: Any) -> Any:
        """GetOneHotEncoding(self: openfhe.SchSwchParams) -> bool"""
        ...

    def GetRingDimension(self, *args: Any, **kwargs: Any) -> Any:
        """GetRingDimension(self: openfhe.SchSwchParams) -> int"""
        ...

    def GetScalingModSize(self, *args: Any, **kwargs: Any) -> Any:
        """GetScalingModSize(self: openfhe.SchSwchParams) -> int"""
        ...

    def GetSecurityLevelCKKS(self, *args: Any, **kwargs: Any) -> Any:
        """GetSecurityLevelCKKS(self: openfhe.SchSwchParams) -> openfhe.SecurityLevel"""
        ...

    def GetSecurityLevelFHEW(self, *args: Any, **kwargs: Any) -> Any:
        """GetSecurityLevelFHEW(self: openfhe.SchSwchParams) -> openfhe.BINFHE_PARAMSET"""
        ...

    def GetUseAltArgmin(self, *args: Any, **kwargs: Any) -> Any:
        """GetUseAltArgmin(self: openfhe.SchSwchParams) -> bool"""
        ...

    def GetUseDynamicModeFHEW(self, *args: Any, **kwargs: Any) -> Any:
        """GetUseDynamicModeFHEW(self: openfhe.SchSwchParams) -> bool"""
        ...

    def SetArbitraryFunctionEvaluation(self, *args: Any, **kwargs: Any) -> Any:
        """SetArbitraryFunctionEvaluation(self: openfhe.SchSwchParams, arg0: bool) -> None"""
        ...

    def SetBStepLTrCKKStoFHEW(self, *args: Any, **kwargs: Any) -> Any:
        """SetBStepLTrCKKStoFHEW(self: openfhe.SchSwchParams, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetBStepLTrFHEWtoCKKS(self, *args: Any, **kwargs: Any) -> Any:
        """SetBStepLTrFHEWtoCKKS(self: openfhe.SchSwchParams, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetBatchSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetBatchSize(self: openfhe.SchSwchParams, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetComputeArgmin(self, *args: Any, **kwargs: Any) -> Any:
        """SetComputeArgmin(self: openfhe.SchSwchParams, arg0: bool) -> None"""
        ...

    def SetCtxtModSizeFHEWIntermedSwch(self, *args: Any, **kwargs: Any) -> Any:
        """SetCtxtModSizeFHEWIntermedSwch(self: openfhe.SchSwchParams, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetCtxtModSizeFHEWLargePrec(self, *args: Any, **kwargs: Any) -> Any:
        """SetCtxtModSizeFHEWLargePrec(self: openfhe.SchSwchParams, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetInitialCKKSModulus(self, *args: Any, **kwargs: Any) -> Any:
        """SetInitialCKKSModulus(self: openfhe.SchSwchParams, arg0: intnat::NativeIntegerT<unsigned long long>) -> None"""
        ...

    def SetLevelLTrCKKStoFHEW(self, *args: Any, **kwargs: Any) -> Any:
        """SetLevelLTrCKKStoFHEW(self: openfhe.SchSwchParams, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetLevelLTrFHEWtoCKKS(self, *args: Any, **kwargs: Any) -> Any:
        """SetLevelLTrFHEWtoCKKS(self: openfhe.SchSwchParams, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetNumSlotsCKKS(self, *args: Any, **kwargs: Any) -> Any:
        """SetNumSlotsCKKS(self: openfhe.SchSwchParams, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetNumValues(self, *args: Any, **kwargs: Any) -> Any:
        """SetNumValues(self: openfhe.SchSwchParams, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetOneHotEncoding(self, *args: Any, **kwargs: Any) -> Any:
        """SetOneHotEncoding(self: openfhe.SchSwchParams, arg0: bool) -> None"""
        ...

    def SetRingDimension(self, *args: Any, **kwargs: Any) -> Any:
        """SetRingDimension(self: openfhe.SchSwchParams, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetScalingModSize(self, *args: Any, **kwargs: Any) -> Any:
        """SetScalingModSize(self: openfhe.SchSwchParams, arg0: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def SetSecurityLevelCKKS(self, *args: Any, **kwargs: Any) -> Any:
        """SetSecurityLevelCKKS(self: openfhe.SchSwchParams, arg0: openfhe.SecurityLevel) -> None"""
        ...

    def SetSecurityLevelFHEW(self, *args: Any, **kwargs: Any) -> Any:
        """SetSecurityLevelFHEW(self: openfhe.SchSwchParams, arg0: openfhe.BINFHE_PARAMSET) -> None"""
        ...

    def SetUseAltArgmin(self, *args: Any, **kwargs: Any) -> Any:
        """SetUseAltArgmin(self: openfhe.SchSwchParams, arg0: bool) -> None"""
        ...

    def SetUseDynamicModeFHEW(self, *args: Any, **kwargs: Any) -> Any:
        """SetUseDynamicModeFHEW(self: openfhe.SchSwchParams, arg0: bool) -> None"""
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.SchSwchParams) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...


class SecretKeyDist:
    """
    Members:

    GAUSSIAN

    UNIFORM_TERNARY

    SPARSE_TERNARY

    SPARSE_ENCAPSULATED
    """
    def GAUSSIAN(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def SPARSE_ENCAPSULATED(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def SPARSE_TERNARY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def UNIFORM_TERNARY(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.SecretKeyDist, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


class SecurityLevel:
    """
    Members:

    HEStd_128_classic

    HEStd_192_classic

    HEStd_256_classic

    HEStd_128_quantum

    HEStd_192_quantum

    HEStd_256_quantum

    HEStd_NotSet
    """
    def HEStd_128_classic(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def HEStd_128_quantum(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def HEStd_192_classic(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def HEStd_192_quantum(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def HEStd_256_classic(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def HEStd_256_quantum(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def HEStd_NotSet(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> Any:
        """__init__(self: openfhe.SecurityLevel, value: typing.SupportsInt | typing.SupportsIndex) -> None"""
        ...

    def _pybind11_conduit_v1_(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name(self: object, /) -> str"""
        ...

    def value(self, *args: Any, **kwargs: Any) -> Any:
        ...


def Serialize(*args: Any, **kwargs: Any) -> Any:
    """
    Serialize(*args, **kwargs)
    Overloaded function.

    1. Serialize(obj: openfhe.CryptoContext, sertype: openfhe.SERJSON) -> str

    2. Serialize(obj: openfhe.PublicKey, sertype: openfhe.SERJSON) -> str

    3. Serialize(obj: openfhe.PrivateKey, sertype: openfhe.SERJSON) -> str

    4. Serialize(obj: openfhe.Ciphertext, sertype: openfhe.SERJSON) -> str

    5. Serialize(obj: openfhe.EvalKey, sertype: openfhe.SERJSON) -> str

    6. Serialize(obj: openfhe.EvalKeyMap, sertype: openfhe.SERJSON) -> bytes

    7. Serialize(obj: openfhe.CryptoContext, sertype: openfhe.SERBINARY) -> bytes

    8. Serialize(obj: openfhe.PublicKey, sertype: openfhe.SERBINARY) -> bytes

    9. Serialize(obj: openfhe.PrivateKey, sertype: openfhe.SERBINARY) -> bytes

    10. Serialize(obj: openfhe.Ciphertext, sertype: openfhe.SERBINARY) -> bytes

    11. Serialize(obj: openfhe.EvalKey, sertype: openfhe.SERBINARY) -> bytes

    12. Serialize(obj: openfhe.EvalKeyMap, sertype: openfhe.SERBINARY) -> bytes

    13. Serialize(obj: collections.abc.Sequence[openfhe.EvalKey], sertype: openfhe.SERBINARY) -> bytes
    """
    ...

def SerializeEvalAutomorphismKeyString(*args: Any, **kwargs: Any) -> Any:
    """
    SerializeEvalAutomorphismKeyString(*args, **kwargs)
    Overloaded function.

    1. SerializeEvalAutomorphismKeyString(sertype: openfhe.SERJSON, keyTag: str = '') -> str

    2. SerializeEvalAutomorphismKeyString(sertype: openfhe.SERBINARY, keyTag: str = '') -> bytes
    """
    ...

def SerializeEvalMultKeyString(*args: Any, **kwargs: Any) -> Any:
    """
    SerializeEvalMultKeyString(*args, **kwargs)
    Overloaded function.

    1. SerializeEvalMultKeyString(sertype: openfhe.SERJSON, keyTag: str = '') -> str

    2. SerializeEvalMultKeyString(sertype: openfhe.SERBINARY, keyTag: str = '') -> bytes
    """
    ...

def SerializeToFile(*args: Any, **kwargs: Any) -> Any:
    """
    SerializeToFile(*args, **kwargs)
    Overloaded function.

    1. SerializeToFile(filename: str, obj: openfhe.CryptoContext, sertype: openfhe.SERJSON) -> bool

    2. SerializeToFile(filename: str, obj: openfhe.PublicKey, sertype: openfhe.SERJSON) -> bool

    3. SerializeToFile(filename: str, obj: openfhe.PrivateKey, sertype: openfhe.SERJSON) -> bool

    4. SerializeToFile(filename: str, obj: openfhe.Ciphertext, sertype: openfhe.SERJSON) -> bool

    5. SerializeToFile(filename: str, obj: openfhe.EvalKey, sertype: openfhe.SERJSON) -> bool

    6. SerializeToFile(filename: str, obj: openfhe.EvalKeyMap, sertype: openfhe.SERJSON) -> bool

    7. SerializeToFile(filename: str, obj: openfhe.CryptoContext, sertype: openfhe.SERBINARY) -> bool

    8. SerializeToFile(filename: str, obj: openfhe.PublicKey, sertype: openfhe.SERBINARY) -> bool

    9. SerializeToFile(filename: str, obj: openfhe.PrivateKey, sertype: openfhe.SERBINARY) -> bool

    10. SerializeToFile(filename: str, obj: openfhe.Ciphertext, sertype: openfhe.SERBINARY) -> bool

    11. SerializeToFile(filename: str, obj: openfhe.EvalKey, sertype: openfhe.SERBINARY) -> bool

    12. SerializeToFile(filename: str, obj: openfhe.EvalKeyMap, sertype: openfhe.SERBINARY) -> bool
    """
    ...

def get_native_int(*args: Any, **kwargs: Any) -> Any:
    """get_native_int() -> int"""
    ...

