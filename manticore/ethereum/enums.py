"""
Enums for Manticore Ethereum transaction types and results.

Replaces string constants with enum comparisons for better performance
and type safety.
"""
from enum import Enum


class TxType(Enum):
    """Ethereum transaction types (sort field)"""
    CREATE = "CREATE"
    CALL = "CALL"
    DELEGATECALL = "DELEGATECALL"
    
    def __str__(self):
        return self.value


class TxResult(Enum):
    """Ethereum transaction result types"""
    STOP = "STOP"
    RETURN = "RETURN"
    SELFDESTRUCT = "SELFDESTRUCT"
    THROW = "THROW"
    TXERROR = "TXERROR"
    REVERT = "REVERT"
    
    def __str__(self):
        return self.value


class Architecture(Enum):
    """Native CPU architectures"""
    I386 = "i386"
    AMD64 = "amd64"
    ARMV7 = "armv7"
    ARM64 = "arm64"
    
    def __str__(self):
        return self.value
