from src import graph, AppContext

def main():
    inputs = {
        "input": "LangGraph demo!",
        "results": ""
    }

    context_instance = AppContext(description="My first langgraph setup")

    final_output = graph.invoke(
        inputs,
        context=context_instance
    )
    print(f"Inputs: {final_output['input']}")
    print(f"Results: {final_output['results']}")


if __name__ == "__main__":
    main()
