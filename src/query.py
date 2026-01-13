def run_query(query, retriever, generator):
    context = retriever(query)
    answer = generator(context, query)
    print(answer)
