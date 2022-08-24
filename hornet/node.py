"""Expose a node."""
import graphviz as _graphviz
from hornet import state as _state


class Node:
    """Represent a node."""

    def __init__(self, identity: str, attrs: dict = {}):
        """Put a node in a graph."""
        self.identity = identity
        self.digraph: _graphviz.Digraph = _state.get_digraph()
        self.digraph.node(self.identity, None, attrs)

    def __lt__(self, other: "Node") -> "Node":
        """Implement '<'."""
        self._select_inner(other).edge(
            self.identity,
            other.identity,
        )
        return other

    def __sub__(self, other: "Node") -> "Node":
        """Implement - ."""
        self._select_inner(other).edge(
            self.identity,
            other.identity,
            None,
            arrowhead="none",
            arrowtail="none",
        )
        return other

    def _select_inner(self, other: "None") -> _graphviz.Digraph:
        return _state.select_inner(self.digraph, other.digraph)
