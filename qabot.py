from maubot import Plugin
from maubot.handlers import event
from mautrix.types import EventType, MessageEvent

class QaBot(Plugin):
  @event.on(EventType.ROOM_MESSAGE)
  async def handle_message(self, evt: MessageEvent) -> None:
    self.log.info(f"{evt.room_id} received a message")
    # default = evt.sender != self.client.mxid and 'org.matrix.msc2716.historical' not in evt.content
    # messageTypes = {
    #   'reply' : default and 'm.relates_to' in evt.content
    # }
    if 'm.relates_to' in evt.content:
      self.log.info("true")
    else:
      self.log.info("false")
    self.log.info(evt.content)
    if evt.sender != self.client.mxid and 'org.matrix.msc2716.historical' not in evt.content and evt.content._relates_to != None:
      await self.client.send_text(evt.room_id, "Received reply message")
    elif evt.sender != self.client.mxid and 'org.matrix.msc2716.historical' not in evt.content:
      await self.client.send_text(evt.room_id, "Received normal message")