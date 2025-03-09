class Observable:
    """
    A class representing an observable object.
    Observers can be added, removed, and notified of changes in the observable object.
    Attributes:
        _observers (list): A list of observers subscribed to the observable object.
    Methods:
        add_observer(observer): Adds an observer to the list of subscribers.
        remove_observer(observer): Removes an observer from the list of subscribers.
        notify_observers(message): Notifies all observers with a given message.
    """

    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        """
        Adds an observer to the list of observers.
        Parameters:
        - observer: The observer object to be added.
        Returns:
        None
        """

        self._observers.append(observer)

    def remove_observer(self, observer):
        """
        Removes an observer from the list of observers.
        Parameters:
        observer (object): The observer to be removed.
        Returns:
        None
        """

        self._observers.remove(observer)

    def notify_observers(self, message):
        """
        Notifies all the observers with the given message.
        Parameters:
        - message (str): The message to be sent to the observers.
        Returns:
        - None
        """

        for observer in self._observers:
            observer.update(message)


class Observer:
    """
    Represents an observer in the Observer design pattern.
    Methods:
        update(message): This method should be implemented by the subclasses.
    """

    pass

    def update(self, message):
        """
        This method should be implemented by the subclasses.
        """
        pass

        pass  # Este método debe ser implementado por las subclases
