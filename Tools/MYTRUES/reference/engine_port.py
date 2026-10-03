from abc import ABC, abstractmethod


class DecisionEngine(ABC):
    """
    Internal port.

    This interface is intentionally much smaller than the public protocol.
    A production/proprietary engine can implement it without exposing its
    retrieval, scoring, ranking or learning algorithm.
    """

    @abstractmethod
    def choose(self, request: dict, candidates: list[dict]) -> dict:
        raise NotImplementedError
