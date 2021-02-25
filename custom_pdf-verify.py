# *-* coding: utf-8 *-*
from endesive import pdf


def main():
    trusted_cert_pems = (
        #working fine but certification are failing
        # open('demo2_ca.crt.pem','rt').read(),
        open('demo2_ca.crt.pem', 'rt').read(),
        #trial ones
        
        #fails pem files
        
        # open('demo2_user1.pub.pem','rt').read()
        # open('demo2_user1.p12','rt').read()   
        # open('demo2_user1.key.pem','rt').read()
        # open('demo2_ca.key.pem','rt').read(),
        # open('demo2_user1.crt.pem','rt').read()
        
    )
    try:
        data = open('pdf-signed-cms.pdf', 'rb').read()
    except Exception as e:
        print('Exception are -{}'.format(e))
    (hashok, signatureok, certok) = pdf.verify(data, trusted_cert_pems)
    # print(data)
    # print(trusted_cert_pems)
    print('signature ok?', signatureok)
    print('hash ok?', hashok)
    print('cert ok?', certok)


main()
