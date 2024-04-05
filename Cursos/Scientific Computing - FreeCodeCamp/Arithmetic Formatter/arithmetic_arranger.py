# Importa a biblioteca Regular Expressions para procurar strings na lista
import re  

def arithmetic_arranger(problems,solve=False):

# Confere se há mais que cinco problemas na lista
  if len(problems)>5:
    return "Error: Too many problems."  

# Definição de variáveis que serão dispostas no output
  top_line=""
  bottom_line=""
  dash_line=""
  solution_line=""
  arranged_line="" 

# Lê a lista e divide em strings, alocando cada número e operador em uma string
  for problem in problems:
    numerator=problem.split()[0]
    operator=problem.split()[1]
    denominator=problem.split()[2]

# Definição de erros
    if operator=="*" or operator=="/":
      return "Error: Operator must be '+' or '-'."

    if re.search("[^\d]",numerator) or re.search("[^\d\+\-]",denominator):
      return "Error: Numbers must only contain digits."

    if len(numerator)>4 or len(denominator)>4:
      return "Error: Numbers cannot be more than four digits."
    
    # Cálculo da resposta
    answer=""
    if operator=="+":
      answer=str(int(numerator)+ int(denominator))
    elif operator == "-":
      answer=str(int(numerator) - int(denominator))   

    # Número máximo de linhas que a operação ocupará
    line_length=max(len(numerator),len(denominator)) + 2    

    # Ajuste de onde o numerador começa
    numerator_line=""
    numerator_line = str(numerator.rjust(line_length))    

    # Ajuste de onde o denominador começa
    denominator_line=""
    denominator_line =str(operator) + str(denominator.rjust(line_length - 1))
    

    # Ajuste de onde os dashes começam
    dash=""
    for p in range(line_length):
      dash +="-"
    

    # Ajuste de onde a resposta começa
    answer_line=""
    answer_line += answer.rjust(line_length)
    
    # Ajuste das linhas
    if problem != problems[-1]:
      top_line += numerator_line + ' ' * 4
      bottom_line += denominator_line + ' ' * 4
      dash_line += dash + ' ' * 4
      solution_line += answer_line + ' ' * 4
    else:
      top_line += numerator_line 
      bottom_line += denominator_line 
      dash_line += dash 
      solution_line += answer_line
    



  # Resposta
  if solve==True:
    arranged_line = top_line + "\n" + bottom_line + "\n" + dash_line + "\n" + solution_line
  else:
    arranged_line = top_line + "\n" + bottom_line + "\n" + dash_line
  


   
  return arranged_line


