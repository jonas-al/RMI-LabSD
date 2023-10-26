import Pyro5.api
import time


greeting_maker = Pyro5.api.Proxy("PYRONAME:valorant.rmi") # use name server object lookup uri shortcut
#print(f'Random agent: {greeting_maker.getRandomAgent()}')
#print(f'Random weapon: {greeting_maker.getRandomWeapon()}')
#print(f'Random agente icon: \n {greeting_maker.getRandomAgentIcon()}')

print(greeting_maker.getMethods())

while True:
  try:
    method = input('Digite o número de algum método ou alguma palavra relacionada: ')

    if 'exit' in method or 'sair' in method:
      raise KeyboardInterrupt
    
    elif (method == '1' or 'agente' in method or 'agent' in method) and 'icone' not in method and 'icon' not in method:
      print('Executando o método getRandomAgent()')
      print('Nome do agente: ' + greeting_maker.getRandomAgent())

    elif method == '2' or 'arma' in method or 'weapon' in method:
      print('Executando o método getRandomWeapon()')
      print('Nome da arma: ' + greeting_maker.getRandomWeapon())

    elif method == '3' or 'icone' in method or 'icon' in method or 'agent icon' in method or 'icone do agente' in method:
      print('Executando o método getRandomAgentIcon()')
      response = greeting_maker.getRandomAgentIcon()
      print('Nome do agente: ' + response[0])
      print('Ícone do agente:\n' + response[1])

    else:
      print('Método inválido, informe uma opção novamente!')
      continue
  
  except KeyboardInterrupt:
    time.sleep(0.2)
    print('\nEncerrando o programa', end='')
    for i in range(6):
      print('.', end='', flush=True)
      time.sleep(0.7)
    break

  print('')