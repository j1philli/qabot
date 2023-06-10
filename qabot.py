from maubot import Plugin
from maubot.handlers import event
from mautrix.types import EventType, MessageEvent

class QaBot(Plugin):
  @event.on(EventType.ROOM_MESSAGE)
  async def handle_message(self, evt: MessageEvent) -> None:
    if evt.sender != self.client.mxid and 'org.matrix.msc2716.historical' not in evt.content and evt.content._relates_to != None:
      self.log.info(f"{evt.room_id} received a message I care about")
      await self.client.send_text(evt.room_id, "Received reply message")
    elif evt.sender != self.client.mxid and 'org.matrix.msc2716.historical' not in evt.content:
      self.log.info(f"{evt.room_id} received a message I care about")
      await self.client.send_text(evt.room_id, "Received normal message")
  
  @event.on(EventType.REACTION)
  async def handle_reactions(self, evt: MessageEvent) -> None:
    if evt.sender != self.client.mxid:
      self.log.info(f"{evt.room_id} received a reaction I care about")
      await self.client.send_text(evt.room_id, "Received reaction")