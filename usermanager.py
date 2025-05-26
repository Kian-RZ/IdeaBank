import os
import hashlib

UMD = "umd.txt"

def check_signup():
    if os.path.exists(UMD):
        with open(UMD,"r",encoding="utf-8") as umd:
            outs = umd.readlines()
            umd.close()
            if outs == []:
                return False
            else:
                if outs[0] != None or outs[0] != "" or outs[0] != " " and outs[1] != None or outs[1] != "" or outs[1] != " ":
                    return {"username":str(outs[0]),"password_hash":str(outs[1])}
                else:
                    return False
    else:
        return False
    
def register_new_user(username,password):
    username = str(username)
    password = str(hashlib.sha256(str(password).encode('utf-8')).hexdigest())
    with open(UMD, "w", encoding="utf-8") as umd:
        data = [username,'\n',password]
        umd.writelines(data)
        umd.close()