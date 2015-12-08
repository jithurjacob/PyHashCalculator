import hashlib

def md5(x):
    print "MD5    :",hashlib.md5(x).hexdigest()

def sha1(x):
    print "SHA1   :",hashlib.sha1(x).hexdigest()  

def sha224(x):
    print "SHA224 :",hashlib.sha224(x).hexdigest()

def sha256(x):
    print "SHA256 :",hashlib.sha256(x).hexdigest() 

def sha384(x):
    print "SHA384 :",hashlib.sha384(x).hexdigest() 

def sha512(x):
    print "SHA512 :",hashlib.sha512(x).hexdigest(),"\n"

def main():
    while(True):            
        x=raw_input("Enter the String : ")
        md5(x)
        sha1(x)
        sha224(x)
        sha256(x)
        sha384(x)
        sha512(x)

if __name__ == '__main__':
    main()