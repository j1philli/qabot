from typing import Type
from maubot import Plugin
from maubot.handlers import event
from mautrix.types import EventType, MessageEvent
from websockets.server import serve
import asyncio
from mautrix.util.config import BaseProxyConfig, ConfigUpdateHelper

class Config(BaseProxyConfig):
    def do_update(self, helper: ConfigUpdateHelper) -> None:
        helper.copy("server-ip")
        helper.copy("server-port")

async def main(self):
  async with serve(echo, self.config["server-host"], self.config["server-ip"]):
    await asyncio.Future()  # run forever

class QaBot(Plugin):
  async def start(self) -> None:
    self.config.load_and_update()

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

  @classmethod
  def get_config_class(cls) -> Type[BaseProxyConfig]:
        return Config