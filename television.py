class Television:

    """Represents a television with features including power on/off, controlling channels, and controlling volume"""

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:

        """Initializes the television with it's default settings"""

        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:

        """Turns the TV on or off"""

        self.__status = not self.__status

    def mute(self) -> None:

        """Mutes or unmutes the TV when it is on"""

        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:

        """Increases the channel by 1, returning to the minimum channel after reaching the maximum"""

        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:

        """Decreases the channel by 1, returning to the maximum channel after reaching the minimum"""
        
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:

        """Unmutes and increases the volume without exceeding the maximum threshold"""

        if self.__status:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:

        """Unmutes and decreases the volome without going below the minimum threshold"""

        if self.__status:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:

        """Returns the television's power, channel, and original volume"""

        if self.__muted:
            volume = self.MIN_VOLUME
        else:
            volume = self.__volume

        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"