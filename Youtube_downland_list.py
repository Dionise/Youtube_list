import pafy
url = []
locald=input( "Save in preferred location see more information in readme.txt:")
numar_lista = int(input("How much songs do you want do downland: "))
for i in range(0, numar_lista):
    print(f"Source {i}:",end=' ')
    item = input()
    url.append(item)
for resultat in url:
    print(resultat)
    result = pafy.new(resultat)
    bestaudio =result.getbestaudio()
    filename = bestaudio.download(filepath=locald)