from pybrain.structure import FeedForwardNetwork
from pybrain.structure import linearLayer, SignoidLayer, BiasUnit
from pybrain.structure import FullConnection

rede = FeedFowardNetwork()
camadaEntrada = LinearLayer(2)
camadaOculta = SignoidLayer(3)
camadaSaida = SignoidLayer(1)
bias1 = BiasUnit()
bias2 = BiasUnit()

rede.addModule(camadaEntrada)
rede.addModule(camadaOculta)
rede.addModule(camadaSaida)
rede.addModule(bias1)
rede.addModule(bias2)

entradaOculta = FullConnetction(camadaEntrada,camadaOculta)
ocultaSaida = FullConnection(camadaOculta, camadaSaida)
biasOculta = FullConnection(bias1, camadaOculta)
biasSaida = FullConnection(bias2, camadaSaida)

rede.sortModules()
print(rede)
