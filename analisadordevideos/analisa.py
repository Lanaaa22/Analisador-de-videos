from pytubefix import YouTube
import whisper
import shutil

def baixa_audio(link):
    try:
        yt = YouTube(link)
        st = yt.streams
        audio_stream = yt.streams.filter(only_audio=True).first()

        if audio_stream:
            baixa = audio_stream.download()
            print("DOWNLOAD FEITO COM SUCESSO")
            return baixa
        else:
            print("AUDIO INDISPONÍVEL")
            return None
    except Exception as e:
        print(f"Erro ao extrair o áudio: {e}")
        return None
    
def transcreve_audio():
    modelo = whisper.load_model("base")

    resposta = modelo.transcribe("Gravando.m4a")
    texto = resposta['text']
    return texto

def arquiva(a, t):
    with open(a, "w", encoding="utf-8") as arquivo:
        arquivo.write(t)


def main():
    link = str()
    link = input("Digite o link do audio:")
    arquivo = input("Digite o nome do arquivo desejado: ")
    nome_antigo = baixa_audio(link)
    if nome_antigo:
        novo_nome = "Gravando.m4a"
        try:
            shutil.move(nome_antigo, novo_nome)
            print(f"Áudio salvo como {novo_nome}")
            transcreve = transcreve_audio()
        except Exception as e:
            print(f"Erro ao renomear ou mover o arquivo: {e}")
    arquiva(arquivo, transcreve)


    transcreve_audio()

if __name__ == "__main__":
    main()