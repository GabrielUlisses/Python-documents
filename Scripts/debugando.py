#python -m pbd programa.py
import pdb
'''
    set_trace()
    list: mostra um trecho do código em execução, com destaque para a linha atual;
    next: comando que indica ao pdb que ele deve seguir para a próxima linha de execução, sem adentrar em funções quando houverem chamadas;
    step: indica ao pdb para que ele siga em frente, entrando na função se a linha atual for uma chamada de função;
    pp <nome_de_variável>: mostra na tela o valor referenciado pela variável nome_de_variável.
'''
import logging


logging.debug('depurando ...')
logging.info('informando ...')
logging.warning('alertando ...')
logging.error('assustando ...')
logging.critical('apavorando ...')
print(__name__)
