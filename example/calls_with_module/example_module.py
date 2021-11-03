import os
import time

from pyrogram import Client

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream

app = Client(
    'py-tgcalls',
    api_id=5538260,
    api_hash='f2551d144689f3f7d8500b2da0b59606',
)

call_py = PyTgCalls(app)
if __name__ == '__main__':
    call_py.start()
    file = '../input.raw'
    while not os.path.exists(file):
        time.sleep(0.125)
    call_py.join_group_call(
        -1001234567890,
        InputAudioStream(
            file,
        ),
        stream_type=StreamType().local_stream,
    )
    idle()
