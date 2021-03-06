# coding=utf-8
import attr
import sys
import typing

from . import topics as topics
from utils import logger_error
from patterns import Pub, Sub, PubSubEvent
from domain.messages.services import MessagesInterface


@attr.s
class ControllerEventsObserver(Pub):
    """ Control/Management events (sensor data controller)
    """
    queue: typing.Any = attr.ib()
    messages_service: MessagesInterface = attr.ib()
    _observers: typing.List[Sub] = attr.ib(default=attr.Factory(list))

    # POST INIT HOOK
    def __attrs_post_init__(self):
        pass

    # PATTERN METHODS
    def attach(self, observer: Sub) -> None:
        """
        Function to add an observer

        Args:
            observer (Sub): observador
        """
        self._observers.append(observer)

    def detach(self, observer: Sub) -> None:
        """
        Function to delete an observer

        Args:
            observer (Sub): observador
        """
        self._observers.remove(observer)

    def notify(self, event: PubSubEvent) -> None:
        """
        Notify event to all observers

        Args:
            event (PubSubEvent): event to inform about the status change
        """
        for observer in self._observers:
            observer.update(event)

    # METHODS
    def __manage_controller_status(self, client, userdata: dict, mensaje) -> None:
        """
        Function to handle the new status from the controller

        Args:
            client (paho.mqtt.client.Client): client's info
            userdata (dict)
            mensaje (paho.mqtt.client.MQTTMessage): payload
        """
        try:
            self.notify(event=PubSubEvent(
                type=topics.CONTROLLER_STATUS,
                data={
                    'topic': mensaje.topic,
                    'payload': mensaje.payload
                }
            ))
        except Exception as error:
            self.queue.put(sys.exc_info())
            logger_error(
                nombre="__manage_controller_status",
                error=error
            )

    def init_subs(self) -> None:
        self.messages_service.sub_sensors_status_controllers(
            callback=self.__manage_controller_status)
