import ollama

texto = "Obrigada, professor Thiago Medeiros Barros."
modelo = "nomic-embed-text"

print(f"Texto: {texto}\n")
print(f"Modelo: {modelo}\n")

resposta = ollama.embed(model=modelo, input=texto)
vetor = resposta["embeddings"][0]

print(f"Tamanho do vetor: {len(vetor)} dimensões")
print(f"Primeiros 10 valores: {vetor[:10]}")
print(f"Últimos 5 valores: {vetor[-5:]}")
