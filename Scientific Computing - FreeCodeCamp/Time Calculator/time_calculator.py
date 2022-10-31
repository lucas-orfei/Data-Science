def add_time(start, duration, day = None):

# As strings recebidas estão no formato de 12 horas, como 12:00 AM, dessa forma o primeiro passo é dividir a string em partes diferentes

# Divide a string start

  horário_começo = start.split()[0]
  sistema_12_horas = start.split()[1]

# Lê a string horário e a divide em duas, horas e minuto

  horas_começo = horário_começo.split(":")[0]
  minutos_começo = horário_começo.split(":")[1]
  
# Divide a string duration

  horas_duração = duration.split(":")[0]
  minutos_duração = duration.split(":")[1]

# Agora, temos que transformar as strings em int para somá-las. Primeiro, pelos minutos

  minutos_soma = int(minutos_começo) + int(minutos_duração)

# Precisamos conferir se os minutos ultrapassam mais de 60 minutos

  if(minutos_soma>60):
    minutos = minutos_soma%60

# Se isso acontecer, o horário final deve ser contabilizado com mais um

# É necessário analisar quantos dias se passaram na string de duração

  if(int(horas_duração)>24):
    dias_duração = int(horas_duração)%24



  #if(horas_duração>12 and sistema_12_horas == 'PM'):











  #return new_time
  return dias_duração



print(add_time("11:46 PM", "302:32"))
