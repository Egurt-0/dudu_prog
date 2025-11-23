import hashlib
#************************************************
# ESSE MODULO SERVE PARA CRIPTOGRAFIA DE DADOS
#************************************************


# verficar os algoritimos disponiveis
print(hashlib.algorithms_available)


# 2 - verificar algoritimos de acordo com o Sistema operacional(OS)
print(hashlib.algorithms_guaranteed)


# 2 - utilizando o SHA256
algoritim = hashlib.sha256()
print(algoritim.digest())
message = "A melhor forma de prever futuro e crialo".encode()
algoritim.update(message)
print(algoritim.hexdigest())

# 4 - utilizando o MDS
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())