# Agentic Experiment

## Organization

### `Nodes`

-  Purpose: the functional logic that takes state + context as input and outputs a new state.

### `state.py`

- Purpose: the schema of a graph. 
> Note: only one state per graph, but each graph may contain multiple subgraphs.

### `Tools`

- Purpose: Specialized nodes that can be activated in the `messages` variable (i.e., 'tool call') and produce a new state.

### `graph.py`

- Purpose: Orchastrate the behavior of nodes.

### `context.py`

- Purpose: the static personality of the agent.
> Note: A parent's context is unidirectionally available to downstream graphs.