from maubot import Plugin
from maubot.handlers import event
from mautrix.types import EventType, MessageEvent

class QaBot(Plugin):
  @event.on(EventType.ROOM_MESSAGE)
  async def handle_message(self, evt: MessageEvent) -> None:
    self.log.info(f"{evt.room_id} received a message")

    if evt.sender != self.client.mxid or evt.content['org.matrix.msc2716.historical'] != True:
      await self.client.send_text(evt.room_id, "Received message")
