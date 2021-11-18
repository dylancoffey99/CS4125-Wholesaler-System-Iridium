"""
This module contains the abstract classes AbstractSubject and AbstractObserver.
The module imports ABC (Abstract Base Class) and abstractmethod from the abc module.
"""
from abc import ABC, abstractmethod


class AbstractSubject(ABC):
    """
    This abstract class represents an interface subject, containing the abstract
    methods to be implemented in subject classes.
    """
    @abstractmethod
    def attach(self, observer):
        """
        This method appends an observer to a list.

        :param observer: Observer to be appended to a list.
        """

    @abstractmethod
    def detach(self, observer):
        """
        This method removes an observer from a list.

        :param observer: Observer to be removed from a list.
        """

    @abstractmethod
    def notify(self):
        """This method notifies the observers when a change has been made."""


class AbstractObserver(ABC):
    """
    This abstract class represents an interface observer, containing the abstract
    methods to be implemented in observer classes.
    """
    @abstractmethod
    def update(self, subject):
        """This method updates a subject when the observer is notified."""



class IObserver(ABC):
    @abstractmethod
    def update(self, subject):
        pass
