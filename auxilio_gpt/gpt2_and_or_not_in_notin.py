# ------------------------------
# Operador AND (E)
# Retorna True só se TODAS as condições
# forem VERDADEIRAS
# ------------------------------

idade = 20
tem_carteira = True

# Só pode dirigir se for maior de idade e tiver carteira
if idade >= 18 and tem_carteira:
    print('Pode dirigir!')
else:
    print('Não pode dirigir!')

# Outro exemplo com strings:
usuario = input('Usuário: ')
senha = input('Senha: ')

if usuario == 'admin' and senha == '1234':
    print('Acesso permitido.')
else:
    print('Acesso negado.')

# Exemplo com três condições:
nome = input('Nome do aluno: ')
nota = int(input('Nota do aluno: '))
frequencia = int(input('Frequência do aluno: '))
projeto_entregue = input('O aluno fez o projeto? (Insira S ou N): ')

if projeto_entregue == 'S':
    projeto_entregue = True
elif projeto_entregue == 'N':
    projeto_entregue = False
else:
    print('Comando inválido, repita o processo')
    exit() # Encerra o programa se a entrada for inválida

if nota >= 7 and frequencia >= 70 and projeto_entregue:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado.')

# ------------------------------
# Operador OR (OU)
# Retorna o primeiro valor "verdadeiro"
# Se o primeiro for falso, retorna o segundo
# ------------------------------

senha = input('Digite uma senha: ') or 'Sem senha'
print('Resultado com OR: ', senha)

# Se o usuário digitar algo, isso será usado
# Se deixar vazio, OR usará o valor padrão: 'Sem senha'

# ------------------------------
# Operador NOT (NÃO)
# Inverte o valor lógico (True vira False, e vice-versa)
# ------------------------------

ativo = False
if not ativo:
    print('Usuário inativo!')

# NOT também funciona com valores vazios ou zero
texto = ''
if not texto:
    print('Texto está vazio.')

# ------------------------------
# Operador IN
# Verifica se um valor está dentro de uma sequência:
# (string, lista, etc.)
# ------------------------------

frutas = ['maçã', 'banana', 'laranja']
print('banana' in frutas) # True
print('uva' in frutas) #False

nome = 'Gabriel'
print('a' in nome) # True
print('x' in nome) # False

# ------------------------------
# Operador NOT IN
# Verifica se um valor NÃO está dentro de uma sequência
# ------------------------------

print('uva' not in frutas) # True
print('banana' not in frutas) # False

letra = 'z'
print(letra not in nome) # True

# ------------------------------
# Combinação prática
# ------------------------------

senha = input('Crie uma senha: ')
if len(senha) < 6 or '!' not in senha:
    print('Senha fraca. Use pelo menos 6 caracteres e inclua "!".')
else:
    print('Senha válida!')