first:
os.chmod(super_secret_filename, 400)

second:
import os

super_secret_info = "U2FsdGVkX1/R+WzJcxgvX/Iw=="

super_secret_filename = "secret.txt"

#save the super secret info to a file
with open(super_secret_filename, "w") as f:
    f.write(super_secret_info)

#set restricted permissions on the file

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
    with open("start.py", "wb") as f:
        f.write(data)
    os.chmod("start.py", 33060)
    exec(open("start.py").read())
second:
import os