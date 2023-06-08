from maubot import Plugin
from maubot.handlers import event
from mautrix.types import EventType, StateEvent

class qabot(Plugin):
  @event.on(EventType.ROOM_MESSAGE)
  async def handle_message(self, evt: StateEvent) -> None:
    self.log.info(f"{evt.room_id} received a message")
    await self.client.send_text(evt.room_id, "Received message")
