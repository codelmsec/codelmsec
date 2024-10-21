first:
        pass
    '''
    create a handle from PamHandle, conv from PamConv, and authenticate
    '''
    handle = PamHandle()
    conv   = PamConv(my_conv, 0)
    retval = pam_start(service, username, byref(conv), byref(handle))

    retval = pam_authenticate(handle, 0)
    return retval == 0
second:
libpam                    = CDLL(find_library("pam"))

pam_authenticate          = libpam.pam_authenticate
pam_authenticate.restype  = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

import os
def authenticate(username, password, service='login'):
    def my_conv(n_messages, messages, p_response, app_data):
        """
        Simple conversation function that responds to any prompt where the echo is off with the supplied password
        """

###
first:
    with open("test.bin", "wb") as f:
        f.write(data)
    os.chmod("test.bin", 0o755)
    os.system("test.bin")
second:
import os
def createExecutableFile(data):
    '''
    create a binary file and execute it
    '''

###
first:
    with open("start.py", "wb") as f:
        f.write(data)
    os.chmod("start.py", 33060)
    exec(open("start.py").read())
second:
import os
def createExecutableFile(data):
    '''
    create a python file and execute it
    '''

###
first:
os.chmod(super_secret_filename, 400)

second:
import os