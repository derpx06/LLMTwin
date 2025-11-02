from InstructorEmbedding import INSTRUCTOR

# Load the model
model = INSTRUCTOR("hkunlp/instructor-base")

# Example input
sentence = "RAG Fundamentals First"
instruction = "Represent the title of an article about AI:"

# Encode with instruction + sentence
embeddings = model.encode([[instruction, sentence]])

print(embeddings.shape)
