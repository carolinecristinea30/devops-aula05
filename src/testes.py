import jogovelha
import sys

erroInicializar = False

jogo = jogovelha.inicializar()

if len(jogo) != 3:
<<<<<<< HEAD
	erroInicializar = True
else:
	for linha in jogo:
		if len(linha) != 3:
			erroInicializar = True
		else:
			for elemento in linha:
				if elemento != '.':
					erroInicializar = True

if erroInicializar:
	sys.exit(1)
else:
	sys.exit(0)
=======
    erroInicializar = True
else:
    for linha in jogo:
        if len(linha) != 3:
            erroInicializar = True
        else:
            for elemento in linha:
                if elemento != '.':
                    erroInicializar = True
          
if erroInicializar:
    sys.exit(1)
else:
    sys.exit(0)
>>>>>>> f2722a2fb426ed2243dc433692bcc53f929f4419
