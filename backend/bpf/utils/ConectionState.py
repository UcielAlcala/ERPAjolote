from enum import Enum


class ConnectionState(Enum):
    """
    Represents the different connection states for an MQTT connection.
    Attributes:
        NO_STATE (int): Represents no connection state.
        CONNECTED (int): Represents a connected state.
        DISCONNECTED (int): Represents a disconnected state.
        PAUSED (int): Represents a paused state.
        QUIT (int): Represents a quit state.
    """

    NO_STATE = 0
    CONNECTED = 1
    DISCONNECTED = 2
