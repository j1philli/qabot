from typing import Type
from maubot import Plugin
from maubot.handlers import event
from mautrix.types import EventType, MessageEvent
from mautrix.util.config import BaseProxyConfig, ConfigUpdateHelper
import asyncio
from websockets.server import serve

class Config(BaseProxyConfig):
    def do_update(self, helper: ConfigUpdateHelper) -> None:
        helper.copy("server-ip")
        helper.copy("server-port")

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def websocket():
    async with serve(echo, config.get, 8765):
        await asyncio.Future()  # run forever

class QaBot(Plugin):
  async def start(self) -> None:
    await super().start()
    self.config.load_and_update()
    await websocket()
    self.log.debug("start def ran")

  async def websocket(self):
    async with serve(echo, self.config.get["server-host"] , self.config.get["server-ip"]):
        await asyncio.Future()  # run forever


  @classmethod
  def get_config_class(cls) -> Type[BaseProxyConfig]:
        return Config
  
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