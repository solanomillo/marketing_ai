from services.graph_service import get_graph

graph = get_graph()

config = {
    "configurable": {
        "thread_id": "usuario_1"
    }
}

state = graph.get_state(config)

print(type(state))

print("\nVALORES\n")
print(state.values)

print("\nCLAVES\n")
print(state.values.keys())