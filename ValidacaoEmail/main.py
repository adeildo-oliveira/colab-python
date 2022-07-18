import datetime
from validacao_email import ValidacaoEmail

def executa_teste_performance_split(interacoes, email):
        media = 0
        itens_media = 0
        validacao_email = ValidacaoEmail()

        for _ in range(interacoes):
            start_time = datetime.datetime.now()

            _= validacao_email.email_validacao_split(email)

            end_time = datetime.datetime.now()
            diferenca = end_time - start_time
            media += diferenca.microseconds
            itens_media += 1
  
        print(f"MÉDIA: {media / itens_media} ms => Interações: {itens_media}")

def executa_teste_performance_regex(interacoes, email):
        media = 0
        itens_media = 0
        validacao_email = ValidacaoEmail()

        for i in range(interacoes):
            start_time = datetime.datetime.now()

            _= validacao_email.email_validado(email)

            end_time = datetime.datetime.now()

            diferenca = end_time - start_time
            media += diferenca.microseconds
            itens_media += 1

        print(f"MÉDIA: {media / itens_media} ms => Interações: {itens_media}")


if __name__ == '__main__':
    print("Executando teste com split:")
    executa_teste_performance_split(10, "popular_website15@comPany.com")
    executa_teste_performance_split(100, "popular_website15@comPany.com")
    executa_teste_performance_split(1000, "popular_website15@comPany.com")
    executa_teste_performance_split(10000, "popular_website15@comPany.com")
    executa_teste_performance_split(100000, "popular_website15@comPany.com")

    print("Executando teste com regex:")
    executa_teste_performance_regex(10, "popular_website15@comPany.com")
    executa_teste_performance_regex(100, "popular_website15@comPany.com")
    executa_teste_performance_regex(1000, "popular_website15@comPany.com")
    executa_teste_performance_regex(10000, "popular_website15@comPany.com")
    executa_teste_performance_regex(100000, "popular_website15@comPany.com")
