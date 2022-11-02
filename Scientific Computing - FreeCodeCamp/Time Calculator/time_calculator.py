def add_time(start, duration, day = None):

# As strings recebidas estão no formato de 12 horas, como 12:00 AM, dessa forma o primeiro passo é dividir a string em partes diferentes

# Divide a string start

  horário_começo = start.split()[0]
  sistema_12_horas = start.split()[1]

# Lê a string horário e a divide em duas, horas e minutos

  horas_começo = int(horário_começo.split(":")[0])
  minutos_começo = int(horário_começo.split(":")[1])
  
# Divide a string duration

  horas_duração = int(duration.split(":")[0])
  minutos_duração = int(duration.split(":")[1])

# Precisamos, também, listar os dias da semana para utilizar no código

  dias_da_semana_índice = {'monday' : 0, 'tuesday' : 1, 'wednesday' : 2, 'thursday' : 3, 'friday' : 4, 'saturday' : 5, 'sunday' : 6}

  dias_da_semana_lista = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Precisamos analisar se o horário do dia virou ou não, para isso vamos criar um dicionário

  am_e_pm = {'AM':'PM','PM':'AM'}

# Agora, temos que transformar as strings em int para somá-las. Primeiro, pelos minutos

  minutos_final = minutos_começo + minutos_duração

# Precisamos conferir se os minutos ultrapassam mais de 60 minutos
  
  if(minutos_final>=60):
    minutos_final = minutos_final%60
    horas_começo += 1

# Se isso acontecer, o horário final deve ser contabilizado com mais um

# Haverá valores de minutos onde a string deveria ser 0 seguido de um número, por exemplo 3:02 + 1:04 = 4:06
# Assim, devemos levar isso em consideração

  minutos_final = minutos_final if minutos_final > 9 else "0" + str(minutos_final)

# É necessário analisar quantos dias se passaram na string de duração

  dias_passados = int(horas_duração/24)

# Agora, vamos somar o tempo de duração com o horário de início
  
  horas_final = (horas_começo + horas_duração)%12
  
# Conferimos se o valor de horas_final não é nulo

  horas_final = horas_final = 12 if horas_final == 0 else horas_final 

# Devemos, ainda, conferir se está  nas primeiras ou últimos 12 horas do dia e quantos dias se passaram

  quantidade_viradas = int((horas_começo + horas_duração)/12)

  if(sistema_12_horas == 'PM' and horas_começo + (horas_duração%12) >= 12):
    dias_passados+=1

  sistema_12_horas = am_e_pm[sistema_12_horas] if quantidade_viradas % 2 == 1 else sistema_12_horas 

# Vamos montar a string final 

  horário_final = str(horas_final) + ':' + str(minutos_final) + ' ' + sistema_12_horas   

# Vamos analisar, agora, em que dia estamos (se necessário)

  if(day):
    day = day.lower()
    índice = (int((dias_da_semana_índice[day])) + int(dias_passados)) % 7 
    dia_final = dias_da_semana_lista[índice]
    horário_final += ', ' + dia_final

# Formatando para a string final

  if(dias_passados == 1):
    horário_final = horário_final + ' (next day)'
  elif(dias_passados > 1):
    horário_final = horário_final + ' (' + str(int(dias_passados)) + ' days later)'
    
  return horário_final
