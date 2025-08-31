
from funcoes import *

disciplinas = {
    "D01": {"nome": "Lógica de Programação", "alunos": {"20230001","20230002","20230005","20230008","20230010","20230012","20230015","20230018","20230020","20230022","20230025","20230028","20230030","20230033","20230035","20230038","20230040","20230043","20230045","20230048","20230050"}},
    "D02": {"nome": "Estrutura de Dados", "alunos": {"20230001","20230003","20230006","20230009","20230011","20230014","20230017","20230019","20230021","20230024","20230027","20230029","20230032","20230034","20230037","20230039","20230042","20230044","20230047","20230049","20230050"}},
    "D03": {"nome": "Programação Orientada a Objetos", "alunos": {"20230002","20230003","20230005","20230007","20230010","20230013","20230016","20230018","20230020","20230023","20230026","20230029","20230031","20230034","20230036","20230039","20230041","20230044","20230046","20230049","20230050"}},
    "D04": {"nome": "Banco de Dados", "alunos": {"20230001","20230004","20230005","20230008","20230011","20230014","20230017","20230019","20230022","20230025","20230028","20230030","20230033","20230036","20230038","20230041","20230043","20230046","20230048","20230050"}},
    "D05": {"nome": "Programação Web", "alunos": {"20230001","20230002","20230003","20230006","20230009","20230012","20230015","20230018","20230021","20230024","20230027","20230030","20230033","20230036","20230039","20230042","20230045","20230048","20230049","20230050"}},
    "D06": {"nome": "Engenharia de Software", "alunos": {"20230003","20230005","20230007","20230010","20230013","20230016","20230019","20230022","20230025","20230028","20230031","20230034","20230037","20230040","20230043","20230046","20230048","20230049","20230050"}},
    "D07": {"nome": "Desenvolvimento Mobile", "alunos": {"20230002","20230004","20230005","20230008","20230011","20230014","20230017","20230020","20230023","20230026","20230029","20230032","20230035","20230038","20230041","20230044","20230047","20230048","20230050"}},
    "D08": {"nome": "Redes de Computadores", "alunos": {"20230001","20230003","20230005","20230007","20230009","20230012","20230015","20230018","20230021","20230024","20230027","20230030","20230033","20230036","20230039","20230042","20230045","20230048","20230049","20230050"}},
    "D09": {"nome": "Sistemas Operacionais", "alunos": {"20230001","20230002","20230004","20230006","20230009","20230012","20230015","20230018","20230021","20230024","20230027","20230030","20230033","20230036","20230039","20230042","20230045","20230048","20230049","20230050"}},
    "D10": {"nome": "DevOps e Integração Contínua", "alunos": {"20230003","20230004","20230005","20230007","20230010","20230013","20230016","20230019","20230022","20230025","20230028","20230031","20230034","20230037","20230040","20230043","20230046","20230048","20230049","20230050"}}
}

alunos = {
    "20230001": {"nome": "Ana Beatriz da Silva", "disciplinas": {"D01","D02","D04","D05","D08","D09"},
                 "notas": {"D01":[8.7,9.1], "D02":[7.9,8.3], "D04":[8.0,8.5], "D05":[7.8,8.2], "D08":[9.0,8.7], "D09":[7.5,8.0]}},
    "20230002": {"nome": "João Luiz Pereira", "disciplinas": {"D01","D03","D05","D07","D09"},
                 "notas": {"D01":[6.5,7.2], "D03":[8.8,9.0], "D05":[7.5,7.9], "D07":[7.2,7.6], "D09":[8.1,8.5]}},
    "20230003": {"nome": "Carla Fernanda Santos", "disciplinas": {"D02","D03","D05","D06","D08","D10"},
                 "notas": {"D02":[9.0,8.5], "D03":[8.9,9.2], "D05":[7.8,8.0], "D06":[8.3,8.7], "D08":[8.5,8.9], "D10":[7.3,7.8]}},
    "20230004": {"nome": "Carlos Eduardo Souza", "disciplinas": {"D02","D04","D07","D09","D10"},
                 "notas": {"D02":[7.5,8.0], "D04":[8.1,7.9], "D07":[6.8,7.0], "D09":[7.7,8.1], "D10":[8.2,8.5]}},
    "20230005": {"nome": "Mariana Oliveira Lima", "disciplinas": {"D01","D03","D04","D06","D07","D08","D10"},
                 "notas": {"D01":[7.5,8.2], "D03":[8.2,8.6], "D04":[7.9,8.3], "D06":[8.5,8.9], "D07":[7.0,7.4], "D08":[9.1,8.7], "D10":[8.0,8.4]}},
    "20230006": {"nome": "Pedro Henrique Costa", "disciplinas": {"D02","D05","D09"},
                 "notas": {"D02":[7.0,7.4], "D05":[6.9,7.2], "D09":[7.3,7.6]}},
    "20230007": {"nome": "Fernanda Lima Rocha", "disciplinas": {"D03","D06","D08","D10"},
                 "notas": {"D03":[8.0,8.4], "D06":[7.5,7.9], "D08":[8.2,8.6], "D10":[7.9,8.3]}},
    "20230008": {"nome": "Lucas Gabriel Ferreira", "disciplinas": {"D01","D04","D07"},
                 "notas": {"D01":[7.6,8.0], "D04":[7.8,8.1], "D07":[7.2,7.6]}},
    "20230009": {"nome": "Juliana Alves Mendes", "disciplinas": {"D02","D05","D09"},
                 "notas": {"D02":[8.1,8.5], "D05":[7.0,7.4], "D09":[7.8,8.2]}},
    "20230010": {"nome": "Rafael Martins Gomes", "disciplinas": {"D01","D03","D06","D10"},
                 "notas": {"D01":[8.0,8.3], "D03":[7.9,8.2], "D06":[8.4,8.7], "D10":[7.5,7.9]}},
    "20230011": {"nome": "Beatriz Nunes Cardoso", "disciplinas": {"D02","D04","D07"}, "notas": {"D02":[7.8,8.2], "D04":[8.0,8.4], "D07":[7.1,7.5]}},
    "20230012": {"nome": "Gustavo Henrique Lima", "disciplinas": {"D01","D05"}, "notas": {"D01":[6.9,7.3], "D05":[7.0,7.5]}},
    "20230013": {"nome": "Larissa Souza Pires", "disciplinas": {"D03","D06","D10"}, "notas": {"D03":[8.3,8.7], "D06":[7.5,7.8], "D10":[8.1,8.5]}},
    "20230014": {"nome": "Thiago Alves Santos", "disciplinas": {"D02","D04","D07"}, "notas": {"D02":[7.4,7.9], "D04":[8.2,8.6], "D07":[6.9,7.3]}},
    "20230015": {"nome": "Amanda Ferreira Gomes", "disciplinas": {"D01","D05","D08","D09"}, "notas": {"D01":[8.1,8.4], "D05":[7.7,8.0], "D08":[8.9,9.2], "D09":[7.6,8.0]}},
    "20230016": {"nome": "Felipe Costa Rocha", "disciplinas": {"D03","D06","D10"}, "notas": {"D03":[7.8,8.1], "D06":[8.0,8.4], "D10":[7.2,7.6]}},
    "20230017": {"nome": "Natália Mendes Lima", "disciplinas": {"D02","D04","D07"}, "notas": {"D02":[7.5,7.9], "D04":[8.3,8.6], "D07":[7.0,7.4]}},
    "20230018": {"nome": "Vitor Hugo Cardoso", "disciplinas": {"D01","D05","D08"}, "notas": {"D01":[8.3,8.7], "D05":[7.5,7.8], "D08":[9.0,8.5]}},
    "20230019": {"nome": "Isabela Rocha Souza", "disciplinas": {"D02","D06","D10"}, "notas": {"D02":[7.9,8.3], "D06":[8.2,8.5], "D10":[7.8,8.1]}},
    "20230020": {"nome": "Gabriel Lima Ferreira", "disciplinas": {"D01","D03","D04","D07"}, "notas": {"D01":[8.0,8.3], "D03":[7.7,8.0], "D04":[8.1,8.4], "D07":[7.3,7.6]}},
    "20230021": {"nome": "Camila Alves Mendes", "disciplinas": {"D02","D05","D09"}, "notas": {"D02":[8.2,8.6], "D05":[7.3,7.7], "D09":[7.9,8.3]}},
    "20230022": {"nome": "Lucas Eduardo Gomes", "disciplinas": {"D01","D04","D06"}, "notas": {"D01":[7.8,8.1], "D04":[8.0,8.3], "D06":[8.1,8.5]}},
    "20230023": {"nome": "Juliana Rocha Lima", "disciplinas": {"D03","D05","D08"}, "notas": {"D03":[8.1,8.4], "D05":[7.7,8.0], "D08":[8.5,8.8]}},
    "20230024": {"nome": "Rafael Costa Nunes", "disciplinas": {"D02","D05","D09"}, "notas": {"D02":[7.5,7.9], "D05":[7.1,7.5], "D09":[7.6,8.0]}},
    "20230025": {"nome": "Ana Clara Lima", "disciplinas": {"D01","D04","D06","D10"}, "notas": {"D01":[8.0,8.3], "D04":[7.9,8.2], "D06":[8.3,8.6], "D10":[7.5,7.8]}},
    "20230026": {"nome": "Mateus Henrique Silva", "disciplinas": {"D03","D07"}, "notas": {"D03":[7.8,8.1], "D07":[7.0,7.3]}},
    "20230027": {"nome": "Larissa Souza Lima", "disciplinas": {"D02","D05","D09"}, "notas": {"D02":[7.9,8.2], "D05":[7.2,7.6], "D09":[7.8,8.1]}},
    "20230028": {"nome": "Vitor Eduardo Gomes", "disciplinas": {"D01","D04","D06"}, "notas": {"D01":[8.2,8.5], "D04":[8.0,8.3], "D06":[8.1,8.4]}},
    "20230029": {"nome": "Mariana Alves Rocha", "disciplinas": {"D02","D03","D05","D10"}, "notas": {"D02":[7.8,8.1], "D03":[8.0,8.3], "D05":[7.3,7.6], "D10":[7.5,7.8]}},
    "20230030": {"nome": "Felipe Costa Lima", "disciplinas": {"D01","D04","D05","D08","D09"}, "notas": {"D01":[8.0,8.3], "D04":[7.8,8.2], "D05":[7.6,7.9], "D08":[8.9,9.2], "D09":[7.7,8.0]}},
    "20230031": {"nome": "Isabela Mendes Silva", "disciplinas": {"D03","D06","D10"}, "notas": {"D03":[8.2,8.5], "D06":[8.0,8.4], "D10":[7.8,8.1]}},
    "20230032": {"nome": "Pedro Lima Rocha", "disciplinas": {"D02","D07"}, "notas": {"D02":[7.5,7.9], "D07":[7.2,7.6]}},
    "20230033": {"nome": "Larissa Oliveira Gomes", "disciplinas": {"D01","D04","D05","D08"}, "notas": {"D01":[8.1,8.4], "D04":[7.9,8.3], "D05":[7.5,7.8], "D08":[8.8,9.1]}},
    "20230034": {"nome": "Lucas Rocha Silva", "disciplinas": {"D02","D03","D06","D10"}, "notas": {"D02":[7.8,8.1], "D03":[8.0,8.3], "D06":[8.1,8.4], "D10":[7.5,7.8]}},
    "20230035": {"nome": "Camila Costa Nunes", "disciplinas": {"D01","D05","D07"}, "notas": {"D01":[8.0,8.3], "D05":[7.2,7.5], "D07":[7.0,7.3]}},
    "20230036": {"nome": "Vitor Lima Rocha", "disciplinas": {"D03","D05","D08","D09"}, "notas": {"D03":[7.9,8.2], "D05":[7.5,7.8], "D08":[8.5,8.9], "D09":[7.6,8.0]}},
    "20230037": {"nome": "Juliana Mendes Costa", "disciplinas": {"D02","D06","D10"}, "notas": {"D02":[7.7,8.0], "D06":[8.0,8.3], "D10":[7.5,7.8]}},
    "20230038": {"nome": "Rafael Oliveira Lima", "disciplinas": {"D01","D04","D07","D08"}, "notas": {"D01":[8.2,8.5], "D04":[7.8,8.1], "D07":[7.2,7.5], "D08":[8.9,9.2]}},
    "20230039": {"nome": "Amanda Rocha Silva", "disciplinas": {"D02","D03","D05","D08"}, "notas": {"D02":[7.8,8.2], "D03":[8.0,8.4], "D05":[7.3,7.7], "D08":[8.6,8.9]}},
    "20230040": {"nome": "Felipe Mendes Costa", "disciplinas": {"D01","D06","D10"}, "notas": {"D01":[8.0,8.3], "D06":[8.2,8.5], "D10":[7.5,7.9]}},
    "20230041": {"nome": "Isabela Lima Rocha", "disciplinas": {"D03","D07","D08"}, "notas": {"D03":[8.1,8.5], "D07":[7.1,7.5], "D08":[8.3,8.7]}},
    "20230042": {"nome": "Pedro Costa Nunes", "disciplinas": {"D02","D05","D09"}, "notas": {"D02":[7.5,7.9], "D05":[7.2,7.6], "D09":[7.6,8.0]}},
    "20230043": {"nome": "Camila Oliveira Silva", "disciplinas": {"D01","D04","D06","D10"}, "notas": {"D01":[8.1,8.4], "D04":[7.9,8.3], "D06":[8.2,8.5], "D10":[7.5,7.8]}},
    "20230044": {"nome": "Lucas Mendes Rocha", "disciplinas": {"D02","D03","D07"}, "notas": {"D02":[7.8,8.2], "D03":[8.0,8.4], "D07":[7.2,7.6]}},
    "20230045": {"nome": "Juliana Lima Costa", "disciplinas": {"D01","D05","D08","D09"}, "notas": {"D01":[8.0,8.3], "D05":[7.5,7.9], "D08":[8.7,9.0], "D09":[7.6,8.0]}},
    "20230046": {"nome": "Rafael Mendes Lima", "disciplinas": {"D03","D06","D10"}, "notas": {"D03":[8.0,8.3], "D06":[8.2,8.5], "D10":[7.5,7.9]}},
    "20230047": {"nome": "Amanda Lima Silva", "disciplinas": {"D02","D07"}, "notas": {"D02":[7.7,8.0], "D07":[7.1,7.4]}},
    "20230048": {"nome": "Felipe Oliveira Costa", "disciplinas": {"D01","D05","D08","D10"}, "notas": {"D01":[8.2,8.5], "D05":[7.5,7.8], "D08":[8.9,9.2], "D10":[7.5,7.9]}},
    "20230049": {"nome": "Isabela Costa Rocha", "disciplinas": {"D02","D03","D08","D10"}, "notas": {"D02":[7.8,8.2], "D03":[8.0,8.4], "D08":[8.5,8.9], "D10":[7.5,7.9]}},
    "20230050": {"nome": "Lucas Lima Mendes", "disciplinas": {"D01","D02","D03","D04","D05","D06","D07","D08","D09","D10"},
                 "notas": {"D01":[8.0,8.3], "D02":[7.8,8.1], "D03":[8.2,8.5], "D04":[7.9,8.2], "D05":[7.5,7.8], "D06":[8.1,8.4], "D07":[7.2,7.5], "D08":[8.5,8.8], "D09":[7.7,8.0], "D10":[7.9,8.3]}}
}

def menu():

    print("\n===== SISTEMA ACADÊMICO =====")
    print("1. Cadastrar aluno")
    print("2. Cadastrar disciplina")
    print("3. Matricular aluno em disciplina")
    print("4. Lançar nota para aluno em disciplina")
    print("5. Listar todos os alunos")
    print("6. Listar todas as disciplinas")
    print("7. Listar alunos de uma disciplina")
    print("8. Exibir boletim de um aluno")
    print("9. Calcular média geral do aluno")
    print("10. Mostrar status de aprovação (todas as disciplinas >= 6.0)")
    print("11. Alterar nome de aluno")
    print("12. Alterar nome de disciplina")
    print("13. Excluir aluno")
    print("14. Excluir disciplina")
    print("0. Sair")

def main():
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            matricula = input("Digite a matrícula do aluno: ").strip()
            nome = input("Digite o nome do aluno: ").strip()
            cadastrar_aluno(alunos, matricula, nome)
        elif opcao == "2":
            codigo = input("Digite o código da disciplina: ").strip().upper()
            nome = input("Digite o nome da disciplina: ").strip()
            cadastrar_disciplina(disciplinas, codigo, nome)
        elif opcao == "3":
            matricula = input("Digite a matrícula do aluno: ").strip()
            codigo = input("Digite o código da disciplina: ").strip().upper()
            matricular_aluno(alunos, disciplinas, matricula, codigo)
        elif opcao == "4":
            matricula = input("Digite a matrícula do aluno: ").strip()
            codigo = input("Digite o código da disciplina: ").strip().upper()
            try:
                nota = float(input("Digite a nota (0 a 10): "))
                lancar_nota(alunos, disciplinas, codigo, nota, matricula)
            except ValueError:
                print("Nota inválida! Digite um número.")
        elif opcao == "5":
            listar_alunos(alunos)
        elif opcao == "6":
            listar_disciplinas(disciplinas)
        elif opcao == "7":
            codigo = input("Digite o código da disciplina: ").strip().upper()
            listar_alunos_disciplina(disciplinas, alunos, codigo)
        elif opcao == "8":
            matricula = input("Digite a matrícula do aluno: ").strip()
            exibir_boletim(alunos, disciplinas, matricula)
        elif opcao == "9":
            matricula = input("Digite a matrícula do aluno: ").strip()
            media = calcular_media_geral(alunos, matricula)
            if media is not None:
                print(f"Média geral de {alunos[matricula]['nome']}: {media:.2f}")
        elif opcao == "10":
            matricula = input("Digite a matrícula do aluno: ").strip()
            if aprovado_em_todas(alunos, matricula):
                print(f"{alunos[matricula]['nome']} está aprovado em todas as disciplinas.")
            else:
                print(f"{alunos[matricula]['nome']} não está aprovado em todas as disciplinas.")
        elif opcao == "11":
            matricula = input("Digite a matrícula do aluno: ").strip()
            novo_nome = input("Digite o novo nome: ").strip()
            alterar_nome_aluno(alunos, matricula, novo_nome)
        elif opcao == "12":
            codigo = input("Digite o código da disciplina: ").strip().upper()
            novo_nome = input("Digite o novo nome: ").strip()
            alterar_nome_disciplina(disciplinas, codigo, novo_nome)
        elif opcao == "13":
            matricula = input("Digite a matrícula do aluno a ser excluído: ").strip()
            excluir_aluno(alunos, disciplinas, matricula)
        elif opcao == "14":
            codigo = input("Digite o código da disciplina a ser excluída: ").strip().upper()
            excluir_disciplina(disciplinas, alunos, codigo)
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()