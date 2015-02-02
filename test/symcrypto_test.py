from lib.crypto.symcrypto import *

import unittest
import logging

class TestSymcrypto(unittest.TestCase):
    """
    Unit tests for Symmetric Cryptography.
    """

    def test(self):
        """
        Symmetric cryptography test case. Test includes
        1. Hash (sha3) hash testing. Compare generated results with
        http://sha3calculator.appspot.com/
        2. MAC (AES-CBC-MAC) testing for random symmetric keys and messages.
        3. Block cipher (AES-CBC) testing with random keys and messages.
        4. Authenticated encryption (AES-GCM) testing with.
        """
        print ('1. Hash Test:')
        msg = 'VRJ8JiM0J4M4ioyLJM6qR1CznEMYnymr1jJxgcLATjlEOFMc6x02wpRCUjo'
        print ('msg = %s' % msg)
        print ('sha3-224(msg) = %s' % sha3hash(msg, 'SHA3-224'))
        print ('sha3-256(msg) = %s' % sha3hash(msg, 'SHA3-256'))
        print ('sha3-384(msg) = %s' % sha3hash(msg, 'SHA3-384'))
        print ('sha3-512(msg) = %s' % sha3hash(msg))# default is SHA-512

        key = get_random_bytes(16)
        key_cache = get_roundkey_cache(key)
        print ('key = %s' % key)

        print ('2. MAC Test:')
        mac = get_cbcmac(key_cache, msg.encode('utf-8'))
        print ("get_cbcmac(key_cache, msg) = %s" % mac)
        print ("CBC-MAC-Verify(key_cache, msg, mac) = ",
               verify_cbcmac(key_cache, msg.encode('utf-8'), mac))

        print ('3. Block Cipher Test:')
        msg = 'Message to be encrypted by AES-CBC block cipher. This is end of message.'
        cipher = cbc_encrypt(key_cache, msg.encode('utf-8')) # iv = 0
        print ('msg = %s' % msg)
        print ('cipher = %s' % cipher)
        decipher = cbc_decrypt(key_cache, cipher)
        print ('decipher = %s' % decipher.decode('utf-8'))

        print ('4. Authenticated Encryption Test:')
        msg = 'This is a message to be protected'
        auth = 'D609B1F056637A0D46DF998D88E5222AB2C2846512153524C0895E8108000F10'
        authcipher = authenticated_encrypt(key_cache, msg.encode('utf-8'), 
                                           auth.encode('utf-8')) # iv = None
        print ('authcipher = %s' % authcipher)
        decipher = authenticated_decrypt(key_cache, authcipher, auth.encode('utf-8'))
        print ('decipher = %s' % decipher.decode('utf-8'))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()