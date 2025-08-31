# funcoes.py

def cadastrar_aluno(alunos, matricula, nome):
    
    if matricula in alunos:
        print("Erro: Matrícula já existe.")
    else:
        alunos[matricula] = {
            "nome": nome,
            "disciplinas": set(),
            "notas": {}
        }
        print(f"Aluno '{nome}' cadastrado com sucesso.")

def cadastrar_disciplina(disciplinas, codigo, nome):
    
    if codigo in disciplinas:
        print("Erro: Código da disciplina já existe.")
    else:
        disciplinas[codigo] = {
            "nome": nome,
            "alunos": set()
        }
        print(f"Disciplina '{nome}' cadastrada com sucesso.")

def matricular_aluno(alunos, disciplinas, matricula, codigo):
   
    if matricula not in alunos:
        print("Erro: Aluno não encontrado.")
    elif codigo not in disciplinas:
        print("Erro: Disciplina não encontrada.")
    elif codigo in alunos[matricula]["disciplinas"]:
        print("Aviso: Aluno já matriculado nesta disciplina.")
    else:
        alunos[matricula]["disciplinas"].add(codigo)
        disciplinas[codigo]["alunos"].add(matricula)
        if codigo not in alunos[matricula]["notas"]:
            alunos[matricula]["notas"][codigo] = []
        print(f"Aluno {alunos[matricula]['nome']} matriculado em {disciplinas[codigo]['nome']} com sucesso.")

def lancar_nota(alunos, disciplinas, codigo, nota, matricula):
    
    if matricula not in alunos:
        print("Erro: Aluno não encontrado.")
    elif codigo not in disciplinas:
        print("Erro: Disciplina não encontrada.")
    elif codigo not in alunos[matricula]["disciplinas"]:
        print("Aviso: Aluno não está matriculado nesta disciplina.")
    else:
        if nota < 0 or nota > 10:
            print("Nota inválida. A nota deve ser entre 0 e 10.")
        else:
            alunos[matricula]["notas"][codigo].append(nota)
            print(f"Nota {nota} lançada para {alunos[matricula]['nome']} em {disciplinas[codigo]['nome']} com sucesso.")

def listar_alunos(alunos):
    
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- Lista de Alunos ---")
        for matricula, dados in alunos.items():
            print(f"Matrícula: {matricula} | Nome: {dados['nome']}")
        print("-" * 25)

def listar_disciplinas(disciplinas):
    
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
    else:
        print("\n--- Lista de Disciplinas ---")
        for codigo, dados in disciplinas.items():
            print(f"Código: {codigo} | Nome: {dados['nome']}")
        print("-" * 25)

def listar_alunos_disciplina(disciplinas, alunos, codigo):
    
    if codigo not in disciplinas:
        print("Erro: Disciplina não encontrada.")
    else:
        print(f"\n--- Alunos em {disciplinas[codigo]['nome']} ---")
        if not disciplinas[codigo]['alunos']:
            print("Nenhum aluno matriculado nesta disciplina.")
        else:
            for matricula_aluno in sorted(list(disciplinas[codigo]['alunos'])):
                print(f"Matrícula: {matricula_aluno} | Nome: {alunos[matricula_aluno]['nome']}")
        print("-" * 25)

def exibir_boletim(alunos, disciplinas, matricula):
    
    if matricula not in alunos:
        print("Erro: Aluno não encontrado.")
        return

    dados_aluno = alunos[matricula]
    print(f"\n--- Boletim de {dados_aluno['nome']} ({matricula}) ---")
    
    if not dados_aluno["disciplinas"]:
        print("O aluno não está matriculado em nenhuma disciplina.")
        return

    for codigo_disciplina in dados_aluno["disciplinas"]:
        nome_disciplina = disciplinas[codigo_disciplina]["nome"]
        notas_disciplina = dados_aluno["notas"].get(codigo_disciplina, [])
        
        if notas_disciplina:
            media_disciplina = sum(notas_disciplina) / len(notas_disciplina)
            status = "APROVADO" if media_disciplina >= 6.0 else "REPROVADO"
            notas_str = ', '.join(map(str, notas_disciplina))
            print(f"Disciplina: {nome_disciplina} | Notas: [{notas_str}] | Média: {media_disciplina:.2f} | Status: {status}")
        else:
            print(f"Disciplina: {nome_disciplina} | Sem notas lançadas.")
    print("-" * 25)

def calcular_media_geral(alunos, matricula):
    
    if matricula not in alunos:
        print("Erro: Aluno não encontrado.")
        return None
    
    dados_aluno = alunos[matricula]
    todas_notas = []
    
    for notas_disciplina in dados_aluno["notas"].values():
        todas_notas.extend(notas_disciplina)
    
    if not todas_notas:
        print("Nenhuma nota lançada para este aluno.")
        return None
    
    media = sum(todas_notas) / len(todas_notas)
    return media

def aprovado_em_todas(alunos, matricula):
   
    if matricula not in alunos:
        print("Erro: Aluno não encontrado.")
        return False
    
    dados_aluno = alunos[matricula]
    
    for codigo_disciplina in dados_aluno["disciplinas"]:
        notas = dados_aluno["notas"].get(codigo_disciplina, [])
        if not notas or (sum(notas) / len(notas)) < 6.0:
            return False
    
    return True

def alterar_nome_aluno(alunos, matricula, novo_nome):
   
    if matricula not in alunos:
        print("Erro: Aluno não encontrado.")
    else:
        alunos[matricula]['nome'] = novo_nome
        print(f"Nome do aluno com matrícula '{matricula}' alterado para '{novo_nome}'.")

def alterar_nome_disciplina(disciplinas, codigo, novo_nome):
   
    if codigo not in disciplinas:
        print("Erro: Disciplina não encontrada.")
    else:
        disciplinas[codigo]['nome'] = novo_nome
        print(f"Nome da disciplina com código '{codigo}' alterado para '{novo_nome}'.")

def excluir_aluno(alunos, disciplinas, matricula):
    
    if matricula not in alunos:
        print("Erro: Aluno não encontrado.")
    else:
        disciplinas_do_aluno = list(alunos[matricula]['disciplinas'])
        for codigo_disciplina in disciplinas_do_aluno:
            if codigo_disciplina in disciplinas:
                disciplinas[codigo_disciplina]['alunos'].discard(matricula)
        
        del alunos[matricula]
        print(f"Aluno com matrícula '{matricula}' e suas matrículas removidos.")

def excluir_disciplina(disciplinas, alunos, codigo):
   
    if codigo not in disciplinas:
        print("Erro: Disciplina não encontrada.")
    else:
        alunos_da_disciplina = list(disciplinas[codigo]['alunos'])
        for matricula_aluno in alunos_da_disciplina:
            if matricula_aluno in alunos:
                alunos[matricula_aluno]['disciplinas'].discard(codigo)
                if codigo in alunos[matricula_aluno]['notas']:
                    del alunos[matricula_aluno]['notas'][codigo]
        
        del disciplinas[codigo]
        print(f"Disciplina com código '{codigo}' e todas as suas matrículas removidas.")